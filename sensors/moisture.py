import time
import grovepi
import services.telemetry as telemetry


def monitor_moisture(current_config):
    sleep_time = current_config["sleep_in_seconds"]

    while True:
        try:
            send_moisture(current_config)

            time.sleep(sleep_time)

        except KeyboardInterrupt:
            break
        except IOError:
            print("Error")
            time.sleep(sleep_time)


def send_moisture(current_config):
    telemetry.send_telemetry(get_moisture(current_config))


def get_moisture(current_config):
    sensor = current_config["sensor_moisture"]
    sensor_value = grovepi.analogRead(sensor)
    print('moisture:', sensor_value)
    return {'moisture': sensor_value}
