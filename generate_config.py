import json
import yaml
import json
import sys
import argparse
from grovepi import *

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--change", nargs="+", help="change values in the config", required=False)
group.add_argument("-k", "--keep", nargs="+", help="keep values in the config", required=False)
parser.add_argument("-cu", "--calibrateultrasonic", action="store_true", help="calibrate the ultrasonic-ranger", required=False)
args = parser.parse_args()

def generate_config():
    config = {}
    print("Tool to generate the required config file.")

    with open('generate_config.yaml', 'r') as generator_config_yaml:
        generator_config = yaml.safe_load(generator_config_yaml)

    old_config = read_current_config()

    for key in generator_config.keys():
        if ((args.keep and key in args.keep) or (args.change and key not in args.change)) and key in old_config:
            config[key] = old_config[key]
            continue

        if (args.change and key not in args.change and key not in old_config):
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
    write_current_config(config)
    

def calibrate_ultrasonic():
    old_config = read_current_config()

    if old_config["sensor_ultra_sonic"]:
        print("Please position the ultra sonic sensor above the empty reservoir")
        print("Press enter to start")
        input()

        old_config["null_distance"] = ultrasonicRead(old_config["sensor_ultra_sonic"])
        write_current_config(old_config)
        print("Calibration successful:", old_config["null_distance"], "cm")
    else:
        print("Plase set the ultrasonic sensor port first")


def read_current_config():
    try:
        with open('conf.json') as conf_json:
            return json.load(conf_json)
    except:
        return "{}"

def write_current_config(config):
    with open('conf.json', 'w') as outfile:
        json.dump(config, outfile)

if __name__ == "__main__":
    if args.calibrateultrasonic:
        calibrate_ultrasonic()
    else:
        generate_config()