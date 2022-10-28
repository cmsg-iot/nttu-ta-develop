from modules.AM2320 import AM2320
from modules.GPIO import GPIO
from modules.HX711 import HX711
from modules.ADC import Adc
from modules.UART import Uart
import parser.configParser
from machine import Pin,UART
import uasyncio as asyncio
from utime import sleep_ms
import json
import os
from controller.commandHandler import CommandHandler

allow_cmd_list = [
    "set pressure_in shift",
    "set pressure_in radial",
    "set pressure_out shift",
    "set pressure_out radial",
    "set mq2 shift",
    "set mq2 radial",
    "set mq7 shift",
    "set mq7 radial",
    "set hx711 ch",
    "set hx711 shift",
    "set hx711 radial",
    "set buzzer on",
    "set buzzer off",
    "set heater on",
    "set heater off",
    "set valveOpen on",
    "set valveOpen off",
    "set valveClose on",
    "set valveClose off",
    "log on",
    "log off",
    "help"
]

configPath = "/config/config.json"
configTargets = ["pressure_in","pressure_out","mq2","mq2_2","mq7","hx711"]

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
commandHandler = CommandHandler(allow_cmd_list=allow_cmd_list)

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
    Pin(25,Pin.OUT).value(1)
    message = "excuted: " + cmd
    setMessage(message)
    logMessage(message)
    cmd_list = getSeperatedCommandList(cmd)
    dispatchAction(cmd_list)
    sleep_ms(10)
    Pin(25,Pin.OUT).value(0)
    writeTargetsParamToFile(configPath,configTargets)

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
    elif cmd_list[0] == "log":
        setLog(cmd_list[1])
    else:
        setMessage("Not vaild method")

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
        setMessage("Not vaild target")

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

def writeTargetsParamToFile(path,targets):
    jsonString = formatTartgetsParamToJson(targets)
    writeJsonToFile(path,jsonString)

def formatTartgetsParamToJson(targets):
    j = {}
    for i in targets:
        j[i] = {}
        if i == "hx711":
            j[i]['ch'] = getTargetObject(i).channel
        j[i]['shift'] = getTargetObject(i).shift
        j[i]['radial'] = getTargetObject(i).radial
    return json.dumps(j)

def writeJsonToFile(path,jsonString):
    f = open(path,'w')
    f.write(jsonString)
    f.close()
    logMessage("Write json to: " + path)

def setLog(flag):
    global __state
    if flag == "on":
        __state['log'] = True
    else:
        __state['log'] = False

def logMessage(message):
    if __state['log']:
        print(message)

def setMessage(message):
    global __state
    __state['message'] = message

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
    'config':{
        'pressure_in':{
            'shift':0,
            'radial':1.0
        },
        'pressure_out':{
            'shift':0,
            'radial':1.0
        },
        'mq2':{
            'shift':0,
            'radial':1.0
        },
        'mq2_2':{
            'shift':0,
            'radial':1.0
        },
        'mq7':{
            'shift':0,
            'radial':1.0
        },
        'hx711':{
            'ch':0,
            'shift':0,
            'radial':1.0
        }
    },
    'uart':None,
    'message':"",
    'log':False
}


initialDeviceStateWithConfigFile(parser.configParser.__deviceConfig)

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

        __state['config']['shift'] = mq2_2.shift
        await asyncio.sleep_ms(5)

        __state['config']['radial'] = mq2_2.radial
        await asyncio.sleep_ms(5)

        __state['config']['shift'] = mq7.shift
        await asyncio.sleep_ms(5)

        __state['config']['radial'] = mq7.radial
        await asyncio.sleep_ms(5)

        __state['config']['shift'] = hx711.shift
        await asyncio.sleep_ms(5)

        __state['config']['radial'] = hx711.radial
        await asyncio.sleep_ms(5)

        __state['config']['ch'] = hx711.channel
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

async def receiver():
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.readline()

async def readUART():
    global __state
    sreader = asyncio.StreamReader(uart, {})
    while True:
        cmd = await sreader.readline()
        
        if cmd != None and cmd != b'' :
            cmd = commandHandler.formatCommand(cmd)
            if commandHandler.checkCommandInAllowedList(cmd):
                if cmd == "help":
                    l = {'allow_cmd_list': allow_cmd_list}
                    l = json.dumps(l)
                    print(l)
                    uart.write(l)
                commandHandler.addCommandToQueue(cmd)

        commandHandler.executeCommandFromQueue()
        logMessage(cmd)
        cmd = None
        await sreader.drain()
        await asyncio.sleep_ms(250)

def getFileListOfPath(rootPath):
    file_list = []
    for i in os.listdir(rootPath):
        file_list.append(rootPath + "/" + i)
    return file_list

async def executeRules(path_list):
    print(path_list)
    while True:
        for i in path_list:
            f = open(i,'r')
            exec(f.read())
            f.close()
            await asyncio.sleep_ms(50)
        await asyncio.sleep(1)

async def main():
    path_list = getFileListOfPath('/rules')
    asyncio.create_task(readData())
    asyncio.create_task(readUART())
    #asyncio.create_task(executeRules(path_list))
    
    while True:
        await asyncio.sleep(1)

def start():
    try:
        asyncio.run(main())
    except OSError:
        print("error")
    finally:
        asyncio.new_event_loop()
        print('as_demos.auart.test() to run again.')

start()

