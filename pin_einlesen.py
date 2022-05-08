from machine import Pin
import time

SW1 = 5

sw1 = Pin(SW1, Pin.IN, Pin.PULL_UP)

while True:
    print("Schalter 1: " + str(sw1.value()))
    time.sleep(1)


