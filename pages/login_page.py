from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Locators
    LOGIN_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    SUBMIT_BTN = (By.XPATH, '/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
    REGISTER_BTN = (By.XPATH, '/html/body/app-root/div/app-login/div/div/div/form/div[4]/p/a[1]')
    ERROR_MESSAGE = (By.XPATH, '/html/body/app-root/div/app-login/div/div/div/form/div[4]/div')
    FORM_TITLE = (By.XPATH, '/html/body/app-root/div/app-login/div/div/div/h3')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login, password):
        """ Login user to the site """
        login_input = self.wait_for_element(self.LOGIN_INPUT)
        login_input.send_keys(login)
        password_input = self.wait_for_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_btn = self.wait_for_element(self.SUBMIT_BTN)
        submit_btn.click()

    def go_to_register_page(self):
        """ Open page to register new user """
        register_btn = self.wait_for_element(self.REGISTER_BTN)
        register_btn.click()

    def get_error(self):
        """ Get error message for incorrect input """
        error_message = self.wait_for_element(self.ERROR_MESSAGE)
        return error_message.text

    def get_form_title(self):
        """ Get the title of login form """
        form_title = self.wait_for_element(self.FORM_TITLE)
        return form_title.text
