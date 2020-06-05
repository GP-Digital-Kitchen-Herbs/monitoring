import requests
import time
import json
from grovepi import *

def lightUp(current_config):
    try:
        led = current_config["report_led"]
        url = 'https://iot.jaykju.de/api/v1/' + current_config["token"] + '/attributes'
        pinMode(led, "OUTPUT")
        data = requests.get(url).json()
        filtered_data = dict(filter(lambda entry: entry[1] == True, data["shared"].items()))
        if len(filtered_data) > 0:
            digitalWrite(led, 1)
        else:
            digitalWrite(led, 0)
    except BaseException as e:
        print('An exception occurred: {}'.format(e))

def changeLedStatus(port, value, sleep_time):
    digitalWrite(port, value)
    time.sleep(sleep_time)