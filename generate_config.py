import json

if __name__ == "__main__":

    config = {}
    print("Tool to generate the required config file.")
    print("Please enter your thingsboard access token:")

    temp = str(input())
    if temp:
        config["token"] = temp
    else:
        while not temp:
            print("The access token is required")
            temp = str(input())

        config["token"] = temp

    print("Please enter the interval between transmissions, the default is 60 (in seconds)")
    temp = str(input())

    if temp:
        config["sleep_in_seconds"] = int(temp)
    else:
        print("Using 60 seconds")
        config["sleep_in_seconds"] = 60


    print("Please enter light sensor port (leave empty to disable)")
    temp = str(input())
    
    if temp:
        config["sensor_light"] = int(temp)
    else:
        print("Light sensor disabled")

    print("Please enter moisture sensor port (leave empty to disable)")
    temp = str(input())
    
    if temp:
        config["sensor_moisture"] = int(temp)
    else:
        print("Moisture sensor disabled")

    print("Please enter temperature and humidity sensor port (leave empty to disable)")
    temp = str(input())
    if temp:
        config["sensor_temp_hum"] = int(temp)
    else:
        print("Temperature and humidity sensor disabled")

    print(config)

    with open('conf.json', 'w') as outfile:
        json.dump(config, outfile)