from machine import Pin
import time

gruen = 4
gelb = 3
rot = 2

pin_gruen = Pin(gruen, Pin.OUT)
pin_gelb = Pin(gelb, Pin.OUT)
pin_rot = Pin(rot, Pin.OUT)

def gruenphase(dauer):
    pin_gruen.on()
    pin_gelb.off()
    pin_rot.off()
    time.sleep(dauer)

def gelbphase(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.off()
    time.sleep(dauer)
    
def rotphase(dauer):
    pin_gruen.off()
    pin_gelb.off()
    pin_rot.on()
    time.sleep(dauer)

def gelb_rotphase(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.on()
    time.sleep(dauer)

from machine import Pin
import time

gruen = 4
gelb = 3
rot = 2

pin_gruen = Pin(gruen, Pin.OUT)
pin_gelb = Pin(gelb, Pin.OUT)
pin_rot = Pin(rot, Pin.OUT)

def gruenphase(dauer):
    pin_gruen.on()
    pin_gelb.off()
    pin_rot.off()
    time.sleep(dauer)

def gelbphase(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.off()
    time.sleep(dauer)
    
def rotphase(dauer):
    pin_gruen.off()
    pin_gelb.off()
    pin_rot.on()
    time.sleep(dauer)

def gelb_rotphase(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.on()
    time.sleep(dauer)

while True:
    # Gruenphase
    gruenphase(3)
    # Gelbphase
    gelbphase(1)    
    # Rotphase
    rotphase(5)
    # Gelb-Rotphase
    gelb_rotphase(1)
while True:
    # Gruenphase
    gruenphase(3)
    # Gelbphase
    gelbphase(1)    
    # Rotphase
    rotphase(5)
    # Gelb-Rotphase
    gelb_rotphase(1)