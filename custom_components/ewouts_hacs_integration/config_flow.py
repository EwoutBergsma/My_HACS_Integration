# ChatGPT made this file
# custom_components/ewouts_hacs_integration/config_flow.py
from __future__ import annotations
from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_NAME
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_NAME, default="Ewout Demo"): str,
    # add your own fields, e.g. host, token, etc.
    # vol.Required(CONF_HOST): str,
    # vol.Required(CONF_API_KEY): str,
})

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    # Do any async validation here (test connection, etc.)
    return {"title": data.get(CONF_NAME) or "Ewout Demo"}

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Ewout's integration."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except Exception:  # replace with specific exceptions
                errors["base"] = "cannot_connect"
            else:
                # Prevent duplicates if your integration has a single instance
                # await self.async_set_unique_id(DOMAIN)  # Ewout removed this line to allow multiple instances
                # self._abort_if_unique_id_configured()  # Ewout removed this line to allow multiple instances
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)
