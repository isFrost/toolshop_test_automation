import platform
import pytest
import allure
from utils.driver_manager import DriverManager


@allure.title('Preparation: setup driver')
@pytest.fixture(scope='function')
def setup_teardown(browser='Chrome'):
    """ Setup driver for the test """
    driver = DriverManager.get_driver(browser=browser)
    allure.dynamic.tag(
        f'{platform.system()}: {platform.version()}',    # report OS version
        f'{driver.capabilities["browserName"]} {driver.capabilities["browserVersion"]}'    # report browser version
    )
    yield driver    # provide driver
    driver.quit()    # quit when required actions with the driver are performed
