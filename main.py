import time
import uart_rfid
import DHT22
import buzzer
import lock
import wifi
import neo
import mqtt

# init
buzzer.BUZZER_init()
wifi.wifi_init()
uart_rfid.rfid_init()
lock.lock_init()
neo.neo_init()
DHT22.dht22_init()
mqtt.mqtt_init()
# init


# start
neo.neo_standby()
mqtt.start_mqtt()
buzzer.BUZZER_BOOT()
# start

mqtt.pub_mqtt("", b"stand-by")

while True:  # main LOOP
    mqtt.sub_mqtt()

    temp, hum = DHT22.dht22_getdata()

    if temp or hum:
        mqtt.pub_mqtt("/DHT/temp", temp)
        mqtt.pub_mqtt("/DHT/hum", hum)
    else:
        mqtt.pub_mqtt("/DHT", "DHT_Fail")

    RFID_data1, RFID_data2 = uart_rfid.rfid_getdata()

    if RFID_data1:
        mqtt.pub_mqtt("/RFID1", RFID_data1)
    if RFID_data2:
        mqtt.pub_mqtt("/RFID2", RFID_data2)

    time.sleep(2)
