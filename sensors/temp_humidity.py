import grovepi
import math
import requests
import time
from datetime import datetime
import services.telemetry as telemetry

def monitorTempHumidity(currentConfig):
    
    sleepTime = currentConfig["sleep_in_seconds"]
    
    while True:
        try:
            sendTempHumidity(currentConfig)
            time.sleep(sleepTime)

        except KeyboardInterrupt:
            break
        except IOError:
            print ("Error")
            time.sleep(sleepTime)

def sendTempHumidity(currentConfig):
    sensor = currentConfig["sensor_temp_hum"]  # The port for the digital Sensor.
    sensorType = 0    # The Blue colored sensor. White is 1 

    [temp,humidity] = grovepi.dht(sensor, sensorType)
    print('temp:', temp, '\nhumidity:', humidity)

    if math.isnan(temp) == False and math.isnan(humidity) == False:
        data = {'temperature' : temp, "humidity" : humidity}
        telemetry.sendTelemetry(data)
