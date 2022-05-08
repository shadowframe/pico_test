from machine import Pin
import utime
led_rot = Pin(2, Pin.OUT)

while True:
    led_rot.on()
    utime.sleep(1)
    led_rot.off()
    utime.sleep(1)