# 先在 Thonny 中建立新資料夾，加入兩個新檔案分別命名為 default.txt, led.txt

import os # 引入 os 模組
from time import sleep # 引入 time 模組中的函式
from machine import PWM, Pin # 從 machine 中 引入 PWM 與 Pin
from lib.format import formatConfig,readFileAndFormat # 引入 lib.format 中的函式

# 參數檔資料夾路徑
configPath = '/config/'
defaultConfigFile = configPath + 'default.txt'
customConfigFile = configPath + 'led.txt'

config = readFileAndFormat(customConfigFile)

# 若無內容則載入 default 中的設定
if not len(config):
    print('not found ' + customConfigFile + ', use ' + defaultConfigFile)
    f = open(defaultConfigFile,'r')
    config = f.read()
    f.close()
    config = formatConfig(config)

print(config)

# 定義 PWM 腳位
pwm = PWM(Pin(int(config['pin'])))
bright = int((int(config['bright']) / 100) * 65534)
time = float(config['sleep'])

for i in range(int(config['cycle'])):
    pwm.duty_u16(bright)
    sleep(time)
    pwm.duty_u16(0)
    sleep(time)
    print(i)
