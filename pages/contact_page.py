from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactPage(BasePage):
    # Locators
    SUBJECT = (By.CSS_SELECTOR, '#subject')
    MESSAGE = (By.CSS_SELECTOR, '#message')
    SEND_BTN = (By.CSS_SELECTOR, '.btnSubmit')
    MESSAGE_VALIDATION_ERROR = (By.CSS_SELECTOR, '#message_alert div')
    SEND_VALIDATION_ERROR = (By.CSS_SELECTOR, '.help-block')

    def __init__(self, driver):
        super().__init__(driver)

    def send_message(self, subject, message):
        """ Selects message subject by finding provided subject attribute in the selector options,
            populates message input text field with the provided message text and clicks send button """
        subject_select = Select(self.wait_for_element(self.SUBJECT))
        subject_select.select_by_visible_text(subject)
        message_input = self.wait_for_element(self.MESSAGE)
        message_input.clear()
        message_input.send_keys(message)
        send_btn = self.wait_for_element(self.SEND_BTN)
        send_btn.click()

    def get_message_validation_error(self):
        """ Returns the text of error message displayed on input invalid message """
        message = self.wait_for_element(self.MESSAGE_VALIDATION_ERROR)
        return message.text

    def get_send_validation_error(self):
        """ Returns the text of error message displayed on sending invalid message """
        message = self.wait_for_element(self.SEND_VALIDATION_ERROR)
        return message.text
