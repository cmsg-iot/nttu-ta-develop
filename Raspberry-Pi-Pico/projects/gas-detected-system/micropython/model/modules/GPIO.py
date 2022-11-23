from machine import Pin
from utime import sleep
class GPIO:
    def __init__(self, pin=0, mode=0):
        self.pin = pin
        self.setMode(mode)  # 初始化時呼叫自己的方法設定模式
    
    def setMode(self,mode=0):
        if mode:
            Pin(self.pin,Pin.OUT)
        else:
            Pin(self.pin,Pin.IN)
        
    def getValue(self):
        return Pin(self.pin).value()

    def setValue(self,val=0):
        Pin(self.pin).value(val)
    
    def openWithTime(self,time=1):
        t = int(time)
        Pin(self.pin).value(1)
        sleep(t)
        Pin(self.pin).value(0)