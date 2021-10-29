import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.subplots
from datetime import datetime as dt, timedelta as td
import os.path
import sql_func as sf


app = dash.Dash()

db_file = "mydata.db"

# define the layout
app.layout = html.Div(
    html.Div(
        [
            html.H4("Temperature and Humidity"),
            html.Div(id="live-update-text"),
            dcc.Graph(id="live-update-graph"),
            dcc.Interval(
                id="interval-component",
                interval=1 * 1000,  # in milliseconds
                n_intervals=0,
            ),
        ]
    )
)


# Callback to update the text with latest data
@app.callback(
    Output("live-update-text", "children"),
    Input("interval-component", "n_intervals")
)
def update_metrics(n):
    style = {"padding": "5px", "fontSize": "16px"}
    time, temp, humi = [None] * 3
    if os.path.isfile(db_file):
        conn = sf.create_connection(db_file)
        with conn:
            rows = sf.get_latestdata(conn, n=1)
            if len(rows) > 0:
                time, temp, humi = rows[0]
    return [
        html.Span(
            f'Time: {dt.fromtimestamp(time) if time is not None else "No data"}',
            style=style,
        ),
        html.Span(
            f'Temperature: {f"{temp:.2f}" if temp is not None else "No data"}',
            style=style,
        ),
        html.Span(
            f'Humidity: {f"{humi:.2f}" if humi is not None else "No data"}',
            style=style
        ),
    ]


# Callback to update the graphs
@app.callback(
    Output("live-update-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_graph_live(n):
    data = {"time": [], "temperature": [], "humidity": []}

    if os.path.isfile(db_file):
        n_data = 20  # maximum number of data points to be plotted
        conn = sf.create_connection(db_file)
        with conn:
            rows = sf.get_latestdata(conn, n_data)
            if rows:  # if rows is not empty
                data["time"] = [dt.fromtimestamp(row[0]) for row in rows]
                data["temperature"] = [row[1] for row in rows]
                data["humidity"] = [row[2] for row in rows]

                if len(rows) < n_data:
                    for i in range(n_data - len(rows)):
                        data["time"].append(data["time"][-1] + td(seconds=10 * (i + 1)))
                        data["temperature"] += [None]
                        data["humidity"] += [None]

    fig = plotly.subplots.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig["layout"]["margin"] = {"l": 30, "r": 10, "b": 30, "t": 10}
    fig["layout"]["legend"] = {"x": 1, "y": 0, "xanchor": "left"}

    fig.append_trace(
        {
            "x": data["time"],
            "y": data["temperature"],
            "name": "Temperature",
            "mode": "lines+markers",
            "type": "scatter",
        },
        1,
        1,
    )

    fig.append_trace(
        {
            "x": data["time"],
            "y": data["humidity"],
            "name": "Humidity",
            "mode": "lines+markers",
            "type": "scatter",
        },
        2,
        1,
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
