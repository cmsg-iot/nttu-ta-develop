from machine import Pin, ADC


class CD74HC4067:
    def __init__(self, adc=0, select_gpio=[9, 8, 7, 6]):
        self.adc = ADC(adc)
        self.select_gpio = select_gpio
        for i in select_gpio:
            Pin(i, Pin.OUT)

    # 長度不足4從左邊補0，例： '1' -> '0001', '10' -> '0010'
    def __fillzero(self, bits):
        temp = bits
        for i in range(1, 5):
            if (len(bits) < i):
                temp = '0' + temp
        return temp

    # 輸入選擇的channel，切換對應的GPIO輸出
    def __switchGPIO(self, num):
        bits = "{0:b}".format(num)  # 轉換為2進位字串，例： 3 -> '11', 5 -> '101'
        bits = self.__fillzero(bits)
        for i in range(0, 4):
            Pin(self.select_gpio[i]).value(0)
            if (bits[i] == '1'):
                Pin(self.select_gpio[i]).value(1)

    # 讀取指定channel數的ADC值陣列
    def readListOfADC(self, num):
        adc_list = []
        for i in range(0, num):
            self.__switchGPIO(i)
            adc_list.append(self.adc.read_u16())
        return adc_list

    # 讀取指定channel的ADC值
    def readChannelOfADC(self, num):
        self.__switchGPIO(num)
        adc = self.adc.read_u16()
        return adc
