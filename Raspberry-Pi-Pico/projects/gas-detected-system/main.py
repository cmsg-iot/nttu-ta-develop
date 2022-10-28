import sys
import utime
import json
sys.path.append("./model")
sys.path.append("./model/modules")
sys.path.append("./controller")
import model.store
from controller.commandHandler import CommandHandler
from machine import Pin
from utime import sleep

readUART_counter = 0
readDATA_counter = 0
# 允許的命令清單
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
    "set hx711 zero",
    "reset hx711 zero",
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

commandHandler = CommandHandler(allow_cmd_list=allow_cmd_list)

print("Strat!")
while True:
    readUART_counter+=1
    readDATA_counter+=1
    """

    # 命令接收&執行
    cmd = model.store.__state['uart']
    if cmd != None and cmd != b'' :
        
        # 清除 state 中的 uart buffer
        model.store.__state['uart'] = None
        
        cmd = commandHandler.formatCommand(cmd)
        
        if commandHandler.checkCommandInAllowedList(cmd):
            print(cmd)
            if cmd == "help":
                l = {'allow_cmd_list': allow_cmd_list}
                model.store.writeUART(str(json.dumps(l)))
            else:
                commandHandler.addCommandToQueue(cmd)

    commandHandler.executeCommandFromQueue()
    
    # 讀取 uart buffer
    if readUART_counter >= 90:
        readUART_counter = 0
        #model.store.readUART()
        if model.store.getAnyUART():
            model.store.writeUART("get data")
            model.store.readUART()

    # 讀取 data
    if readDATA_counter >= 100:
        readDATA_counter = 0
        model.store.readData()
    """
    utime.sleep_ms(10)

    if readDATA_counter >= 2:
        Pin(25,Pin.OUT).value(1)
    if readDATA_counter >= 11:
        Pin(25,Pin.OUT).value(0)


