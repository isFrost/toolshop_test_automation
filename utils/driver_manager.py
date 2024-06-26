import logging
from selenium import webdriver
from selenium.common import WebDriverException


class DriverManager:
    """Class provides WebDrivers for auto tests"""
    @staticmethod
    def get_driver(browser='Chrome', version=''):
        """Return WebDriver based on the browser. By default, returns Chrome driver"""
        try:
            if browser == 'Chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                service = webdriver.ChromeService()
                return webdriver.Chrome(service=service, options=options)
            elif browser == 'Firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                service = webdriver.FirefoxService()
                return webdriver.Firefox(service=service, options=options)
            elif browser == 'Edge':
                options = webdriver.EdgeOptions()
                options.add_argument('--headless=new')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                service = webdriver.EdgeService()
                return webdriver.Edge(service=service, options=options)
        except WebDriverException as e:
            logging.getLogger('auto_test_logger').exception(e)
