import os
import sys
import uasyncio as asyncio
sys.path.append("./model")
sys.path.append("./model/modules")
sys.path.append("./controller")
sys.path.append("./utility")
import model.store
import model.cmd
from utility.fileList import getFileListOfPath
from utility.file import updateFileWithState
from controller.commandHandler import CommandHandler
from machine import Pin

rule_list = getFileListOfPath('/rules',os.listdir('/rules'))
allow_cmd_list = model.cmd.allow_cmd_list

commandHandler = CommandHandler(allow_cmd_list)

async def main():
    
    asyncio.create_task(model.store.readData())
    asyncio.create_task(model.store.readUART())
    asyncio.create_task(handleCommand())
    asyncio.create_task(updateConfigFile())
    #asyncio.create_task(model.store.executeRules(rule_list))
    
    while True:
        await asyncio.sleep(1)
global previous_config
previous_config = {}
async def handleCommand():
    global previous_config
    while True:
        cmd = model.store.__state['uart']
        commandHandler.handleCommandExecuted(cmd)
        previous_config = model.store.__state['config']
        model.store.__state['uart'] = None
        await asyncio.sleep_ms(100)

async def updateConfigFile():
    count_writeConfig = 0
    path = "/config/config.json"
    while True:
        if(model.store.__state['isConfigUpdate']):

            count_writeConfig+=1
            temp = model.store.__state['config']
            
            if(count_writeConfig > 150):
                print("\nUpdate file: " + path)
                print(temp)
                updateFileWithState(path,model.store.__state)
                count_writeConfig = 0
                model.store.__state['isConfigUpdate'] = False

        await asyncio.sleep_ms(10)

def start():
    try:
        asyncio.run(main())
    except OSError:
        print("error")
    finally:
        asyncio.new_event_loop()
        print('as_demos.auart.test() to run again.')

start()
