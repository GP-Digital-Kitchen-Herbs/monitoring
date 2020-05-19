import requests
import sys
import services.config as config

url = ''
loaded = False


def load_url():
    try:
        token = config.get_value('token')
    except IOError as e:
        print('Error: Create the file "conf.json" on the project-root and add the field "token".')
        print(e)
        sys.exit()

    global url
    url = 'https://iot.jaykju.de/api/v1/' + token + '/telemetry'
    global loaded
    loaded = True


def send_telemetry(values):
    if loaded is False:
        load_url()
    requests.post(url=url, data=str(values))
