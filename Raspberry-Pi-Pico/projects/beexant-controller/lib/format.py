# 定義格式化參數函式，將傳入的參數字串格式化為字典格式回傳
def formatConfig(config):
    tempConfig = config.split( )
    config = {}
    for v in tempConfig:
        temp = v.split('=')
        config[temp[0]] = temp[1]
    return config

# 讀取參數檔內容，並呼叫格式化函式後回傳結果
def readFileAndFormat(path):
    try:
        f = open(path,'r')
        config = f.read()
        f.close()
        config = formatConfig(config)
    except IndexError as error:
        print('target file format failed: '+ path + '\n')
        print('error message: ')
        print(error)
        print('\n')
        return {}
    return config
