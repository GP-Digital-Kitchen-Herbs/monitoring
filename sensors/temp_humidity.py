import grovepi
import math
import time
import services.telemetry as telemetry


def monitor_temp_humidity(current_config):
    sleep_time = current_config["sleep_in_seconds"]

    while True:
        try:
            send_temp_humidity(current_config)
            time.sleep(sleep_time)

        except KeyboardInterrupt:
            break
        except IOError:
            print("Error")
            time.sleep(sleep_time)


def send_temp_humidity(current_config):
    data = get_temp_humidity(current_config)
    if (data):
        telemetry.send_telemetry(data)


def get_temp_humidity(current_config):
    sensor = current_config["sensor_temp_hum"]  # The port for the digital Sensor.
    sensor_type = 0  # The Blue colored sensor. White is 1

    [temp, humidity] = grovepi.dht(sensor, sensor_type)

    if math.isnan(temp) is False and math.isnan(humidity) is False:
        print('temp:', temp)
        print('humidity:', humidity)
        return {'temperature': temp, "humidity": humidity}
    else:
        print('Invalid temperature and humidity measurement')
        return None
