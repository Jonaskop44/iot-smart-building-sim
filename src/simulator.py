import random
import signal
import sys
import time
from lib import config, mqtt_client
from lib.devices import SensorType, get_device
from lib.messages import QOS_DATA, sensor_message, sensor_topic

def measure(device):
    if device.type == SensorType.DOOR:
        return "open" if random.random() < 0.2 else "closed"
    return round(device.start + random.uniform(-1.5, 1.5), 1)



def main():
    device = get_device(sys.argv[1])
    data_topic = sensor_topic(device, "data")
    status_topic = sensor_topic(device, "status")
    interval = config.INTERVALS[device.protocol]

    client = mqtt_client.connect(device.id, status_topic)
    print(f"[{device.id}] sendet alle {interval}s auf {data_topic}")

    # "docker stop" schickt SIGTERM -> wie Strg+C behandeln
    signal.signal(signal.SIGTERM, signal.default_int_handler)
    try:
        while True:
            value = measure(device)
            client.publish(data_topic, sensor_message(device, value), qos=QOS_DATA)
            print(f"[{device.id}] {value} {device.unit}")
            time.sleep(interval)
    except KeyboardInterrupt:
        mqtt_client.disconnect(client, status_topic)

main()