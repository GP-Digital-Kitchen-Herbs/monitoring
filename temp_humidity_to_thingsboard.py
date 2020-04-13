import sys
import grovepi
import math
import requests
import time
import json

sensor = 8  # The port for the digital Sensor.
blue = 0    # The Blue colored sensor.

try:
    with open('thingsboard-access.json') as access_json:
        data = json.load(access_json)
        token = data['token']
except IOError:
    print('Error: Create a file "thingsboard-access.json" on the root of this folder.')
    sys.exit()
except KeyError:
    print('Error: Add the following key-value-pair: "token" : "[YOUR_ACCESS_TOKEN]"')
    sys.exit()

url = 'https://iot.jaykju.de/api/v1/' + token + '/telemetry'

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            data = {'temperature' : temp, "humidity" : humidity}
        res = requests.post(url, data = str(data))
        time.sleep(60)

    except IOError:
        print ("Error")
