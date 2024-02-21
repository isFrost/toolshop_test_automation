from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    # Locators
    F_NAME_INPUT = (By.XPATH, '//*[@id="first_name"]')
    F_NAME_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[1]/div[2]/div')
    L_NAME_INPUT = (By.XPATH, '//*[@id="last_name"]')
    L_NAME_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[2]/div[2]/div')
    BIRTH_DATE_INPUT = (By.XPATH, '//*[@id="dob"]')
    BIRTH_DATE_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[3]/div/div')
    ADDRESS_INPUT = (By.XPATH, '//*[@id="address"]')
    ADDRESS_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[4]/div/div')
    POSTCODE_INPUT = (By.XPATH, '//*[@id="postcode"]')
    POSTCODE_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[5]/div[2]/div')
    CITY_INPUT = (By.XPATH, '//*[@id="city"]')
    CITY_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[6]/div[2]/div')
    STATE_INPUT = (By.XPATH, '//*[@id="state"]')
    STATE_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[7]/div[2]/div')
    COUNTRY_INPUT = (By.XPATH, '//*[@id="country"]')
    COUNTRY_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[8]/div[2]/div')
    PHONE_INPUT = (By.XPATH, '//*[@id="phone"]')
    PHONE_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[9]/div/div')
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    EMAIL_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[10]/div/div')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    PASSWORD_ERROR = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/div[11]/div')
    REGISTER_BTN = (By.XPATH, '/html/body/app-root/div/app-register/div/div/div/form/div/button')

    def __init__(self, driver):
        super().__init__(driver)

    def register_user(self, user):
        """ Register new user """
        first_name_input = self.wait_for_element(self.F_NAME_INPUT)
        first_name_input.send_keys(user['first_name'])
        last_name_input = self.wait_for_element(self.L_NAME_INPUT)
        last_name_input.send_keys(user['last_name'])
        birth_date_input = self.wait_for_element(self.BIRTH_DATE_INPUT)
        birth_date_input.send_keys(user['birth_date'])
        address_input = self.wait_for_element(self.ADDRESS_INPUT)
        address_input.send_keys(user['address'])
        postcode_input = self.wait_for_element(self.POSTCODE_INPUT)
        postcode_input.send_keys(user['postcode'])
        city_input = self.wait_for_element(self.CITY_INPUT)
        city_input.send_keys(user['city'])
        state_input = self.wait_for_element(self.STATE_INPUT)
        state_input.send_keys(user['state'])
        country_input = self.wait_for_element(self.COUNTRY_INPUT)
        country_input.send_keys(user['country'])
        phone_input = self.wait_for_element(self.PHONE_INPUT)
        phone_input.send_keys(user['phone'])
        email_input = self.wait_for_element(self.EMAIL_INPUT)
        email_input.send_keys(user['email'])
        password_input = self.wait_for_element(self.PASSWORD_INPUT)
        password_input.send_keys(user['password'])
        register_btn = self.wait_for_element(self.REGISTER_BTN)
        register_btn.click()

    def get_errors(self):
        """ Return errors for registration of new user with invalid data """
        return {
            'first_name_error': self.wait_for_element(self.F_NAME_ERROR).text,
            'last_name_error': self.wait_for_element(self.L_NAME_ERROR).text,
            'birth_date_error': self.wait_for_element(self.BIRTH_DATE_ERROR).text,
            'address_error': self.wait_for_element(self.ADDRESS_ERROR).text,
            'postcode_error': self.wait_for_element(self.POSTCODE_ERROR).text,
            'city_error': self.wait_for_element(self.CITY_ERROR).text,
            'state_error': self.wait_for_element(self.STATE_ERROR).text,
            'country_error': self.wait_for_element(self.COUNTRY_ERROR).text,
            'phone_error': self.wait_for_element(self.PHONE_ERROR).text,
            'email_error': self.wait_for_element(self.EMAIL_ERROR).text,
            'password_error': self.wait_for_element(self.PASSWORD_ERROR).text
        }
