import time
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from lib import config
from lib.messages import QOS_STATE

def connect(client_id, status_topic):
    client = mqtt.Client(CallbackAPIVersion.VERSION2, client_id=client_id)
    client.will_set(status_topic, "offline", qos=QOS_STATE, retain=True)

    def on_connect(*_):
        client.publish(status_topic, "online", qos=QOS_STATE, retain=True)

    client.on_connect = on_connect

    client.connect_async(config.MQTT_HOST, config.MQTT_PORT, config.MQTT_KEEPALIVE)
    client.loop_start()
    while not client.is_connected():
        time.sleep(0.1)
    return client

def disconnect(client, status_topic):
    client.publish(status_topic, "offline", qos=QOS_STATE, retain=True).wait_for_publish()
    client.disconnect()
    client.loop_stop()