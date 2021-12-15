import json
from time import sleep
import paho.mqtt.client as mqtt
from datetime import datetime

#MQTT
mqttBroker = "192.168.43.57"
client = mqtt.Client("None Subscriber")
client.connect(mqttBroker, 1884)

def pencatatan(dateSend):
	now = str(datetime.now().timestamp())
	f = open('subscribe_TanpaDekripsi.csv', 'a')
	f.write( now + ";" + dateSend + "\n")

if __name__ == "__main__":
    def on_message(client, userdata, message):
        raw = json.loads(message.payload.decode("utf-8"))
        dateSend = raw['datetime']
        pencatatan(dateSend)
        
    client.loop_start()
    client.subscribe("NONE")
    client.on_message=on_message
    sleep(300)
    client.loop_stop
