from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


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
                # options.add_argument('user-agent=Chrome')
                options.add_argument('--window-size=1920,1080')
                return webdriver.Chrome(options=options)
            elif browser == 'Firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                return webdriver.Firefox(options=options)
            elif browser == 'Edge':
                options = webdriver.EdgeOptions()
                options.add_argument('--headless=new')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                return webdriver.Edge(options=options)
        except WebDriverException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages
