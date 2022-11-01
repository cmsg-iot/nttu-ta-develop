import json

def getConfigFromPath(path):
    config = {}
    f = open(path,'r')
    config = json.load(f)
    f.close()
    return config
