# import network and more
import network
import ntptime
import time
from time import sleep

# config
ssid = "my-ssid"
password = "my-passphrase"

# bring up network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while wifi.isconnected() == False:
    print"Connecting to " + ssid)
print("Connected")
# when connected, set time
ntptime.settime()
sleep(2)
