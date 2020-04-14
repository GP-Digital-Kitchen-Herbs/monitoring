import sys
import grovepi
import math
import requests
import time
import sys
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/tel_helper")
from tel_helper import sendTelemetry
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/conf_helper")
from conf_helper import getValue
from datetime import datetime

sensor = getValue("sensor_temp_hum")  # The port for the digital Sensor.
sleep_time = getValue("sleep_in_seconds")
blue = 0    # The Blue colored sensor.

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            data = {'temperature' : temp, "humidity" : humidity}
            sendTelemetry(data)
            print(str(datetime.now()) + ": " + str(data))
        time.sleep(sleep_time)

    except IOError:
        print ("Error")

