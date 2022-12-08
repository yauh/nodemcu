from machine import Pin, SoftSPI
import ssd1306
import network
from time import sleep

spi = SoftSPI(
    baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12)
)

dc = Pin(5)  # data/command
rst = Pin(4)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

oled = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

ssid = "my-ssid"
password = "my-password"

oled.fill(0)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while wifi.isconnected() == False:
    oled.text("Connecting to", 0, 0)
    oled.text(ssid, 0, 20)
    oled.show()
oled.text("Connected", 15, 45)
oled.show()

