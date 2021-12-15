from random import randint
import paho.mqtt.client as mqtt
import timeit
from datetime import datetime
import json

#MQTT
mqttBroker = "192.168.43.57"
client = mqtt.Client("None Publisher")
client.connect(mqttBroker, 1884)

def pencatatan(i, waktu):
    f = open('publish_TanpaEnkripsi.csv', 'a')
    f.write("Message ke-" + i + ";" + str(mess) + ";" + waktu + "\n")

# Mencatat waktu mulai
start = timeit.default_timer()

message ={}
for i in range(100):
    mess = int('{:10}'.format(randint (60,100)))
    print("Plaintext\t: ", mess)
    now = str(datetime.now().timestamp())
    pencatatan(str(i), now)
    message['datetime'] = now
    stringify = json.dumps(message, indent=2)
    client.publish("NONE", stringify)
    print("Just published a message to topic NONE at "+ now)
    # sleep(1)

# Mencatat waktu selesai
stop = timeit.default_timer()
lama_enkripsi = stop - start
print("Waktu akumulasi : "+str(lama_enkripsi))