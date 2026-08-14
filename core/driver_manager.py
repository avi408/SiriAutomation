from core.driver_factory import DriverFactory


class DriverManager:

    _driver = None

    @classmethod
    def get_driver(cls):

        if cls._driver is None:
            cls._driver = DriverFactory.create_driver()

        return cls._driver

    @classmethod
    def quit_driver(cls):

        if cls._driver:
            cls._driver.quit()
            cls._driver = None