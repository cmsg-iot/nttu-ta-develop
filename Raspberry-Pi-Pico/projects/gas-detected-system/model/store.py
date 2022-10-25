import random
# import sys
# sys.path.append("./parser")
# sys.path.append("./protocol")
# from machine import UART,ADC,Pin
# import utime

# GPIO
PIN_WEIGHT=[2,3]
PIN_HALL=10
PIN_BUZZER=11
PIN_HEATER=12
PIN_VALVE=13
PIN_MQ2=14
PIN_MQ7=15

# ADC
PRESSURE_1=26
PRESSURE_2=27

# I2C
AM2320=[4,5]

# UART
BEExANT=None

def getMQ2(pin):
    return Pin(pin)

global __state
__state = {
    'sensor':{
        'p1':0.0,
        'p2':0.0,
        'temp':0.0,
        'weight':0.0,
        'co':0,
        'gas':0,
        'hall':0
    },
    'device':{
        'buzzer':0,
        'heater':0,
        'valve':0,
        'uart':None
    }
}

def init():
    global __state
    __state = {
        'sensor':{
            'p1':0.0,
            'p2':0.0,
            'temp':0.0,
            'weight':0.0,
            'co':0,
            'gas':0,
            'hall':0
        },
        'device':{
            'buzzer':0,
            'heater':0,
            'valve':0,
            'uart':None
        }
    }


def readRandomData():
    global __state
    __state = {
        'sensor':{
            'p1':random.uniform(0.0,8.0),
            'p2':random.uniform(0.0,8.0),
            'temp':random.uniform(25.0,35.0),
            'weight':random.uniform(30.0,40.0),
            'co':random.randint(0,1024),
            'gas':random.randint(0,1024),
            'hall':0
        },
        'device':{
            'buzzer':0,
            'heater':0,
            'valve':0,
            'uart':None
        }
    }

def readRawData():

    global __state
    __state = {
        'sensor':{
            'p1':random.uniform(0.0,8.0),
            'p2':random.uniform(0.0,8.0),
            'temp':random.uniform(25.0,35.0),
            'weight':random.uniform(30.0,40.0),
            'co':random.randint(0,1024),
            'gas':random.randint(0,1024),
            'hall':0
        },
        'device':{
            'buzzer':0,
            'heater':0,
            'valve':0
        }
    }

