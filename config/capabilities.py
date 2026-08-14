"""
Appium capabilities builder.
"""

from config.settings import Settings


class Capabilities:

    @staticmethod
    def ios():

        return {
            "platformName": Settings.get("device", "platformName"),
            "automationName": Settings.get("device", "automationName"),
            "platformVersion": Settings.get("device", "platformVersion"),
            "deviceName": Settings.get("device", "deviceName"),

            # General Appium Settings
            "newCommandTimeout": 300,
            "noReset": True,
            "autoAcceptAlerts": True,
        }