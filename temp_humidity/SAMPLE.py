import math
import time
from datetime import datetime
import sys
sys.path.insert(0, "/home/moxdlab/digital-kitchen-herbs/tel_helper")
from tel_helper import sendTelemetry

sensor = 3

blue = 0

if __name__ == '__main__':
    dict = {
        "temperature": 40,
        "humidity": 50
    }

    sendTelemetry(dict)

