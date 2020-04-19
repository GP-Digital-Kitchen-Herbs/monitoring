import requests
import sys
import services.config as config

url = ''
loaded = False

def loadUrl():
    try:
        token = config.getValue('token')
    except IOError as e:
        print('Error: Create the file "conf.json" on the project-root and add the field "token".')
        print(e)
        sys.exit()

    global url
    url = 'https://iot.jaykju.de/api/v1/' + token + '/telemetry'
    global loaded
    loaded = True


def sendTelemetry(values):
    if loaded == False:
        loadUrl()
    requests.post(url=url, data=str(values))