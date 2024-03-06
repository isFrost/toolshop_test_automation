import pytest
from utils.driver_manager import DriverManager


@pytest.fixture(scope='function')
def setup_teardown(browser='Chrome'):
    driver = DriverManager.get_driver(browser=browser)
    yield driver
    driver.quit()
