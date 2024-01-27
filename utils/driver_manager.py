from selenium import webdriver
from selenium.common import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


class DriverManager:
    @staticmethod
    def get_driver(browser='Chrome', version='', window='start-maximized'):
        try:
            if browser == 'Chrome':
                options = webdriver.ChromeOptions()
                return webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager(driver_version=version).install(),
                                          options=options.add_argument(window))
                )
            elif browser == 'Firefox':
                options = webdriver.FirefoxOptions()
                return webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager(version=version).install(),
                                           options=options.add_argument(window))
                )
            elif browser == 'Edge':
                options = webdriver.EdgeOptions()
                return webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager(version=version).install(),
                                        options=options.add_argument(window))
                )
        except WebDriverException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages
