import json

def getValue(param):
    try:
        with open('../conf_helper/conf.json') as conf_json:
            data = json.load(conf_json)
            return data[param]
    except IOError as e:
        print('Error: Create a file "thingsboard-access.json" on the root of this folder.')
        print(e)
        sys.exit()
    except KeyError:
        print('Error: Add the following key-value-pair: "token" : "[YOUR_ACCESS_TOKEN]"')
        sys.exit()