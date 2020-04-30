import services.telemetry as telemetry
from datetime import datetime
from grovepi import *

def monitoreDistance(currentConfig):

    sleep_time = currentConfig("sleep_in_seconds")

    while True:
        try:
            sendDistance(currentConfig)
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            break
        except IOError:
            print("IO, Error")

def sendDistance(currentConfig):
    sensor = currentConfig["sensor_ultra_sonic"]
    if currentConfig["null_distance"]:
        sensor_value = int(currentConfig["null_distance"]) - ultrasonicRead(sensor)
        print('water:', sensor_value, 'cm')
        data = {'water' : sensor_value}
        telemetry.sendTelemetry(data)
    else:
        print("Please calibrate the Ultrasonic-Ranger")