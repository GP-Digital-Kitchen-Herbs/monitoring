import time
import grovepi
import services.telemetry as telemetry


def monitor_light(current_config):
    sleep_time = current_config["sleep_in_seconds"]

    while True:
        try:
            send_light(current_config)

            time.sleep(sleep_time)
        except KeyboardInterrupt:
            break
        except IOError:
            print("Error")
            time.sleep(sleep_time)


def send_light(current_config):
    telemetry.send_telemetry(get_light(current_config))


def get_light(current_config):
    sensor = current_config["sensor_light"]
    grovepi.pinMode(sensor, "INPUT")
    sensor_value = grovepi.analogRead(sensor)
    print('light:', sensor_value)
    return {'light': sensor_value}
