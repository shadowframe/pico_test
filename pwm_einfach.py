from machine import Pin, PWM

pwm1 = PWM(Pin(6))
pwm1.freq(8)
pwm1.duty_u16(30000)

while True:
    pass


