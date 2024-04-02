import time
import allure
from utils.driver_manager import DriverManager as DM


class TestDriver:
    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS00: Driver Smoke Test')
    @allure.sub_suite('TC01: Open Chrome browser')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_chrome_driver(self):
        """Test that Chrome driver is working"""
        driver = DM.get_driver()
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS00: Driver Smoke Test')
    @allure.sub_suite('TC02: Open Firefox browser')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_firefox_driver(self):
        """Test that Firefox driver is working"""
        driver = DM.get_driver('Firefox')
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS00: Driver Smoke Test')
    @allure.sub_suite('TC03: Open Edge browser')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edge_driver(self):
        """Test that Edge driver is working"""
        driver = DM.get_driver('Edge')
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()
