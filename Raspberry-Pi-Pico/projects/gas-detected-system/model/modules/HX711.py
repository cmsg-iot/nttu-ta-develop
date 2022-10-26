import sys
sys.path.append("../..")
import lib.hx711

class HX711:
    def __init__(self,d_out=4,pd_sck=5):
        self.driver = lib.hx711.HX711(d_out=d_out,pd_sck=pd_sck)
        self.driver.channel = lib.hx711.HX711.CHANNEL_B_32
        self.shift = 0
        self.radial = 1.0
        self.current = 0.0
        self.shift2zero = 0.0
    
    # 設定 hx711 增益頻道
    def setChannel(self,v=0):
        if(v==0):
            self.driver.channel = lib.hx711.HX711.CHANNEL_B_32
        elif(v==1):
            self.driver.channel = lib.hx711.HX711.CHANNEL_A_64
        else:
            self.driver.channel = lib.hx711.HX711.CHANNEL_A_128

    # 設定偏移值校正
    def setShift(self,v=0):
        self.shift = v

    # 設定比例值校正
    def setRadial(self,v=1.0):
        self.radial = v

    # 設定歸零值
    def setShiftZero(self):
        self.shift2zero = self.current
    
    # 清除歸零值
    def resetShiftZero(self):
        self.shift2zero = 0
    
    # 取得校正後重量(扣除歸零值)
    def getValue(self):
        read = self.driver.read()
        read = -read
        read -= self.shift
        if(read<0):
            read = 0
        read /= self.radial
        self.current = read
        return read - self.shift2zero