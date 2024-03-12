from machine import Pin, I2C, ADC
import ssd1306

#ESP32 Pin assignment

light_pin=Pin(26)
adc = ADC(light_pin)
light_intensity =adc.read_u16()
light = "Light :" str



I2C = I2C(0, scl= Pin(1), sda=Pin(0))





"""
oled_width = 128
oled_height = 64
oled = ssd1306,SSD1306_I2C(oled_width,oled_height,i2c)

oled.text('Umbwakni', 10, 10)
"""