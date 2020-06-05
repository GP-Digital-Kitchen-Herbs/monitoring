import sys
import sensors.moisture as moisture
import sensors.light as light
import sensors.temp_humidity as temp_humidity
import sensors.ultrasonic as ultrasonic
import report.led as led
import report.display as display
import services.config as config
from datetime import datetime
import time

from services import telemetry

if __name__ == "__main__":

    current_config = config.get_config()
    sleep_time = current_config["sleep_in_seconds"]

    if "sensor_moisture" not in current_config and \
            "sensor_light" not in current_config and \
            "sensor_ultra_sonic" not in current_config and \
            "sensor_temp_hum" not in current_config and \
            "report_display" not in current_config:
        print('No sensor configurated in config.json. Run "generate_config.py" script.')
        sys.exit()

    while True:
        try:
            print(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

            data = {}

            if "sensor_moisture" in current_config:
                data.update(moisture.get_moisture(current_config))

            if "sensor_light" in current_config:
                data.update(light.get_light(current_config))

            if "sensor_temp_hum" in current_config:
                data.update(temp_humidity.get_temp_humidity(current_config))

            if "sensor_ultra_sonic" in current_config:
                ultrasonic.send_distance(current_config)

            if "report_display" in current_config:
                display.lightUp(current_config)

            telemetry.send_telemetry(data)

            print('-------')
            time.sleep(sleep_time)
        except IOError as ioe:
            print('Error:', ioe)
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            break
