from flask import Flask, request, jsonify, render_template, abort
from datetime import datetime as dt
import os.path
import sql_func as sf


app = Flask(__name__)

db_file = "mydata.db"


# Declaring endpoint
@app.route("/")
def home():
    return render_template("index.html")


# Declaring endpoint and accepted method (by default only accept get)
@app.route("/send_data", methods=["POST", "GET"])
def send_data():
    try:
        if request.method == "GET":
            temp = float(request.args.get("temperature"))
            humi = float(request.args.get("humidity"))
            print(temp, humi)
        elif request.method == "POST":
            data = request.get_json(force=True)
            temp = float(data["temperature"])
            humi = float(data["humidity"])
    except (TypeError, ValueError, KeyError):
        abort(400, "Invalid or incomplete parameters")
    else:
        if not ((-50 <= temp <= 100) and (0 <= humi <= 100)):
            abort(400, "Invalid values")
        create_file = False if os.path.isfile(db_file) else True
        conn = sf.create_connection(db_file)
        with conn:
            if create_file:
                sf.create_table(conn)

            utcnow = dt.utcnow()
            timestamp = int(utcnow.timestamp())
            data = [timestamp, temp, humi]
            id = sf.insert_data(conn, data)

        output = dict(
            timestamp=utcnow.strftime("%Y/%m/%d %H:%M:%S"),
            temperature=temp,
            humidity=humi,
        )
        return jsonify(output)


# Declaring endpoint
@app.route("/get_data")
def get_data():
    try:
        n = int(request.args.get("n"))
    except (ValueError, TypeError):
        abort(400, "Invalid or incomplete parameters")
    else:
        if not os.path.isfile(db_file):
            return "No data"
        conn = sf.create_connection(db_file)
        with conn:
            rows = sf.get_latestdata(conn, n=n)
            if len(rows) == 0:
                return "No data"
            data = {"timestamp": [], "temperature": [], "humidity": []}
            data["timestamp"] = [row[0] for row in rows]
            data["temperature"] = [row[1] for row in rows]
            data["humidity"] = [row[2] for row in rows]
            return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
