"""Tests for the Shelly integration."""
from homeassistant.components.shelly.const import CONF_SLEEP_PERIOD, DOMAIN
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry


async def init_integration(
    hass: HomeAssistant, gen: int, model="SHSW-25"
) -> MockConfigEntry:
    """Set up the Shelly integration in Home Assistant."""
    data = {
        CONF_HOST: "192.168.1.37",
        CONF_SLEEP_PERIOD: 0,
        "model": model,
        "gen": gen,
    }

    entry = MockConfigEntry(domain=DOMAIN, data=data, unique_id=DOMAIN)
    entry.add_to_hass(hass)

    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    return entry
