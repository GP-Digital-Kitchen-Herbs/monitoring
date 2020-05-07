import services.telemetry as telemetry
from datetime import datetime
from grovepi import *
from statistics import median

# 10 seconds would probably also work, but just in case 15 to not brick the sensor / board
INTERVAL = 15
# Number of measurements
MEASUREMENT_COUNT = 3

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
        sensor_values = []
        for i in range(MEASUREMENT_COUNT):
            sensor_values.append(int(currentConfig["null_distance"]) - ultrasonicRead(sensor))
            time.sleep(INTERVAL)
        sensor_value = median(sensor_values)
        print('water:', sensor_value, 'cm')
        data = {'water' : sensor_value}
        telemetry.sendTelemetry(data)
    else:
        print("Please calibrate the Ultrasonic-Ranger")
    

