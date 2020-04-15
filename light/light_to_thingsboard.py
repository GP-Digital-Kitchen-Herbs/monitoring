import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "../tel_helper"))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "../conf_helper"))
import time
import grovepi
from tel_helper import sendTelemetry
from conf_helper import getValue

sensor = getValue("sensor_light")
grovepi.pinMode(sensor,"INPUT")

while True:
    try:
        sensor_value = grovepi.analogRead(sensor)
        
        data = {'light' : sensor_value}
        sendTelemetry(data)

        time.sleep(getValue("sleep_in_seconds_light"))

    except IOError:
        print ("Error")
