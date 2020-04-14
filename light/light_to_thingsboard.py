import time
import grovepi
import sys
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/tel_helper")
from tel_helper import sendTelemetry
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/conf_helper")
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
