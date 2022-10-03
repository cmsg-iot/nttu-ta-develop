# 先在 Thonny 中建立新資料夾，加入兩個新檔案分別命名為 default.txt, led.txt

import os # 引入 os 模組
from time import sleep # 引入 time 模組中的函式
from machine import Pin, ADC # 從 machine 中 引入Pin 與 ADC
from lib.format import formatConfig,readFileAndFormat # 引入 lib.format 中的函式

# 參數檔資料夾路徑
configPath = '/config/'
defaultConfigFile = configPath + 'default.txt'
customConfigFile = configPath + 'alert.txt'

config = readFileAndFormat(customConfigFile)

# 若無內容則載入 default 中的設定
if not len(config):
    print('not found ' + customConfigFile + ', use ' + defaultConfigFile)
    f = open(defaultConfigFile,'r')
    config = f.read()
    f.close()
    config = formatConfig(config)

led_pin=Pin(2,Pin.OUT)

sensor_range=int(config["sensor_range"])
alert_thresh=float(config["thresh"]) 
sensor_min=float(config["sensor_minV"]) * 19859
snesor_max=float(config["sensor_maxV"]) * 19859



