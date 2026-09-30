from lib import config
from lib.devices import get_device
from lib.messages import sensor_topic

class Rule:
    def __init__(self, device_id, condition, room, actuator):
        self.device_id = device_id
        self.topic = sensor_topic(get_device(device_id), "data")
        self.condition = condition
        self.room = room
        self.actuator = actuator

# Neue Regel = eine neue Zeile: Sensor, Bedingung, Raum und Aktor
RULES = [
    Rule("zb-temp-serverraum", lambda v: v > config.SERVERROOM_TEMP_MAX, "serverraum", "klimaanlage"),
    Rule("lora-soil-garten", lambda v: v < config.SOIL_MOISTURE_MIN, "garten", "bewaesserung"),
    Rule("ble-door-eingang", lambda v: v == "open", "eingang", "alarm"),
]

# Gibt für jede Regel, die zum Topic passt, (Regel, an/aus) zurück
def evaluate(topic, value):
    results = []
    for rule in RULES:
        if rule.topic != topic:
            continue
        try:
            results.append((rule, rule.condition(value)))
        except TypeError:
            print(f"Ungültiger Wert für {rule.device_id}: {value}")
    return results
