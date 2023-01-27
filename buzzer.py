from machine import Pin, PWM
import time


def BUZZER_init():
    global buzzer
    buzzer = PWM(Pin(16))
    buzzer.freq(2000)
    buzzer.duty_u16(54235)
    time.sleep(1)
    buzzer.duty_u16(0)


def BUZZER_OPEN():
    global buzzer
    buzzer.duty_u16(64488)
    time.sleep(0.5)
    buzzer.duty_u16(0)
    time.sleep(3)


def BUZZER_BOOT():
    global buzzer
    buzzer.duty_u16(25235)
    time.sleep(0.3)
    buzzer.duty_u16(0)
    buzzer.duty_u16(30235)
    time.sleep(0.3)
    buzzer.duty_u16(0)
