from machine import PWM, Pin # 從 machine 中 引入 PWM 與 Pin
from time import sleep # 從 time 中 引入 sleep 模組

# 定義 GPIO2 為 PWM 腳位
led = PWM(Pin(2))

# 使用 duty_u16() 來控制 pwm duty, 數值範圍 0 ~ 65534, 表示 0~ 100%
while True:
    # 在螢幕上顯示目前 duty 值
    print(led.duty_u16())

    # 逐漸增加
    if led.duty_u16() >= 0 and led.duty_u16() < 65534:
        led.duty_u16(led.duty_u16()+100)

    # 到達最大值時重置為 0
    if led.duty_u16() >= 65534:
        led.duty_u16(0)

    # 等待 0.005 秒
    sleep(0.005)