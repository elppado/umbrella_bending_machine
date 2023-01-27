from machine import Pin


def dht22_init():
    global dht
    import dht
    dht = dht.DHT22(Pin(27))


def dht22_getdata():
    try:
        dht.measure()
        temp = str(dht.temperature())
        hum = str(dht.humidity())
        return temp, hum

    except RuntimeError as e:
        return 0, 0
