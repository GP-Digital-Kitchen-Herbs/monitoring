import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "../tel_helper"))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "../conf_helper"))
from tel_helper import sendTelemetry
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