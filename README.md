# nodemcu
NodeMCU ESP8266 Code samples in MicroPython

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
