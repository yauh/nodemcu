# import dependencies for SSD1306
from machine import Pin, SoftSPI
import ssd1306

# import dependencies for BME680
from machine import Pin, I2C
from bme680 import *

# import network
try:
  import usocket as socket
except:
  import socket
import network

# time related libs
import ntptime
import time
from time import sleep

# import os to access the filesystem
import os
import sys

# import lib to read json config
import ujson

# clean up before we start
import gc
gc.collect()

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
config = {}
try:
    with open("config.cfg") as fp:
	    config = ujson.load(fp)
except OSError:  # open failed
    display.text("NodeMCU v3", 0, 0)
    display.text("config file missing", 0, 16)
    display.text("stopping...", 0, 32)
    display.show()
    print("no network config found")
    config = {"wifi": {
      "ssid:":"nodemcu-esp8266",
      "passphrase":"my-network-passphrase"}
      }
    # //TODO
    # enable access point mode
    # allow configuration via web server
    sys.exit("no config file config.cfg found")

# boot splash screen
display.text("Welcome", 0, 0)
display.text("to NodeMCU", 0, 16)
display.show()
sleep(1)
display.fill(0)

# print config contents
for k,v in config.items():
    print(k, ':', v)

# connect to existing network
wifi = network.WLAN(network.STA_IF)

wifi.active(True)
wifi.connect(config['wifi']['ssid'], config['wifi']['passphrase'])

while wifi.isconnected() == False:
  display.text("Waiting for", 0, 0)
  display.text("connection to", 0, 16)
  display.text(config['wifi']['ssid'], 0, 24)
  display.show()
  pass

display.fill(0)
display.text("Connected to", 0, 0)
display.text(config['wifi']['ssid'], 0, 24)
display.show()
print('Connection successful')
print(wifi.ifconfig())
ntptime.settime()


start_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"

# start taking measurements
while True:
    display.fill(0)
    temperature = str(round(bme.temperature, 2)) + ' C'
    humidity = str(round(bme.humidity, 2)) + ' %'
    pressure = str(round(bme.pressure, 2)) + ' hPa'
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'
    current_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
    display.text(start_time, 0, 0)
    display.text("Tmp: " + temperature, 0, 13)
    display.text("Prs: " + pressure, 0, 26)
    display.text("Hum: " + humidity, 0, 39)
    # display.text("gas: " + gas, 0, 52)
    display.text(current_time, 0, 52)
    display.show()
    sleep(5)
    # //TODO: Add https://github.com/peterhinch/micropython-mqtt
