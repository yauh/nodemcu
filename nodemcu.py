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

# import lib for mqtt
from umqtt.simple import MQTTClient

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

# Wifi config
WIFI_SSID = config['wifi']['ssid']
WIFI_PASSPHRASE = config['wifi']['passphrase']

# connect to existing network
wifi = network.WLAN(network.STA_IF)

wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSPHRASE)

while wifi.isconnected() == False:
  display.text("Waiting for", 0, 0)
  display.text("connection to", 0, 16)
  display.text(WIFI_SSID, 0, 24)
  display.show()
  pass

display.fill(0)
display.text("Connected to", 0, 0)
display.text(WIFI_SSID, 0, 24)
display.show()
print('Connection successful')
print(wifi.ifconfig())
ntptime.settime()
start_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
print('Time is set to ' + start_time)

# MQTT config
MQTT_CLIENT = config['mqtt']['client']
MQTT_TOPIC = config['mqtt']['topic']
MQTT_SERVER = config['mqtt']['server']
MQTT_PORT = config['mqtt']['port']
MQTT_USER = config['mqtt']['user']
MQTT_PASSWORD = config['mqtt']['password']
MQTT_KEEPALIVE = 60

MQTT_TOPIC_TEMPERATURE = MQTT_TOPIC + "/bme680/temperature"
MQTT_TOPIC_HUMIDITY = MQTT_TOPIC + "/bme680/humidity"
MQTT_TOPIC_PRESSURE = MQTT_TOPIC + "/bme680/pressure"
MQTT_TOPIC_GAS = MQTT_TOPIC + "/bme680/gas"

# set up mqtt connection
print('connecting to mqtt broker at ' + MQTT_SERVER)
mqttc = MQTTClient(MQTT_CLIENT, MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASSWORD, MQTT_KEEPALIVE)

mqttc.connect()

# start taking measurements
while True:
    display.fill(0)
    current_time = f"{time.gmtime()[3]:02}:{time.gmtime()[4]:02}:{time.gmtime()[5]:02}"
    print('Measuring at ' + current_time)
    temperature_value = str(round(bme.temperature, 2)) # °C
    humidity_value = str(round(bme.humidity, 2)) # % 
    pressure_value = str(round(bme.pressure, 2)) # hPa
    gas_value = str(round(bme.gas/1000, 2)) # KOhms

    temperature_display = temperature_value + ' C'
    humidity_display = humidity_value + ' %'
    pressure_display = pressure_value + ' hPa'
    gas_display = gas_value + ' KOhms'
    
    display.text(start_time, 0, 0)
    display.text("Tmp: " + temperature_display, 0, 13)
    display.text("Prs: " + humidity_display, 0, 26)
    display.text("Hum: " + pressure_display, 0, 39)
    # display.text("gas: " + gas_display, 0, 52)
    display.text(current_time, 0, 52)
    display.show()
    print('publishing to mqtt')
    mqttc.publish( MQTT_TOPIC_TEMPERATURE.encode(), temperature_value.encode())
    mqttc.publish( MQTT_TOPIC_HUMIDITY.encode(), humidity_value.encode())
    mqttc.publish( MQTT_TOPIC_PRESSURE.encode(), pressure_value.encode())
    mqttc.publish( MQTT_TOPIC_GAS.encode(), gas_value.encode())
    sleep(60)
    gc.collect()
    # //TODO: Consider building and switching to https://github.com/peterhinch/micropython-mqtt
    
