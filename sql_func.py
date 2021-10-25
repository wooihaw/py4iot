import sqlite3


def create_connection(db_file):
    '''Create and return a connection to the database'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    '''Create the "datalog" table for a new sqlite database'''
    sql = """CREATE TABLE datalog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp INTEGER,
                    temperature real,
                    humidity real
            )"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def insert_data(conn, data):
    '''Insert data to the "datalog" table'''
    sql = """INSERT INTO datalog(timestamp, temperature, humidity)
                VALUES(?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


def get_latestdata(conn, n=10):
    '''Get and return the last n rows from the "datalog" table'''
    sql = """SELECT timestamp, temperature, humidity FROM datalog
                ORDER BY id DESC
                LIMIT ?"""
    cur = conn.cursor()
    cur.execute(sql, (n,))
    rows = cur.fetchall()
    return rows
