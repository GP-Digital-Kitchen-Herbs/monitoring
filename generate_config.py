import json
import yaml
import json
import sys
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--change", nargs="+", help="change values in the config", required=False)
group.add_argument("-k", "--keep", nargs="+", help="keep values in the config", required=False)
args = parser.parse_args()

if __name__ == "__main__":
    config = {}
    print("Tool to generate the required config file.")

    with open('generate_config.yaml', 'r') as generator_config_yaml:
        generator_config = yaml.safe_load(generator_config_yaml)

    try:
        with open('conf.json') as conf_json:
            old_config = json.load(conf_json)
    except:
        old_config = "{}"

    for key in generator_config.keys():
        if ((args.keep and key in args.keep) or (args.change and key not in args.change)) and key in old_config:
            config[key] = old_config[key]
            continue

        type = generator_config.get(key).get("type")
        temp = None

        if not generator_config.get(key).get("optional"):
            while not temp:
                print()
                print(generator_config.get(key).get("description"), "(required)")
                temp = str(input())

        else:
            print()
            print(generator_config.get(key).get("description"), "(optional, leave empty to disable)")
            temp = str(input())

        if temp:
            if type == "Number":
                temp = int(temp)
            config[key] = temp
            print("Value: ", temp)
        else:
            print("disabled")

    print(config)
    with open('conf.json', 'w') as outfile:
        json.dump(config, outfile)