import os
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", "5"))

INTERVALS = {
    "zigbee": float(os.getenv("INTERVAL_ZIGBEE", "5")),
    "ble": float(os.getenv("INTERVAL_BLE", "30")),
    "lorawan": float(os.getenv("INTERVAL_LORAWAN", "60")),
}

SERVERROOM_TEMP_MAX = float(os.getenv("SERVERROOM_TEMP_MAX", "28"))
SOIL_MOISTURE_MIN = float(os.getenv("SOIL_MOISTURE_MIN", "30"))
