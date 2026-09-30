import json
from datetime import datetime, timezone

QOS_DATA = 0  
QOS_STATE = 1 
SENSOR_DATA_SUBSCRIPTION = "building/sensors/+/+/+/data"
CONTROLLER_STATUS_TOPIC = "building/controller/status"

def sensor_topic(device, suffix):
    return f"building/sensors/{device.protocol}/{device.room}/{device.type}/{suffix}"

def actuator_topic(room, actuator):
    return f"building/actuators/{room}/{actuator}/state"

def to_json(data):
    data["ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return json.dumps(data, ensure_ascii=False)

def sensor_message(device, value):
    return to_json({"device_id": device.id, "value": value, "unit": device.unit})

def actuator_message(on, reason):
    return to_json({"state": "ON" if on else "OFF", "reason": reason})

def read_value(payload):
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return payload.decode()
    return data.get("value") if isinstance(data, dict) else data