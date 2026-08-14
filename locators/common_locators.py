"""
Common locators used across multiple screens.
"""

from appium.webdriver.common.appiumby import AppiumBy


class CommonLocators:

    OK_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "OK"
    )

    CANCEL_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Cancel"
    )

    DONE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Done"
    )

    SEARCH_FIELD = (
        AppiumBy.ACCESSIBILITY_ID,
        "Search"
    )