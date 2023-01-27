from machine import Pin, UART


def rfid_init():
    global uart1
    global uart2
    uart1 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
    uart2 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))


def rfid_getdata():
    global uart1
    global uart2

    RFID1, RFID2 = 0

    if uart1.any() > 0:
        RFID1 = str(uart1.readline())

    if uart2.any() > 0:
        RFID2 = str(uart2.readline())

    return RFID1, RFID2

