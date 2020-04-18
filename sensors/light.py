import time
import grovepi
import requests
import services.telemetry as telemetry

def monitorLight(currentConfig):

    sleepTime = currentConfig["sleep_in_seconds"]
    grovepi.pinMode(sensor,"INPUT")

    while True:
        try:
            sendLight(currentConfig)

            time.sleep(sleepTime)
        except KeyboardInterrupt:
                break
        except IOError:
            print ("Error")
            time.sleep(sleepTime)

def sendLight(currentConfig):
    sensor = currentConfig["sensor_light"]
    sensor_value = grovepi.analogRead(sensor)
    print('light:', sensor_value)

    data = {'light' : sensor_value}
    telemetry.sendTelemetry(data)
    
