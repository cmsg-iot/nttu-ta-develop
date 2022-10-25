import am2320
from machine import I2C, Pin
from utime import sleep
i2c = I2C(0,scl=Pin(17), sda=Pin(16))
sensor = am2320.AM2320(i2c)

while True:
    if sensor.measure() != False:
        print(sensor.temperature())
        print(sensor.humidity())
    sleep(1)
