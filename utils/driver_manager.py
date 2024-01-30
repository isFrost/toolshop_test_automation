from selenium import webdriver
from selenium.common import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


class DriverManager:
    """Class provides WebDrivers for auto tests"""
    @staticmethod
    def get_driver(browser='Chrome', version=''):
        """Return WebDriver based on the browser. By default, returns Chrome driver"""
        try:
            if browser == 'Chrome':
                return webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager(driver_version=version).install())
                )
            elif browser == 'Firefox':
                return webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager(version=version).install())
                )
            elif browser == 'Edge':
                return webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager(version=version).install())
                )
        except WebDriverException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages
