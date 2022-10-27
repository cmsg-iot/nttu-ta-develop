from machine import ADC
from CD74HC4067 import CD74HC4067

class Adc(CD74HC4067):
    def __init__(self, channel=0):
        super().__init__()
        self.channel = channel
        self.shift = 0
        self.radial = 1.0
    
    # 設定偏移值校正
    def setShift(self,val=0):
        v = int(val)
        self.shift = v
    
    # 設定比例值校正
    def setRadial(self, val=1.0):
        v = float(val)
        self.radial = v
    
    # 取得校正後數值
    def getValue(self):
        read = self.readChannelOfADC(self.channel)
        read -= self.shift
        if(read < 0):
            read = 0
        read /= self.radial
        return read