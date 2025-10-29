# custom_components/ewouts_hacs_integration/sensor.py
# ChatGPT made this file, mostly
from __future__ import annotations
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    name = entry.data.get("name", "Ewout Demo")
    # Use the config entry ID to ensure uniqueness and stability
    unique_id = f"{entry.entry_id}-value"
    device_id = entry.entry_id

    async_add_entities([EwoutDemoSensor(name, unique_id, device_id)], update_before_add=True)

class EwoutDemoSensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_name = "Value"
    _attr_native_unit_of_measurement = "units"

    def __init__(self, base_name: str, unique_id: str, device_id: str) -> None:
        self._base_name = base_name
        self._attr_unique_id = unique_id              # 👈 enables UI editing
        self._device_id = device_id

        # Optional: group under a device in the UI
        self._attr_device_info = {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": base_name,
            "manufacturer": "Ewout",
            "model": "Demo",
        }

    async def async_update(self) -> None:
        # Replace with real data fetch
        self._attr_native_value = getattr(self, "_value", 0) + 1
        self._value = self._attr_native_value

    @property
    def name(self) -> str:
        return f"{self._base_name} {self._attr_name}"
