#from machine import freq
from hx711 import HX711
from time import sleep

#freq(125000000)

driver = HX711(d_out=4, pd_sck=5)

driver.channel = HX711.CHANNEL_B_32
#driver.channel = HX711.CHANNEL_A_64
#driver.channel = HX711.CHANNEL_A_128

print(driver)

#offset = 40000
#offset = 22400
offset = 11570
while True:
    d = driver.read()
#    print(d)
    d = -d
    d -= offset
    if(d<0):
        d=0
#    d /= 20
#    d /= 13
    d /= 6.4583
    print(d)
    sleep(0.5)
    
