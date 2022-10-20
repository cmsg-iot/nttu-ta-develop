# 引入所需模組
from machine import UART,ADC,Pin
from time import sleep

# UART格式: UART(uartNum, baud, parity, stop, bits, rxPin, txPin)
# 定義UART腳位,由於設定uartNum為1，根據線路圖能使用GPIO 4,5,8,9, 這邊使用 GPIO4(TX) 及 GPIO5(RX)
uart = UART(1, 115200, parity=None, stop=1, bits=8, Pin(5), Pin(4))

# 定義ADC腳位
adc = ADC(26)

while True:
    read = adc.read_u16()
    print("ACD: ",reading)
    sleep(1)