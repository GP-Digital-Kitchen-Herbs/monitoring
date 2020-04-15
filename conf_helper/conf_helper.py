import json
import sys

def getValue(param):
    try:
        with open('../conf_helper/conf.json') as conf_json:
            data = json.load(conf_json)
            return data[param]
    except IOError as e:
        print('Error: Create a file "conf.json" on the root of this folder.')
        print(e)
        sys.exit()
    except KeyError as e:
        print('Error: Add the following key-value-pair:' + param)
        print(e)
        sys.exit()