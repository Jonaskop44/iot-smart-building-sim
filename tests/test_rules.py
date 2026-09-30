from lib import config
from lib.rules import evaluate

SERVERRAUM = "building/sensors/zigbee/serverraum/temperature/data"
WOHNZIMMER = "building/sensors/zigbee/wohnzimmer/temperature/data"
GARTEN = "building/sensors/lorawan/garten/soil_moisture/data"
EINGANG = "building/sensors/ble/eingang/door/data"

# Hilfsfunktion: welche Aktoren würden wie geschaltet? z. B. [("klimaanlage", True)]
def switched(topic, value):
    return [(rule.actuator, on) for rule, on in evaluate(topic, value)]

def test_serverraum_zu_heiss_klimaanlage_an():
    assert switched(SERVERRAUM, config.SERVERROOM_TEMP_MAX + 1) == [("klimaanlage", True)]

def test_serverraum_normal_klimaanlage_aus():
    assert switched(SERVERRAUM, config.SERVERROOM_TEMP_MAX - 1) == [("klimaanlage", False)]

def test_serverraum_genau_am_schwellwert_bleibt_aus():
    assert switched(SERVERRAUM, config.SERVERROOM_TEMP_MAX) == [("klimaanlage", False)]

def test_boden_zu_trocken_bewaesserung_an():
    assert switched(GARTEN, config.SOIL_MOISTURE_MIN - 1) == [("bewaesserung", True)]

def test_boden_feucht_bewaesserung_aus():
    assert switched(GARTEN, config.SOIL_MOISTURE_MIN + 1) == [("bewaesserung", False)]

def test_tuer_offen_alarm_an():
    assert switched(EINGANG, "open") == [("alarm", True)]

def test_tuer_zu_alarm_aus():
    assert switched(EINGANG, "closed") == [("alarm", False)]

def test_sensor_ohne_regel_schaltet_nichts():
    assert switched(WOHNZIMMER, 50) == []

def test_ungueltiger_wert_wird_ignoriert():
    assert switched(SERVERRAUM, "abc") == []

# monkeypatch ändert den Schwellwert nur für diesen Test (wie ein anderer Wert in der .env)
def test_geaenderter_schwellwert_wird_verwendet(monkeypatch):
    monkeypatch.setattr(config, "SERVERROOM_TEMP_MAX", 20)
    assert switched(SERVERRAUM, 24) == [("klimaanlage", True)]
