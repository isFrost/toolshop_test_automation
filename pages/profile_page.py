from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    # Locators
    F_NAME_INPUT = (By.XPATH, '//*[@id="first_name"]')
    L_NAME_INPUT = (By.XPATH, '//*[@id="last_name"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PHONE_INPUT = (By.XPATH, '//*[@id="phone"]')
    ADDRESS_INPUT = (By.XPATH, '//*[@id="address"]')
    POSTCODE_INPUT = (By.XPATH, '//*[@id="postcode"]')
    CITY_INPUT = (By.XPATH, '//*[@id="city"]')
    STATE_INPUT = (By.XPATH, '//*[@id="state"]')
    COUNTRY_INPUT = (By.XPATH, '//*[@id="country"]')
    UPDATE_BTN = (By.XPATH, '/html/body/app-root/div/app-profile/div/form[1]/div[3]/div/button')
    CURRENT_PASSWORD_INPUT = (By.XPATH, '//*[@id="current-password"]')
    NEW_PASSWORD_INOUT = (By.XPATH, '//*[@id="new-password"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//*[@id="new-password-confirm"]')
    CHANGE_PASSWORD_BTN = (By.XPATH, '/html/body/app-root/div/app-profile/div/form[2]/div[3]/div/button')

    def __init__(self, driver):
        super().__init__(driver)

    def get_profile_data(self):
        """ Get the info of the current user """
        self.wait_until_value_updated(self.F_NAME_INPUT)    # wait until first name is loaded into the input field
        return {
            'first_name': self.wait_for_element(self.F_NAME_INPUT).get_attribute('value'),
            'last_name': self.wait_for_element(self.L_NAME_INPUT).get_attribute('value'),
            'email': self.wait_for_element(self.EMAIL_INPUT).get_attribute('value'),
            'phone': self.wait_for_element(self.PHONE_INPUT).get_attribute('value'),
            'address': self.wait_for_element(self.ADDRESS_INPUT).get_attribute('value'),
            'postcode': self.wait_for_element(self.POSTCODE_INPUT).get_attribute('value'),
            'city': self.wait_for_element(self.CITY_INPUT).get_attribute('value'),
            'state': self.wait_for_element(self.STATE_INPUT).get_attribute('value'),
            'country': self.wait_for_element(self.COUNTRY_INPUT).get_attribute('value')
        }
