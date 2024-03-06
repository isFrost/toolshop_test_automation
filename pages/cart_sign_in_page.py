from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartSignInPage(BasePage):
    # Locators
    PROCEED_BTN = (By.CSS_SELECTOR, '.wizard-steps > aw-wizard-step:nth-child(2) > app-login:nth-child(1) > '
                                    'div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > '
                                    'button:nth-child(1)')

    def __init__(self, driver):
        super().__init__(driver)

    def proceed(self):
        proceed_btn = self.wait_for_element(self.PROCEED_BTN)
        proceed_btn.click()
