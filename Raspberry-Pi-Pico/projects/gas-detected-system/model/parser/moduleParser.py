import deviceConfigParser

def has_key(dict,key):
    if key not in dict:
        return False
    return True

def getModuleData():
    return moduleObj

module = deviceConfigParser.__deviceConfig["module"]

# print('\n')
# print(module)
# print('\n')

moduleObj = {}
params = []
moduleParams = []
typeParams = []

for i in module:
    moduleObj[i]=0

for i in moduleObj:
    params.append(module[i])

for param in params:
    if(has_key(param,'module')):
        moduleParams.append(param)
    else:
        typeParams.append(param)

print(moduleObj)
# print(moduleParams)
# print(typeParams)

# print('\n')
