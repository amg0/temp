"""
Runtime data types for ksenia.

Access pattern: entry.runtime_data.client / entry.runtime_data.coordinator
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import KSeniaLaresApiClient
    from .coordinator import KSeniaLaresDataUpdateCoordinator


type KSeniaLaresConfigEntry = ConfigEntry[KSeniaLaresData]


@dataclass
class KSeniaLaresData:
    """Runtime data stored on the config entry after a successful setup."""

    client: KSeniaLaresApiClient
    coordinator: KSeniaLaresDataUpdateCoordinator
    integration: Integration
