"""Button platform for ksenia."""

from typing import TYPE_CHECKING

from .reset_filter import ENTITY_DESCRIPTIONS, KSeniaLaresButton

# Acts on the device: the coordinator does not limit outbound calls.
PARALLEL_UPDATES = 1

if TYPE_CHECKING:
    from custom_components.ksenia.data import KSeniaLaresConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: KSeniaLaresConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the button platform."""
    async_add_entities(
        KSeniaLaresButton(entry.runtime_data.coordinator, description) for description in ENTITY_DESCRIPTIONS
    )
