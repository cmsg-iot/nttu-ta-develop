from modules.AM2320 import AM2320
from modules.GPIO import GPIO
from modules.HX711 import HX711
from modules.ADC import Adc
from modules.UART import Uart
from utime import sleep_ms
import json

am2320 = AM2320(i2cNum=0,scl=17,sda=16,freq=100000)
hx711 = HX711(d_out=4,pd_sck=5)
hall = GPIO(pin=10,mode=0)
buzzer = GPIO(pin=11,mode=1)
heater = GPIO(pin=12,mode=1)
valve = GPIO(pin=13,mode=1)
mq7=Adc(channel=0)
mq2 = Adc(channel=1)
pressure_in = Adc(channel=2)
pressure_out = Adc(channel=3)
uart=Uart(uartNum=0,baud=115200,rxPin=1,txPin=0)
uart.init()

def setShift(sensor,value):
    if sensor == "pressure_in":
        pressure_in.setShift(value)

global __state
__state = {
    'data':{
        'pressure_in':0.0,
        'pressure_out':0.0,
        'temp':0.0,
        'hum':0.0,
        'hx711':0.0,
        'mq2':0,
        'mq7':0,
        'hall':0,
        'buzzer':0,
        'heater':0,
        'valve':0
    },
    'uart':None,
    'message':""
}

def init():
    global __state
    __state = {
    'data':{
        'pressure_in':0.0,
        'pressure_out':0.0,
        'temp':0.0,
        'hum':0.0,
        'hx711':0.0,
        'mq2':0,
        'mq7':0,
        'hall':0,
        'buzzer':0,
        'heater':0,
        'valve':0,
    },
    'uart':None,
    'message':""
}

def readData():
    global __state

    __state['data']['pressure_in'] = pressure_in.getValue()
    sleep_ms(5)

    __state['data']['pressure_out'] = pressure_out.getValue()
    sleep_ms(5)

    am2320Data = am2320.getMeasureData()
    if am2320Data != None:
        __state['data']['temp'] = am2320Data['temp']
        __state['data']['hum'] = am2320Data['hum']
    sleep_ms(5)
    
    __state['data']['hx711'] = hx711.getValue()
    sleep_ms(5)

    __state['data']['mq2'] = mq2.getValue()
    sleep_ms(5)

    __state['data']['mq7'] = mq7.getValue()
    sleep_ms(5)

    __state['data']['hall'] = hall.getValue()
    sleep_ms(5)

    __state['data']['buzzer'] = buzzer.getValue()
    sleep_ms(5)

    __state['data']['heater'] = heater.getValue()
    sleep_ms(5)

    __state['data']['valve'] =valve.getValue()
    sleep_ms(5)

    newData = dict(__state['data'])
    message = {'message':__state['message']}
    newData.update(message)
    j = json.dumps(newData)
    #print(j)
    uart.write(str(j))
    
    # clear message
    if len(__state['message']) > 0:
        __state['message'] = ""

def readUART():
    global __state
    __state['uart'] = uart.readline()

def setMessage(message):
    global __state
    __state['message'] = message