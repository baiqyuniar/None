import json
from time import sleep
import paho.mqtt.client as mqtt
from datetime import datetime

#MQTT
mqttBroker = "34.101.187.83"
client = mqtt.Client("None Subscriber")
client.connect(mqttBroker)

def pencatatan(dateSend, message):
	now = str(datetime.now().timestamp())
	f = open('subscribe_TanpaDekripsi.csv', 'a')
	f.write( message + ";" + now + ";" + dateSend + "\n")

if __name__ == "__main__":
    def on_message(client, userdata, message):
        raw = json.loads(message.payload.decode("utf-8"))
        dateSend = raw['datetime']
        message = raw['plaintext']
        print("Message\t: ", message)
        pencatatan(dateSend, message)
        
    client.loop_start()
    client.subscribe("NONE")
    client.on_message=on_message
    sleep(300)
    client.loop_stop
