from enum import StrEnum

class Protocol(StrEnum):
    ZIGBEE = "zigbee"
    LORAWAN = "lorawan"
    BLE = "ble"

class SensorType(StrEnum):
    TEMPERATURE = "temperature"
    SOIL_MOISTURE = "soil_moisture"
    DOOR = "door"

class Device:
    def __init__(self, id, protocol, room, type, unit, start):
        self.id = id
        self.protocol = protocol
        self.room = room
        self.type = type
        self.unit = unit
        self.start = start

DEVICES = [
    Device("zb-temp-wohnzimmer", Protocol.ZIGBEE, "wohnzimmer", SensorType.TEMPERATURE, "°C", 21),
    Device("zb-temp-serverraum", Protocol.ZIGBEE, "serverraum", SensorType.TEMPERATURE, "°C", 24),
    Device("lora-soil-garten", Protocol.LORAWAN, "garten", SensorType.SOIL_MOISTURE, "%", 45),
    Device("ble-door-eingang", Protocol.BLE, "eingang", SensorType.DOOR, "", "closed"),
]

def get_device(device_id):
    for device in DEVICES:
        if device.id == device_id:
            return device
    raise ValueError(f"Unbekanntes Gerät: {device_id}")