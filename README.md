# NodeMCU ESP8266 Code samples in Arduino

Tested with NodeMCU v2 Amica

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

### BME680 environmental sensor

Variant with 6 pins, using I2C

| ESP8266 NodeMCU | BME680 | Color |
| --- | --- | --- |
| 3.3V | VCC | yellow |
| GND| GND | orange |
| GPIO 2 (D4) | SCL | red |
| GPIO 0 (D3) | SDA | brown |

It also requires the [bme680.py library](https://raw.githubusercontent.com/RuiSantosdotme/Random-Nerd-Tutorials/master/Projects/ESP-MicroPython/bme680.py).
