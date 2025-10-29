"""Ewout's HACS Integration custom component for Home Assistant."""
# custom_components/ewouts_hacs_integration/__init__.py
from __future__ import annotations
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform

DOMAIN = "ewouts_hacs_integration"


PLATFORMS: list[Platform] = [Platform.SENSOR]  # add others as needed

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    # Do NOT read YAML here; we’re UI-only now.
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Store anything you need on hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "name": entry.data.get("name", "Ewout Demo")
        # plus any clients/coordinators you create
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
