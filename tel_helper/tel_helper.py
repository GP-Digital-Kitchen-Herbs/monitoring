import json
import requests
import sys

url = ''
loaded = False

def loadUrl():
    try:
        with open('..\\tel_helper\\thingsboard-access.json') as access_json:
            data = json.load(access_json)
            token = data['token']
    except IOError as e:
        print('Error: Create a file "thingsboard-access.json" on the root of this folder.')
        print(e)
        sys.exit()
    except KeyError:
        print('Error: Add the following key-value-pair: "token" : "[YOUR_ACCESS_TOKEN]"')
        sys.exit()

    global url
    url = 'https://iot.jaykju.de/api/v1/' + token + '/telemetry'
    global loaded
    loaded = True


def sendTelemetry(values):
    if loaded == False:
        loadUrl()
    requests.post(url=url, data=str(values))