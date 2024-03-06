from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartAddressPage(BasePage):
    # Locators
    ADDRESS_FIELD = (By.CSS_SELECTOR, '#address')
    CITY = (By.CSS_SELECTOR, '#city')
    STATE = (By.CSS_SELECTOR, '#state')
    COUNTRY = (By.CSS_SELECTOR, '#country')
    POSTCODE = (By.CSS_SELECTOR, '#postcode')
    PROCEED_BTN = (By.CSS_SELECTOR, '.wizard-steps > aw-wizard-step:nth-child(3) > app-address:nth-child(1) > '
                                    'div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > '
                                    'button:nth-child(1)')

    def __init__(self, driver):
        super().__init__(driver)

    def get_billing_info(self):
        """ Method returns billing address information as  dictionary """
        self.wait_until_value_updated(self.ADDRESS_FIELD)
        return {
            'address': self.wait_for_element(self.ADDRESS_FIELD).get_attribute('value'),
            'city': self.wait_for_element(self.CITY).get_attribute('value'),
            'state': self.wait_for_element(self.STATE).get_attribute('value'),
            'country_code': self.wait_for_element(self.COUNTRY).get_attribute('value'),
            'postcode': self.wait_for_element(self.POSTCODE).get_attribute('value')
        }

    def proceed(self):
        """ Method proceeds to payment details page of order confirmation """
        proceed_btn = self.wait_for_element(self.PROCEED_BTN, timeout=10)
        proceed_btn.click()
