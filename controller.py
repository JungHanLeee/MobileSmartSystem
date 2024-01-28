import sys
import io
import time
import picamera
from PIL import Image, ImageFilter
import paho.mqtt.client as mqtt
import gpio

isPicamera = False                                                      #
isStarted = False                                                       #
isDistance = False                                                      #

def onConnect(client, userdata, flag, rc):
        print("Connect with result code:"+ str(rc))
        client.subscribe("command", qos = 0)    # command
        pass

def onMessage(client, userdata, msg):
        global isStarted
        global isDistance

        command = str(msg.payload.decode("utf-8"))

        if(command == 'distance'):
                # ON/OFF
                isStarted=True if isStarted == False else False
                isDistance = True if isDistance == False else False
        pass

broker_address = "localhost"

client = mqtt.Client()
client.on_connect = onConnect
client.on_message = onMessage

client.connect(broker_address, 1883)
client.loop_start()

camera = picamera.PiCamera(framerate=60)

while(True):
        distance = gpio.measureDistance()
        b=True
        if(isDistance == True): #후진기어 설정
                stream = io.BytesIO()
                camera.capture(stream, format='jpeg', use_video_port = True)
                stream.seek(0)
                client.publish("mjpeg", stream.read(), qos=0)
                if(distance <=25.00):
                        gpio.ledOnOff(b)
                        time.sleep(0.15)
                        b= False if b== True else True
                        gpio.ledOnOff(b)
                        pass
                elif(distance >15.00):
                        gpio.ledOnOff(False)

client.loop_stop()
client.disconnect()
