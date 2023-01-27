import network


def wifi_init():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("U+Net81C8", "DDAF034733")
