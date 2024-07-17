import paho.mqtt.client as mqtt
from json import dumps
import os

MQTT_HOST = "mosquitto"
USER = '##########'
PASSWORD = '##########'
IP_BROKER = "##########"

i = 0
CUSTOMIZATION = []
while True:
    CUSTOMIZATION.append(os.environ.get("CUSTOMIZATION_"+str(i+1)))
    i = i+1
    if CUSTOMIZATION[-1] == None:
        del CUSTOMIZATION[-1]
        break
def warning():

    clienteMqtt = mqtt.Client()
    clienteMqtt.username_pw_set(USER, password=PASSWORD)
    clienteMqtt.connect(IP_BROKER, 31883)
    if CUSTOMIZATION[0].split("=")[-1] == "nurse":
        clienteMqtt.publish('NurseSystem/Warning', payload=dumps(CUSTOMIZATION[1].split("=")[-1]).encode('utf-8'))

if __name__ == '__main__':
    warning()