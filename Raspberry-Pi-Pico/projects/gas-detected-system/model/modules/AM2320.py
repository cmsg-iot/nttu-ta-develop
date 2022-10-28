import sys
sys.path.append("../..")
from machine import I2C,Pin
import lib.am2320

class AM2320:
    def __init__(self, i2cNum=0, scl=17, sda=16, freq=100000):
        self.i2c = I2C(i2cNum,scl=Pin(scl),sda=Pin(sda),freq=freq)
        self.sensor = lib.am2320.AM2320(self.i2c)
    
    # 回傳感測器讀取資料，未讀到回傳 None
    def getMeasureData(self):
        data = {}
        if self.sensor.measure() != False:
            temp = self.sensor.temperature()
            hum = self.sensor.humidity()
            data['temp'] = round(temp * 10) / 10
            data['hum'] =  round(hum * 10) / 10
            return data
        return None
