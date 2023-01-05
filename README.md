# NodeMCU ESP8266 Code samples in MicroPython

Sample scripts follow the naming convention `<sensor>_script.py`. These samples are minimal on purpose.

The is currently `nodemcu.py` and should be renamed to `main.py` when copied to the ESP8266.

Tested with NodeMCU v2 Amica and NodeMCU v3 Lolin

**Beware** Using [Mu Editor](https://codewith.mu) did not allow me to transfer files to the v2 model. Instead I used [Visual Studio Code](https://code.visualstudio.com) with the [PyMakr extension](https://github.com/pycom/pymakr-vsc). This works without any issues on a M1 MacBook using a USB hub.

## Network connectivity

### MQTT client

Use [mqtt_as.py](https://github.com/peterhinch/micropython-mqtt/tree/master/mqtt_as) instead of standard mqtt libraries.

## Connecting hardware

### SSD1306 OLED Display

| ESP8266 NodeMCU | OLED Display | Color |
| --- | --- | --- |
| GND | GND | white |
| 3.3V | VCC | black |
| GPIO 14 (D5) | D0 (SCK / CLK) | brown |
| GPIO 13 (D7) | D1 (MOSI) | red |
| GPIO 4 (D2) | RES | orange |
| GPIO 5 (D1) | DC | yellow |
| GPIO 15 (D8) | CS | green |

For details see [this blog entry](https://www.herrhochhaus.de/Micropython_esp8266-ssd1306/).

### BME280 environmental sensor

Variant with 4 wires, using I2C

| ESP8266 NodeMCU | BME280 | Color |
| --- | --- | --- |
| GND | GND | grey |
| 3.3V | VIN | white |
| GPIO 2 (D4) | SCL | purple |
| GPIO 0 (D3) | SDA | blue |

It also requires the [bme280_float.py library](https://github.com/robert-hh/BME280/).

### BME680 environmental sensor

Variant with 6 pins, using I2C

| ESP8266 NodeMCU | BME680 | Color |
| --- | --- | --- |
| 3.3V | VCC | yellow |
| GND| GND | orange |
| GPIO 2 (D4) | SCL | red |
| GPIO 0 (D3) | SDA | brown |

It also requires the [bme680.py library](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/bme680.py).
