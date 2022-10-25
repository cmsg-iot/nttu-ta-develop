# from machine import UART,ADC,Pin
from lib.hx711 import HX711

class GPIO:

    def __init__(self,pin=0):
        self.pin = pin
        pass

    def setMode(self,mode=""):
        if(mode == "OUT"):
            # Pin(self.pin,Pin.OUT)
            pass
        else:
            # Pin(self.pin,Pin.IN)
            pass
        
    def getValue(self):
        pass
        # return Pin(self.pin).value()

    def setValue(self,v=0):
        pass
        # Pin(self.pin).value(v)

class WEIGHT:
    def __init__(self,d_out=4,pd_sck=5):
        self.driver = HX711(d_out=d_out,pd_sck=pd_sck)
        self.driver.channel = HX711.CHANNEL_B_32
        self.shift = 0
        self.radial = 0.0
        self.current = 0.0
        self.shift2zero = 0.0
    
    def setChannel(self,v=0):
        if(v==0):
            self.driver.channel = HX711.CHANNEL_B_32
        elif(v==1):
            self.driver.channel = HX711.CHANNEL_A_64
        else:
            self.driver.channel = HX711.CHANNEL_A_128

    def setShift(self,v=0):
        self.shift = v

    def setRadial(self,v=0.0):
        self.radial = v

    def set2zero(self):
        self.shift2zero = self.current
    
    def getValue(self):
        d = self.driver.read()
        d = -d
        d -= self.shift
        if(d<0):
            d = 0
        d /= self.radial
        self.current = d
        return d - self.shift2zero

class PRESSURE:
    def __init__(self,pin):
        self.adc = ADC(pin)
        self.shift = 0
        self.radial = 0.0
    
    def setShift(self,v=0):
        self.shift = v
    
    def setRadial(self, v=0.0):
        self.radial = v
    
    def getValue(self):
        read = self.adc.read_u16()
        read -= self.shift
        if(read < 0):
            read = 0
        read /= self.radial
        return read