#!/usr/bin/python3

import paho.mqtt.client as mqtt
#import paho.mqtt.publish as publish
import datetime

MQTT_HOST = '192.168.1.1'
store_path='store'


def store(topic, val):
    now = str(datetime.datetime.today())
    with open(store_path+'/'+now[:10]+'_'+topic+'.log', 'a') as f:
            f.write(now+' '+val+'\n')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = str(msg.topic).replace('/','_')
    val = str(msg.payload.decode())
    #print(topic+" "+val)
    store(topic,val)
    #publish.single("paho/test/single", payload=str(msg.payload), hostname=MQTT_HOST, retain=True)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, 1883, 60)
client.loop_forever()

