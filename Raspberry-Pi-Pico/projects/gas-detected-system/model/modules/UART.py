from machine import UART, Pin
from time import sleep_us, ticks_diff, ticks_ms

class Uart:
    def __init__(self, id, *args, **kwargs):
        self.timeout = kwargs.pop("timeout", None)
        print(kwargs)
        self.uart = UART(id, **kwargs)
        self.read = self.uart.read
        self.write = self.uart.write
        self.readinto = self.uart.readinto
        self.any = self.uart.any
        self.sendbreak = self.uart.sendbreak
    
    def readUntil(self, termination):
        result = b''
        start = ticks_ms()
        while self.timeout is None or ticks_diff(ticks_ms(), start) < self.timeout:
            if self.uart.any():
                byte = self.uart.read(1)
                result = result + byte
                if byte == termination:
                    break
            sleep_us(10)
        return result

    def readline(self):
        return self.uart.readline()
    
    def any(self):
        return self.uart.any()
    
    def read(self):
        return self.uart.read()
    
    def write(self,data):
        self.uart.write(data)
