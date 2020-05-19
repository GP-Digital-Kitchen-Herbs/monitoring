import json
import sys


def get_value(param):
    try:
        return get_config()[param]
    except KeyError as e:
        print('Error: Add the following key-value-pair:' + param)
        print(e)
        sys.exit()


def get_config():
    try:
        with open('conf.json') as conf_json:
            data = json.load(conf_json)
            return data
    except IOError as e:
        print('Error: Create a file "conf.json" on the root of this folder.')
        print(e)
        sys.exit()
