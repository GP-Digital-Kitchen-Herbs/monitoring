import requests
import time
import sys
import json
import smbus
import RPi.GPIO as GPIO
from grovepi import *

DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

def lightUp(current_config):
    rev = GPIO.RPI_REVISION
    global bus
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)

    DISPLAY_RGB_ADDR = 0x62
    DISPLAY_TEXT_ADDR = 0x3e

    try:
        url = 'https://iot.jaykju.de/api/v1/' + current_config["token"] + '/attributes'
        data = requests.get(url).json()
        filtered_data = dict(filter(lambda entry: entry[1] == True, data["shared"].items()))
        if len(filtered_data) == 0:
            setText(":)")
            setRGB(0, 255, 0)
        elif len(filtered_data) == 1:
            setText(" ".join(filtered_data.keys()).replace("Critical", ""))
            setRGB(255, 255, 0),
        else:
            setText(" ".join(filtered_data.keys()).replace("Critical", ""))
            setRGB(255, 0, 0)
        
    except BaseException as e:
        print('An exception occurred: {}'.format(e))


def setRGB(r,g,b):
    bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

def setText(text):
    textCommand(0x01) # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0

    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue

        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)