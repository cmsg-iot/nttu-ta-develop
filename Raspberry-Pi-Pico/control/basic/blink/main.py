from machine import Pin # 引入 Pin模組
from time import sleep # 引入 sleep 模組，同 arduino 中的 delay, 單位為秒

# 定義 GPIO2 為輸出腳位
led = Pin(2, Pin.OUT)

# 無窮迴圈，同 arduino 中的 loop
while True:
    # 使用 .value() 方法來設定腳位的I/O，led.value(1) 等於 Pin(2,Pin.OUT).value(1)，表示 GPIO2 輸出高電位
    # 直接使用 led.value() 可以取得目前腳位的狀態，not 表示布林函式，將 0 變 1，1 變 0
    # 故下面這段程式碼可以看為： led.value(1) -> 等待0.5秒 -> led.value(0) -> 等待0.5秒 -> led.value(1)...重複執行
    led.value(not led.value())
    sleep(0.5)