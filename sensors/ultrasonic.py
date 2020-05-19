import time
import services.telemetry as telemetry
from grovepi import *
from statistics import median

# 10 seconds would probably also work, but just in case 15 to not brick the sensor / board
INTERVAL = 15
# Number of measurements
MEASUREMENT_COUNT = 3


def monitor_distance(current_config):
    sleep_time = current_config("sleep_in_seconds")

    while True:
        try:
            send_distance(current_config)
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            break
        except IOError:
            print("IO, Error")


def send_distance(current_config):
    data = get_distance(current_config)
    if data:
        telemetry.send_telemetry(data)


def get_distance(current_config):
    sensor = current_config["sensor_ultra_sonic"]
    if current_config["null_distance"]:
        sensor_values = []
        for i in range(MEASUREMENT_COUNT):
            sensor_values.append(int(current_config["null_distance"]) - ultrasonicRead(sensor))
            time.sleep(INTERVAL)
        sensor_value = median(sensor_values)
        print('water:', sensor_value, 'cm')
        return {'water': sensor_value}
    else:
        print("Please calibrate the Ultrasonic-Ranger")
        return None
