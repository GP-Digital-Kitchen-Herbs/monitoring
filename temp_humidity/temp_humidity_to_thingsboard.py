import sys
import grovepi
import math
import requests
import time
import sys
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/tel_helper")
from tel_helper import sendTelemetry

sensor = 8  # The port for the digital Sensor.
blue = 0    # The Blue colored sensor.

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            data = {'temperature' : temp, "humidity" : humidity}
            print(data)
        sendTelemetry(dict)
        time.sleep(60)

    except IOError:
        print ("Error")
