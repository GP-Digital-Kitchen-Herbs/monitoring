import time
import grovepi
import services.telemetry as telemetry

def monitorLight(currentConfig):

    sleepTime = currentConfig["sleep_in_seconds"]

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
    grovepi.pinMode(sensor, "INPUT")
    sensor_value = grovepi.analogRead(sensor)
    print('light:', sensor_value)

    data = {'light' : sensor_value}
    telemetry.sendTelemetry(data)
    
