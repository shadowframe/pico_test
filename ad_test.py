import time
from machine import Pin, ADC

analog_in = ADC(Pin(26))

while True:
    value = 1 * analog_in.read_u16() / 65727
    value = round(value, 2)
    print(value)
    time.sleep(1)
    