from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):
    # Locators
    PROFILE_BTN = (By.XPATH, '/html/body/app-root/div/app-overview/div/a[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_profile(self):
        """ Open the profile page of the current user """
        profile_btn = self.wait_for_element(self.PROFILE_BTN)
        profile_btn.click()
