import signal
import time
from lib import mqtt_client
from lib.messages import CONTROLLER_STATUS_TOPIC, QOS_STATE, SENSOR_DATA_SUBSCRIPTION, actuator_message, actuator_topic, read_value
from lib.rules import evaluate

states = {}

def on_message(client, userdata, msg):
    value = read_value(msg.payload)
    for rule, on in evaluate(msg.topic, value):
        topic = actuator_topic(rule.room, rule.actuator)
        if states.get(topic) == on:
            continue
        states[topic] = on
        client.publish(topic, actuator_message(on, f"{rule.device_id}: {value}"), qos=QOS_STATE, retain=True)
        print(f"{topic} -> {'ON' if on else 'OFF'} ({rule.device_id}: {value})")

def main():
    client = mqtt_client.connect("controller", CONTROLLER_STATUS_TOPIC, SENSOR_DATA_SUBSCRIPTION, on_message)
    print(f"[controller] hört auf {SENSOR_DATA_SUBSCRIPTION}")

    signal.signal(signal.SIGTERM, signal.default_int_handler)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        mqtt_client.disconnect(client, CONTROLLER_STATUS_TOPIC)

main()
