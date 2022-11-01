from modules.AM2320 import AM2320
from modules.GPIO import GPIO
from modules.HX711 import HX711
from modules.ADC import Adc
from machine import Pin,UART
import uasyncio as asyncio
from utime import sleep_ms
import json
from utility.commandList import getSeperatedCommandList
from utility.configParser import getConfigFromPath
from utility.file import updateFileWithState
from utility.common import logMessage
import state

configPath = "/config/config.json"
#configTargets = ["pressure_in","pressure_out","mq2","mq2_2","mq7","hx711"]

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
uart=UART(0, baudrate=115200, parity=None, stop=1, bits=8)

global __state
__state = state.state

def excuteCommand(cmd):
    global __state
    Pin(25,Pin.OUT).value(1)
    message = "Excuted: " + cmd
    setMessage(message)
    logMessage(message,__state['log'])
    cmd_list = getSeperatedCommandList(cmd)
    dispatchAction(cmd_list)
    sleep_ms(50)
    Pin(25,Pin.OUT).value(0)
    updateFileWithState(configPath,__state)

def dispatchAction(cmd_list):
    if cmd_list[0] == "set" and cmd_list[3] != None:
        setTargetWithValue(cmd_list[1],cmd_list[2],cmd_list[3])
    elif cmd_list[0] == "set" and cmd_list[3] == None:
        setTarget(cmd_list[1],cmd_list[2])
    elif cmd_list[0] == "log":
        setLog(cmd_list[1])
    else:
        setMessage("Not vaild method: " + cmd_list[0])

def setTargetWithValue(target,act,value):
    global __state
    if act == "on":
        getTargetObject(target).openWithTime(value)
    elif act == "shift":
        getTargetObject(target).setShift(value)
    elif act == "radial":
        getTargetObject(target).setRadial(value)
    elif act == "ch":
        getTargetObject(target).setChannel(value)
    else:
        setMessage("Not vaild target")
    
    if act != "on":
        __state['isConfigUpdate'] = True

def setTarget(target,act):
    if act == "on":
        getTargetObject(target).setValue(1)
    elif act == "off":
        getTargetObject(target).setValue(0)
    elif act == "zero":
        getTargetObject(target).setShiftZero()
    else:
        setMessage("Missing 1 required argument")

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

initialDeviceStateWithConfigFile(getConfigFromPath("/config/config.json"))

def setLog(flag):
    global __state
    if flag == "on":
        __state['log'] = True
    else:
        __state['log'] = False

def setMessage(message):
    global __state
    __state['message'] = message

async def readData():
    global __state
    swriter = asyncio.StreamWriter(uart, {})
    while True:
        
        # DATA
        __state['data']['pressure_in'] = pressure_in.getValue()
        await asyncio.sleep_ms(5)
        
        __state['data']['pressure_out'] = pressure_out.getValue()
        await asyncio.sleep_ms(5)

        am2320Data = am2320.getMeasureData()
        if am2320Data != None:
            __state['data']['temp'] = am2320Data['temp']
            __state['data']['hum'] = am2320Data['hum']
        await asyncio.sleep_ms(5)
    
        __state['data']['hx711'] = hx711.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['mq2'] = mq2.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['mq2_2'] = mq2_2.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['mq7'] = mq7.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['hall'] = hall.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['buzzer'] = buzzer.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['heater'] = heater.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['valveOpen'] =valveOpen.getValue()
        await asyncio.sleep_ms(5)

        __state['data']['valveClose'] =valveClose.getValue()
        await asyncio.sleep_ms(5)

        # Config
        __state['config']['pressure_in']['shift'] = pressure_in.shift
        await asyncio.sleep_ms(5)

        __state['config']['pressure_in']['radial'] = pressure_in.radial
        await asyncio.sleep_ms(5)
        
        __state['config']['pressure_out']['shift'] = pressure_out.shift
        await asyncio.sleep_ms(5)

        __state['config']['pressure_out']['radial'] = pressure_out.radial
        await asyncio.sleep_ms(5)

        __state['config']['mq2']['shift'] = mq2.shift
        await asyncio.sleep_ms(5)

        __state['config']['mq2']['radial'] = mq2.radial
        await asyncio.sleep_ms(5)

        __state['config']['mq2_2']['shift'] = mq2_2.shift
        await asyncio.sleep_ms(5)

        __state['config']['mq2_2']['radial'] = mq2_2.radial
        await asyncio.sleep_ms(5)

        __state['config']['mq7']['shift'] = mq7.shift
        await asyncio.sleep_ms(5)

        __state['config']['mq7']['radial'] = mq7.radial
        await asyncio.sleep_ms(5)

        __state['config']['hx711']['shift'] = hx711.shift
        await asyncio.sleep_ms(5)

        __state['config']['hx711']['radial'] = hx711.radial
        await asyncio.sleep_ms(5)

        __state['config']['hx711']['ch'] = hx711.channel
        await asyncio.sleep_ms(5)
        
        newData = {}
        data = {'data':__state['data']}
        config = {'config':__state['config']}
        message = {'message':__state['message']}
        newData.update(data)
        newData.update(config)
        newData.update(message)
        j = json.dumps(newData)

        # clear message
        if len(__state['message']) > 0:
            __state['message'] = ""
        swriter.write(str(j))
        await swriter.drain()
        await asyncio.sleep(1)

async def readUART():
    global __state
    sreader = asyncio.StreamReader(uart, {})
    while True:
        cmd = await sreader.readline()
        __state['uart'] = cmd
        logMessage(cmd,__state['log'])
        cmd = ""
        await sreader.drain()
        await asyncio.sleep_ms(250)

async def executeRules(path_list):
    while True:
        for i in path_list:
            f = open(i,'r')
            exec(f.read())
            f.close()
            await asyncio.sleep_ms(50)
        await asyncio.sleep(1)
