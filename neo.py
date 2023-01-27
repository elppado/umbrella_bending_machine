import neopixel
from machine import Pin


def neo_init():
    global np
    np = neopixel.NeoPixel(Pin(9), 1)
    np[0] = (255, 0, 255)
    np.write()


def neo_open():
    global np
    np[0] = (255, 255, 255)
    np.write()


def neo_close():
    global np
    np[0] = (0, 0, 255)
    np.write()


def neo_standby():
    global np
    np[0] = (0, 0, 255)
    np.write()
