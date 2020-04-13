import grovepi
import math
import time
import csv
from datetime import datetime

sensor = 7  # The port for the digital Sensor.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.

filename = 'data/data-' + datetime.now().strftime('%d-%m-%Y_%H-%M') + '.csv'

f = open(filename, 'w')

with f:

    writer = csv.writer(f)
    writer.writerow(['Date', 'Time', 'Temperature', 'Humidity'])

    while True:
        try:
            [temp,humidity] = grovepi.dht(sensor,blue)
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                current_date = datetime.now().strftime("%d.%m.%Y")
                current_time = datetime.now().strftime("%H:%M")
                writer.writerow([current_date, current_time, temp, humidity])
                f.flush()

	    time.sleep(60)

        except IOError:
            print ("Error")
