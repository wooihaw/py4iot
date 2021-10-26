from time import sleep
from random import gauss
from uuid import uuid1, getnode
from json import dumps
import paho.mqtt.client as mqtt


def on_publish(client, userdata, result):  # callback function for publish
    print(f"Data published: {d}")


broker = "test.mosquitto.org"
port = 1883

# Make sure that the topic is unique for your machine
machineID = hex(getnode())[-7:]  # last 7 hex digits of MAC address
topic = machineID + "/sensor1"

client1 = mqtt.Client(str(uuid1()))  # create client object
client1.on_publish = on_publish  # assign callback function
client1.connect(broker, port)  # establish connection

while True:
    temp = f"{gauss(28, 2):.2f}"
    humi = f"{gauss(84, 5):.2f}"
    d = dict(temperature=temp, humidity=humi)
    ret = client1.publish(topic, dumps(d))  # publish
    sleep(5)
