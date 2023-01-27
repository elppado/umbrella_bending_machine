from machine import Pin


def lock_init():
    global R1
    global R2

    R1 = Pin(17, Pin.OUT)
    R2 = Pin(18, Pin.OUT)

    R1.on()
    R2.on()
