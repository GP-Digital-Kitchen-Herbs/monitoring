import json
import sys

def getValue(param):
    try:
        return getConfig()[param]
    except KeyError as e:
        print('Error: Add the following key-value-pair:' + param)
        print(e)
        sys.exit()


def getConfig():
    try:
        with open('conf.json') as conf_json:
            data = json.load(conf_json)
            return data
    except IOError as e:
        print('Error: Create a file "conf.json" on the root of this folder.')
        print(e)
        sys.exit()