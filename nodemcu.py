# import dependencies for SSD1306
from machine import Pin, SoftSPI
import ssd1306

# import network and more
import network
import ntptime
from time import sleep

spi = SoftSPI(
    baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12)
)

dc = Pin(5)  # data/command
rst = Pin(4)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

# config
ssid = "my-ssid"
password = "my-ssid-passphrase"

display.text("NodeMCU v3", 0, 0)
display.text("Ready", 0, 16)
display.show()

sleep(5)

display.fill(0)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while wifi.isconnected() == False:
    display.text("Connecting to", 0, 0)
    display.text(ssid, 0, 20)
    display.show()
display.text("Connected", 15, 45)
display.show()
