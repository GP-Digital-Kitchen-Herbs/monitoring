import grovepi
import math
import time
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
            print("Error")
            time.sleep(sleepTime)


def sendTempHumidity(currentConfig):
    sensor = currentConfig["sensor_temp_hum"]  # The port for the digital Sensor.
    sensorType = 0  # The Blue colored sensor. White is 1

    [temp, humidity] = grovepi.dht(sensor, sensorType)

    if math.isnan(temp) == False and math.isnan(humidity) == False:
        print('temp:', temp)
        print('humidity:', humidity)
        data = {'temperature': temp, "humidity": humidity}
        telemetry.sendTelemetry(data)
    else:
        print('Invalid temperature and humidity measurement')
