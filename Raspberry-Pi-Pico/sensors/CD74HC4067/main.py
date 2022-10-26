from machine import Pin,ADC
import utime

adc = ADC(0)
select_gpio = [9,8,7,6] # 排序為 S3,S2,S1,S0

for i in select_gpio:
    Pin(i,Pin.OUT)

# 輸入選擇的channel，切換對應的GPIO輸出
def switchGPIO(num):
    bits = "{0:b}".format(num) # 轉換為2進位字串，例： 3 -> '11', 5 -> '101'
    bits = fillzero(bits)
    for i in range(0,4):
        Pin(select_gpio[i]).value(0)
        if(bits[i] == '1'):
            Pin(select_gpio[i]).value(1)            

# 長度不足4從左邊補0，例： '1' -> '0001', '10' -> '0010'
def fillzero(bits):
    temp = bits
    for i in range(1,5):
        if(len(bits) < i):
            temp =  '0' + temp
    return temp

def readListOfADC(num):
    adc_list=[]
    for i in range(0,num):
        switchGPIO(i)
        adc_list.append(adc.read_u16())
    return adc_list

def readChannelOfADC(num):
    switchGPIO(num)
    read = adc.read_u16()
    return read

while True:
    #read = readListOfADC(4)
    read = [readChannelOfADC(0),readChannelOfADC(1),readChannelOfADC(2),readChannelOfADC(3)]
    print(read)
    utime.sleep(0.1)
