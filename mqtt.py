import time
import machine
import lock
import neo
import buzzer

mqtt_server = '192.168.219.111'
client_id = 'Pico_V1'
topic_sub = b'/test'
topic_pub = b'TUVCC/V1'


def mqtt_init():
    global client
    import mip

    mip.install("umqtt.simple")
    mip.install("umqtt.robust")

    from umqtt.simple import MQTTClient
    client = MQTTClient(client_id, mqtt_server, keepalive=60)


def reconnect():
    time.sleep(3)
    machine.reset()


def sub_cb(topic, msg):
    print("New message on topic {}".format(topic.decode('utf-8')))
    msg = msg.decode('utf-8')
    print(msg)

    if msg == "R1_off":
        lock.R1.off()
        neo.neo_open()
        buzzer.BUZZER_OPEN()
        lock.R1.on()
        neo.neo_close()

    elif msg == "R2_off":
        lock.R2.off()
        neo.neo_open()
        buzzer.BUZZER_OPEN()
        lock.R2.on()
        neo.neo_close()


def mqtt_connect():
    global client
    from umqtt.simple import MQTTClient
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.set_callback(sub_cb)
    client.connect()
    return client


def start_mqtt():
    global client
    try:
        client = mqtt_connect()
        client.publish(topic_pub, "boot")
    except OSError as e:
        reconnect()


def pub_mqtt(topic, p_str):
    global client
    client.publish(topic_pub+topic, p_str)


def sub_mqtt():
    global client
    client.subscribe(topic_sub)
