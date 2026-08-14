"""
Driver Factory

Creates an Appium driver instance.
"""

from appium import webdriver
from appium.options.ios import XCUITestOptions

from config.capabilities import Capabilities
from config.settings import Settings
from core.logger import logger

class DriverFactory:

    @staticmethod
    def create_driver():

        print("=" * 60)
        logger.info("Creating Appium Session")

        options = XCUITestOptions()

        caps = Capabilities.ios()

        print("Capabilities:")
        print(caps)

        options.load_capabilities(caps)

        print("Connecting to Appium Server...")
        print(Settings.get("appium", "server"))

        driver = webdriver.Remote(
            command_executor=Settings.get("appium", "server"),
            options=options
        )

        print("Session Created Successfully!")
        print(driver.session_id)

        return driver