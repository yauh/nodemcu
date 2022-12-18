# import dependencies for BME280
from machine import Pin, I2C
import bme280_float as bme280

# import time related libs
import time
from time import sleep

# configure BME280
i2c = I2C(sda=machine.Pin(0), scl=machine.Pin(2))
bme = bme280.BME280(i2c=i2c)

# start taking measurements
while True:
    current_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
    print"Tmp: " + bme.values[0])
    print("Prs: " + bme.values[1])
    # skip humidity since my sensor does not give anything but 0.00%
    # print("Hum: " + bme.values[2])
    print(current_time)
    
    sleep(5)