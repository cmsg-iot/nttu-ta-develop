import json

path = "/config/config.json"

global __deviceConfig
__deviceConfig = {}

f = open(path,'r')
data = json.load(f)
__deviceConfig = data
f.close()