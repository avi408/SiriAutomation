"""
Siri UI Locators

NOTE:
These are placeholder locators until we inspect the
actual Siri accessibility tree using Appium Inspector.
"""

from appium.webdriver.common.appiumby import AppiumBy


class SiriLocators:

    MICROPHONE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Microphone"
    )

    RESPONSE_TEXT = (
        AppiumBy.IOS_PREDICATE,
        'type == "XCUIElementTypeStaticText"'
    )

    TEXT_INPUT = (
        AppiumBy.IOS_CLASS_CHAIN,
        "**/XCUIElementTypeTextField"
    )