from machine import UART, Pin

class Uart:
    __uart = None
    def __init__(self,uartNum,baud,rxPin,txPin):
        self.uartNum = uartNum
        self.baud = baud
        self.rxPin = rxPin
        self.txPin = txPin
    
    def init(self):
        self.__uart = UART(self.uartNum,self.baud,parity=None,stop=1,bits=8,rx=Pin(self.rxPin),tx=Pin(self.txPin))

    def readline(self):
        return self.__uart.readline()
    
    def write(self,data):
        self.__uart.write(data)