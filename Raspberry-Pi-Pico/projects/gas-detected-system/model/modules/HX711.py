import sys
sys.path.append("../..")
import lib.hx711

class HX711:
    def __init__(self,d_out=4,pd_sck=5):
        self.driver = lib.hx711.HX711(d_out=d_out,pd_sck=pd_sck)
        self.driver.channel = lib.hx711.HX711.CHANNEL_B_32
        self.shift = 0
        self.radial = 1.0
        self.channel = 0
    
    # 設定 hx711 增益頻道
    def setChannel(self,val=0):
        v = int(val)
        self.channel = v
        if(v==0):
            self.driver.channel = lib.hx711.HX711.CHANNEL_B_32
        elif(v==1):
            self.driver.channel = lib.hx711.HX711.CHANNEL_A_64
        else:
            self.driver.channel = lib.hx711.HX711.CHANNEL_A_128

    # 設定偏移值校正
    def setShift(self,val=0):
        v = int(val)
        self.shift = v

    # 設定比例值校正
    def setRadial(self,val=1.0):
        v = float(val)
        if v <= 0.0: return
        self.radial = v
    
    # 取得校正後重量
    def getValue(self):
        read = self.driver.read()
        read = -read
        read -= self.shift
        if(read<0):
            read = 0
        read /= self.radial
        read = round(read)
        return read
