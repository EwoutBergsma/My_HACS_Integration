# custom_components/ewouts_hacs_integration/sensor.py
from __future__ import annotations
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    data = hass.data[DOMAIN][entry.entry_id]
    name = data["name"]
    async_add_entities([EwoutDemoSensor(name)], update_before_add=True)

class EwoutDemoSensor(SensorEntity):
    _attr_native_unit_of_measurement = "units"
    _attr_name: str

    def __init__(self, name: str) -> None:
        self._attr_name = f"{name} Value"
        self._value = 0

    async def async_update(self) -> None:
        # fetch/update your value here
        self._value += 1
        self._attr_native_value = self._value
