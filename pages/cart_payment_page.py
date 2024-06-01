from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CartPaymentPage(BasePage):
    # Locators
    PAYMENT_METHOD = (By.CSS_SELECTOR, '#payment-method')
    CARD_NUMBER = (By.CSS_SELECTOR, '#credit_card_number')
    EXPIRATION_DATE = (By.CSS_SELECTOR, '#expiration_date')    # MM/YYYY
    CVV = (By.CSS_SELECTOR, '#cvv')
    CARD_HOLDER = (By.CSS_SELECTOR, '#card_holder_name')
    CONFIRM_BTN = (By.CSS_SELECTOR, '.wizard-steps > aw-wizard-completion-step:nth-child(4) > app-payment:nth-child('
                                    '1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) >'
                                    ' button:nth-child(1)')
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, '.alert div')

    def __init__(self, driver):
        super().__init__(driver)

    def pay_with_credit_card(self):
        """ Method selects credit card payment option, populates payment details and returns confirmation message """
        payment_method = Select(self.wait_for_element(self.PAYMENT_METHOD))
        payment_method.select_by_visible_text('Credit Card')
        card_number = self.wait_for_element(self.CARD_NUMBER)
        card_number.clear()
        card_number.send_keys('0000-0000-0000-0000')
        expiration_date = self.wait_for_element(self.EXPIRATION_DATE)
        expiration_date.clear()
        expiration_date.send_keys('08/2025')
        cvv = self.wait_for_element(self.CVV)
        cvv.clear()
        cvv.send_keys('023')
        card_holder = self.wait_for_element(self.CARD_HOLDER)
        card_holder.clear()
        card_holder.send_keys('SAM SIERA')
        confirm_btn = self.wait_for_element(self.CONFIRM_BTN)
        confirm_btn.click()
        confirmation_message = self.wait_for_element(self.CONFIRMATION_MESSAGE)
        return confirmation_message.text
