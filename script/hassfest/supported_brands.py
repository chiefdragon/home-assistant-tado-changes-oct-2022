"""Generate supported_brands data."""
from __future__ import annotations

import black

from .model import Config, Integration
from .serializer import to_string

BASE = """
\"\"\"Automatically generated by hassfest.

To update, run python3 -m script.hassfest
\"\"\"

HAS_SUPPORTED_BRANDS = {}
""".strip()


def generate_and_validate(integrations: dict[str, Integration], config: Config) -> str:
    """Validate and generate supported_brands data."""

    brands = [
        domain
        for domain, integration in sorted(integrations.items())
        if integration.supported_brands
    ]

    return black.format_str(BASE.format(to_string(brands)), mode=black.Mode())


def validate(integrations: dict[str, Integration], config: Config) -> None:
    """Validate supported_brands data."""
    supported_brands_path = config.root / "homeassistant/generated/supported_brands.py"
    config.cache["supported_brands"] = content = generate_and_validate(
        integrations, config
    )

    if config.specific_integrations:
        return

    if supported_brands_path.read_text(encoding="utf-8") != content:
        config.add_error(
            "supported_brands",
            "File supported_brands.py is not up to date. Run python3 -m script.hassfest",
            fixable=True,
        )


def generate(integrations: dict[str, Integration], config: Config):
    """Generate supported_brands data."""
    supported_brands_path = config.root / "homeassistant/generated/supported_brands.py"
    supported_brands_path.write_text(
        f"{config.cache['supported_brands']}", encoding="utf-8"
    )
