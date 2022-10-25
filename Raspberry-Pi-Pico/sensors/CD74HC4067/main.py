from machine import Pin,ADC
import utime

adc = ADC(0)
select_gpio = [9,8,7,6] # 排序為 S3,S2,S1,S0
adc_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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

while True:

    for i in range(0,16):
        switchGPIO(i)
        adc_list[i] = adc.read_u16()

    print(adc_list)
    utime.sleep(0.1)