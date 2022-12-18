# import dependencies for SSD1306
from machine import Pin, SoftSPI
import ssd1306

# import dependencies for BME680
from machine import Pin, I2C
from bme680 import *

# import network and more
import network
import ntptime
import time
from time import sleep
import os
import ujson

# configure SSD1306
spi = SoftSPI(
    baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12)
)
dc = Pin(5)  # data/command
rst = Pin(4)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this
display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

# configure BME680
i2c = I2C(scl=Pin(2), sda=Pin(0))
bme = BME680_I2C(i2c=i2c)

# read network config
network_cfg = {}
try:
    with open("network.cfg") as fp:
	    network_cfg = ujson.load(fp)
except OSError:  # open failed
   print("no network config found")
   network_cfg['ssid'] = "nodemcu-esp8266"
   network_cfg['passphrase'] = "my-network-passphrase"

# boot splash screen
display.text("NodeMCU v3", 0, 0)
display.text("Ready", 0, 16)
display.text(network_cfg['ssid'], 0, 32)
display.show()
sleep(1)

# bring up network
# display.fill(0)
# wifi = network.WLAN(network.STA_IF)
# wifi.active(True)
# wifi.connect(network_cfg['ssid'], network_cfg['passphrase'])
# while wifi.isconnected() == False:
#     display.text("Connecting to", 0, 0)
#     display.text(network_cfg['ssid'], 0, 20)
#     display.show()
# display.text("Connected", 15, 45)
# # when connected, set time
# ntptime.settime()  #
# display.show()
# sleep(2)

# # start taking measurements
# counter = 0
# while True:
#     display.fill(0)
#     counter += 1
#     display.text("BME680 values", 0, 0)
#     display.text("Tmp: " + bme.values[0], 0, 15)
#     display.text("Prs: " + bme.values[1], 0, 30)
#     # skip humidity since my sensor does not give anything but 0.00%
#     # display.text("Hum: " + bme.values[2], 0, 45)
#     current_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
#     display.text(current_time, 25, 50)
    
#     display.show()
#     sleep(5)
