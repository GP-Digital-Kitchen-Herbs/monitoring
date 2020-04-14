import sys
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/tel_helper")
from tel_helper import sendTelemetry
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/conf_helper")
from conf_helper import getValue
from datetime import datetime
from grovepi import *

sensor = getValue("sensor_ultra_sonic")
sleep_time = getValue("sleep_in_seconds")

while True:
    try:
        value = ultrasonicRead(sensor)
        print(str(datetime.now()) + ": " + str(value))
        dict = {
            "Distance": value
        }
        sendTelemetry(dict)
        time.sleep(sleep_time)
    except TypeError:
        print("TE, Error")
    except IOError:
        print("IO, Error")