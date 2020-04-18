import sys
import sensors.moisture as moisture
import sensors.light as light
import sensors.temp_humidity as temp_humidity
import services.config as config
from datetime import datetime
import time

if __name__ == "__main__":

    currentConfig = config.getConfig()
    sleepTime = currentConfig["sleep_in_seconds"]

    if not "sensor_moisture" in currentConfig and \
       not "sensor_light" in currentConfig and \
       not "sensor_temp_hum" in currentConfig:
        print('No sensor configurated in config.json. Run "generate_config.py" script.')
        sys.exit()

    while True:
        try:
            print(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

            if "sensor_moisture" in currentConfig:
                moisture.sendMoisture(currentConfig)

            if "sensor_light" in currentConfig:
                light.sendLight(currentConfig)

            if "sensor_temp_hum" in currentConfig:
                temp_humidity.sendTempHumidity(currentConfig)
                        
            print('-------')
            time.sleep(sleepTime)
        except IOError as ioe:
            print('Error:', ioe)
            time.sleep(sleepTime)
        except KeyboardInterrupt:
            break
