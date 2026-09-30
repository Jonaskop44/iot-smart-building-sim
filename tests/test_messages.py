import json
from lib.devices import get_device
from lib.messages import actuator_message, actuator_topic, read_value, sensor_message, sensor_topic

def test_sensor_topic_enthaelt_protokoll_raum_und_typ():
    device = get_device("zb-temp-serverraum")
    assert sensor_topic(device, "data") == "building/sensors/zigbee/serverraum/temperature/data"
    assert sensor_topic(device, "status") == "building/sensors/zigbee/serverraum/temperature/status"

def test_actuator_topic():
    assert actuator_topic("serverraum", "klimaanlage") == "building/actuators/serverraum/klimaanlage/state"

def test_sensor_message_ist_json():
    data = json.loads(sensor_message(get_device("zb-temp-serverraum"), 24.3))
    assert data["device_id"] == "zb-temp-serverraum"
    assert data["value"] == 24.3
    assert data["unit"] == "°C"
    assert "ts" in data

def test_actuator_message_ist_json():
    data = json.loads(actuator_message(True, "zu heiß"))
    assert data["state"] == "ON"
    assert data["reason"] == "zu heiß"

def test_read_value_volles_json():
    assert read_value(b'{"device_id": "x", "value": 35, "unit": "C"}') == 35

def test_read_value_nur_value():
    assert read_value(b'{"value": 35}') == 35

def test_read_value_nur_zahl():
    assert read_value(b"35") == 35

def test_read_value_text():
    assert read_value(b"open") == "open"
