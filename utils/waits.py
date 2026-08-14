from selenium.webdriver.support.ui import WebDriverWait


class Waits:

    @staticmethod
    def explicit(driver, timeout=20):
        return WebDriverWait(driver, timeout)