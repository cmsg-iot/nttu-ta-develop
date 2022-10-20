# 引入所需模組
from machine import UART,ADC,Pin
import utime
import json
from lib.format import readFileAndFormat

# 參數檔資料夾路徑
configPath ='/config.txt'

# 載入參數檔
config = readFileAndFormat(configPath)

print(config)

# 定義參數
NUM_UART=int(config["NUM_UART"])
BAUD=int(config["BAUD"])
PIN_TX=int(config["PIN_TX"])
PIN_RX=int(config["PIN_RX"])
COUNT_SEND=int(config["COUNT_SEND"])

# UART格式: UART(uartNum, baud, parity, stop, bits, rxPin, txPin)
# 定義UART腳位,如果設定uartNum為1，根據線路圖能使用GPIO 4,5,8,9
uart = UART(NUM_UART, BAUD, parity=None, stop=1, bits=8, rx=Pin(PIN_RX), tx=Pin(PIN_TX))

# 定義ADC腳位
adc0 = ADC(26)
adc1 = ADC(27)
adc2 = ADC(28)

counter = 0

# 處理資料輸出
def handleWriteData(data,countToSend,counter):
    if(counter <= countToSend):
        
        # 將dict格式轉換為JSON格式
        jsonData = json.dumps(data)
        
        # 輸出 uart 資料
        uart.write(str(jsonData))
        
        print(jsonData)
        return True
    else:
        return False
    
    
    

while True:
    read = 0
    data = {}
    command= ""
    isWrite=False
    
    # 讀取 16bits, 0~65535, 0~3.3v
    read = adc0.read_u16()
    data["ADC0"] = read
    utime.sleep_ms(200)
    
    read = adc1.read_u16()
    data["ADC1"] = read
    utime.sleep_ms(200)
    
    read = adc2.read_u16()
    data["ADC2"] = read
    utime.sleep_ms(200)
    
    utime.sleep_ms(400)
    counter+=1
    # 處理資料輸出
    isWrite = handleWriteData(data,COUNT_SEND,counter)
    if(isWrite):
        counter = 0
