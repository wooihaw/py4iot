from uuid import uuid1, getnode
from json import loads
from datetime import datetime as dt
import os.path
import paho.mqtt.client as mqtt
import sql_func as sf


def on_connect(client, userdata, flag, rc):
    '''Callback function for connect'''
    print(f"Connected with result code: {str(rc)}")


def on_subscribe(client, userdata, mid, granted_qos):
    '''Callback function for subscribe'''
    print(f"Subscribed with QOS: {granted_qos}")


def on_message(client, userdata, msg):
    '''Callback function for message'''
    print(f"Message: {str(msg.payload)}")
    utcnow = dt.utcnow()
    timestamp = int(utcnow.timestamp())
    d = loads(msg.payload)
    data = [timestamp, d["temperature"], d["humidity"]]
    conn = sf.create_connection(db_file)
    with conn:
        id = sf.insert_data(conn, data)


broker = "test.mosquitto.org"
port = 1883

# Make sure that the topic is unique for your machine
machineID = hex(getnode())[-7:]  # last 7 hex digits of MAC address
topic = machineID + "/sensor1"

db_file = "mydata.db"
no_file = False if os.path.isfile(db_file) else True
conn = sf.create_connection(db_file)
with conn:
    if no_file:
        sf.create_table(conn)  # create table for new db file


client1 = mqtt.Client(str(uuid1()))  # create client object
client1.on_connect = on_connect  # assign callback function for connect
client1.on_subscribe = on_subscribe  # assign callback function for subscribe
client1.on_message = on_message  # assign callback function for message
client1.connect(broker, port)  # establish connection
client1.subscribe(topic, 0)  # subscribe to topic with QoS 0
client1.loop_forever()  # wait for message
