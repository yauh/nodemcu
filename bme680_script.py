# import dependencies for BME680
from machine import Pin, I2C
from bme680 import *

# import time related libs
import time
from time import sleep

# configure BME680
i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = BME680_I2C(i2c=i2c)

# start taking measurements
while True:
    current_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
    temperature = str(round(bme.temperature, 2)) + ' C'
    humidity = str(round(bme.humidity, 2)) + ' %'
    pressure = str(round(bme.pressure, 2)) + ' hPa'
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'
    
    print('Temperature:', temperature)
    print('Humidity:', humidity)
    print('Pressure:', pressure)
    print('Gas:', gas)
    print(current_time)
    
    sleep(5)