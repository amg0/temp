"""
API package for ksenia.

Exception hierarchy:
    KSeniaLaresApiClientError (base)
    ├── KSeniaLaresApiClientCommunicationError (network/timeout)
    └── KSeniaLaresApiClientAuthenticationError (401/403)

The coordinator maps them onto ConfigEntryAuthFailed and UpdateFailed; nothing else
in the integration imports this package.
"""

from .client import (
    FAN_SPEEDS,
    KSeniaLaresApiClient,
    KSeniaLaresApiClientAuthenticationError,
    KSeniaLaresApiClientCommunicationError,
    KSeniaLaresApiClientError,
)

__all__ = [
    "FAN_SPEEDS",
    "KSeniaLaresApiClient",
    "KSeniaLaresApiClientAuthenticationError",
    "KSeniaLaresApiClientCommunicationError",
    "KSeniaLaresApiClientError",
]
