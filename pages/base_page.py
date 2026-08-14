"""
BasePage

Contains all reusable Appium actions.
Every Page Object should inherit from this class.
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def exists(self, locator):
        return len(
            self.driver.find_elements(*locator)
        ) > 0

    # -------------------------
    # Wait Helpers
    # -------------------------

    def wait_until_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    # -------------------------
    # Device Helpers
    # -------------------------

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def back(self):
        self.driver.back()

    def get_page_source(self):
        return self.driver.page_source

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # -------------------------
    # Gestures
    # -------------------------

    def swipe_up(self):
        size = self.driver.get_window_size()

        x = size["width"] // 2

        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.2)

        self.driver.swipe(
            x,
            start_y,
            x,
            end_y,
            500
        )

    def swipe_down(self):

        size = self.driver.get_window_size()

        x = size["width"] // 2

        start_y = int(size["height"] * 0.2)
        end_y = int(size["height"] * 0.8)

        self.driver.swipe(
            x,
            start_y,
            x,
            end_y,
            500
        )