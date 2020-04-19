import time
import grovepi
import services.telemetry as telemetry

def monitorMoisture (currentConfig):

    sleepTime = currentConfig["sleep_in_seconds"]

    while True:
        try:
            sendMoisture(currentConfig)

            time.sleep(sleepTime)

        except KeyboardInterrupt:
            break
        except IOError:
            print ("Error")
            time.sleep(sleepTime)

def sendMoisture(currentConfig):
    sensor = currentConfig["sensor_moisture"]
    sensor_value = grovepi.analogRead(sensor)
    print('moisture:', sensor_value)
    data = {'moisture' : sensor_value}
    telemetry.sendTelemetry(data)
