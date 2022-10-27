from modules.AM2320 import AM2320
from modules.GPIO import GPIO
from modules.HX711 import HX711
from modules.ADC import Adc
from modules.UART import Uart
import parser.configParser
from utime import sleep_ms
import json

am2320 = AM2320(i2cNum=0,scl=17,sda=16,freq=100000)
hx711 = HX711(d_out=4,pd_sck=5)
hall = GPIO(pin=10,mode=0)
buzzer = GPIO(pin=11,mode=1)
heater = GPIO(pin=12,mode=1)
valveOpen = GPIO(pin=13,mode=1)
valveClose = GPIO(pin=14,mode=1)
mq7 = Adc(channel=0)
mq2 = Adc(channel=1)
mq2_2 = Adc(channel=2)
pressure_in = Adc(channel=3)
pressure_out = Adc(channel=4)
uart=Uart(uartNum=0,baud=115200,rxPin=1,txPin=0)
uart.init()

def initialDeviceStateWithConfigFile(state):
    for target in state:
        t = getTargetObject(target)
        for param in state[target]:
            v = state[target][param]
            if param == "shift":
                t.setShift(v)
            elif param == "radial":
                t.setRadial(v)
            elif param == "ch":
                t.setChannel(v)

def excuteCommand(cmd):
    cmd_list = getSeperatedCommandList(cmd)
    dispatchAction(cmd_list)

def getSeperatedCommandList(cmd):
    cmd_list = separateCommandWithSpace(cmd)
    cmd_list = formatCommandList(cmd_list)
    return cmd_list

def separateCommandWithSpace(cmd):
    return cmd.split()

def formatCommandList(cmd_list):
    new_list = ["","","",None]
    for idx,v in enumerate(cmd_list):
        new_list[idx] = v
    return new_list

def dispatchAction(cmd_list):
    if cmd_list[0] == "set" and cmd_list[3] != None:
        setTargetWithValue(cmd_list[1],cmd_list[2],cmd_list[3])
    elif cmd_list[0] == "set" and cmd_list[3] == None:
        setTarget(cmd_list[1],cmd_list[2])
    elif cmd_list[0] == "reset":
        resetTarget(cmd_list[1],cmd_list[2])
    else:
        setMessage("not vaild method")

def setTargetWithValue(target,act,value):
    if act == "on":
        getTargetObject(target).openWithTime(value)
    elif act == "shift":
        getTargetObject(target).setShift(value)
    elif act == "radial":
        getTargetObject(target).setRadial(value)
    elif act == "ch":
        getTargetObject(target).setChannel(value)
    else:
        setMessage("not vaild target")

def setTarget(target,act):
    if act == "on":
        getTargetObject(target).setValue(1)
    elif act == "off":
        getTargetObject(target).setValue(0)
    elif act == "zero":
        getTargetObject(target).setShiftZero()
    else:
        setMessage("missing 1 required argument")
    

def resetTarget(target,act):
    if act =="zero":
        getTargetObject(target).resetShiftZero()
    else:
        setMessage("not vaild target")

def getTargetObject(target=""):
    if target == "pressure_in":
        return pressure_in
    elif target == "pressure_out":
        return pressure_out
    elif target == "mq2":
        return mq2
    elif target == "mq2_2":
        return mq2_2
    elif target == "mq7":
        return mq7
    elif target == "hx711":
        return hx711
    elif target == "buzzer":
        return buzzer
    elif target == "heater":
        return heater
    elif target == "valveOpen":
        return valveOpen
    elif target == "valveClose":
        return valveClose
    else:
        return None

global __state
__state = {
    'data':{
        'pressure_in':0.0,
        'pressure_out':0.0,
        'temp':0.0,
        'hum':0.0,
        'hx711':0.0,
        'mq2':0,
        'mq2_2':0,
        'mq7':0,
        'hall':0,
        'buzzer':0,
        'heater':0,
        'valveOpen':0,
        'valveClose':0
    },
    'uart':None,
    'message':""
}

initialDeviceStateWithConfigFile(parser.configParser.__deviceConfig)

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
        'mq2_2':0,
        'mq7':0,
        'hall':0,
        'buzzer':0,
        'heater':0,
        'valveOpen':0,
        'valveClose':0
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

    __state['data']['mq2_2'] = mq2_2.getValue()
    sleep_ms(5)

    __state['data']['mq7'] = mq7.getValue()
    sleep_ms(5)

    __state['data']['hall'] = hall.getValue()
    sleep_ms(5)

    __state['data']['buzzer'] = buzzer.getValue()
    sleep_ms(5)

    __state['data']['heater'] = heater.getValue()
    sleep_ms(5)

    __state['data']['valveOpen'] =valveOpen.getValue()
    sleep_ms(5)

    __state['data']['valveClose'] =valveClose.getValue()
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