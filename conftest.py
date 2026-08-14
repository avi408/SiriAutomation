import pytest

from core import DriverManager


@pytest.fixture(scope="session")
def driver():

    driver = DriverManager.get_driver()

    yield driver

    DriverManager.quit_driver()