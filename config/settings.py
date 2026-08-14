"""
Framework Settings

Loads configuration from config.yaml
and provides access to configuration values.
"""

from pathlib import Path
import yaml


class Settings:
    _config = None

    @classmethod
    def load(cls):
        """Load configuration only once."""

        if cls._config is None:

            config_path = (
                Path(__file__).parent / "config.yaml"
            )

            with open(config_path, "r", encoding="utf-8") as file:
                cls._config = yaml.safe_load(file)

        return cls._config

    @classmethod
    def get(cls, section, key=None):
        """
        Read configuration values.

        Examples:

        Settings.get("device")

        Settings.get("device", "deviceName")
        """

        config = cls.load()

        if section not in config:
            raise KeyError(f"Missing section '{section}'")

        if key is None:
            return config[section]

        if key not in config[section]:
            raise KeyError(
                f"Missing key '{key}' under '{section}'"
            )

        return config[section][key]

    @classmethod
    def validate(cls):
        """
        Validate mandatory configuration.
        """

        required = {
            "appium": [
                "server",
            ],
            "device": [
                "platformName",
                "automationName",
                "platformVersion",
                "deviceName",
            ]
        }

        for section, keys in required.items():

            for key in keys:

                value = cls.get(section, key)

                if value in ("", None):

                    raise ValueError(
                        f"Missing configuration: {section}.{key}"
                    )