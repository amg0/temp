"""
Entity package for ksenia.

Architecture:
    All platform entities inherit from (PlatformEntity, KSeniaLaresEntity).
    MRO order matters — platform-specific class first, then the integration base.
    Entities read data from coordinator.data and NEVER call the API client directly.
    Unique IDs follow the pattern: {entry_id}_{description.key}

See entity/base.py for the KSeniaLaresEntity base class.
"""

from .base import KSeniaLaresEntity

__all__ = ["KSeniaLaresEntity"]
