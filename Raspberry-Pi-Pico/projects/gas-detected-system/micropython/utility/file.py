import json
from configParser import getConfigFromPath
from common import logMessage


def updateFileWithState(path,state):
    jsonObject = getConfigFromPath(path)
    jsonString = getJsonStringWithUpdatedJsonObject(jsonObject,state)
    result = writeJsonToFile(path,jsonString)
    logMessage(result,state['log'])

def getJsonStringWithUpdatedJsonObject(jsonObject,state):
    newObj = {}
    for key in jsonObject:
        newObj[key] = {}
        for param in jsonObject[key]:
            newObj[key][param] = state['config'][key][param]
    return json.dumps(newObj)

def writeJsonToFile(path,jsonString):
    f = open(path,'w')
    f.write(jsonString)
    f.close()
    return "Write json to: " + path