import time
from utils.driver_manager import DriverManager as DM


class TestDriver:
    def test_chrome_driver(self):
        """Test that Chrome driver is working"""
        driver = DM.get_driver()
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()

    def test_firefox_driver(self):
        """Test that Firefox driver is working"""
        driver = DM.get_driver('Firefox')
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()

    def test_edge_driver(self):
        """Test that Edge driver is working"""
        driver = DM.get_driver('Edge')
        driver.get('https://google.com')
        time.sleep(3)
        assert driver.title == 'Google'
        driver.quit()
