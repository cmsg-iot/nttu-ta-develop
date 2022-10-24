import json

# 使用絕對路徑
path = "/home/cmsg/github/nttu-ta-develop/Raspberry-Pi-Pico/projects/gas-detected-system/config/devices.json"

# 定義全域變數讓其他程式處理
global __deviceConfig
__deviceConfig={}

f = open(path,"r")
data = json.load(f)
__deviceConfig = data
f.close()