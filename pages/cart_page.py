from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging


class CartPage(BasePage):
    # Locators
    ITEM = (By.CSS_SELECTOR, '.table > tbody > tr')
    APP_CART = (By.CSS_SELECTOR, '.wizard-steps > aw-wizard-step:nth-child(1) > app-cart:nth-child(1)')
    ITEM_NAME = (By.CLASS_NAME, 'product-title')
    ITEM_QUANTITY = (By.CLASS_NAME, 'quantity')
    ITEM_PRICE = (By.CSS_SELECTOR, 'tr.ng-star-inserted > td:nth-child(3) > span:nth-child(1)')
    ITEM_TOTAL = (By.CSS_SELECTOR, 'tr.ng-star-inserted > td:nth-child(4) > span:nth-child(1)')
    ITEM_XPATH = '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/table/tbody/tr'
    ITEM_TOTAL_XPATH = '/td[5]/span'
    REMOVE_BTN = (By.CSS_SELECTOR, 'a.btn')
    PROCEED_BTN = (By.CSS_SELECTOR, 'div.float-end:nth-child(2) > button:nth-child(1)')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_item_to_be_removed(self, element):
        WebDriverWait(self.driver, timeout=5).until(
            EC.invisibility_of_element(element)
        )

    def get_cart_items(self):
        """ Get all the items displayed in the cart """
        items = self.wait_for_elements(self.ITEM)
        if not items:
            return None
        items_info = []
        for item in items:
            items_info.append(
                {
                    'name': item.find_element(*self.ITEM_NAME).text.strip(),
                    'quantity': item.find_element(*self.ITEM_QUANTITY).get_attribute('value'),
                    'price': item.find_element(*self.ITEM_PRICE).text,
                    'total': item.find_element(*self.ITEM_TOTAL).text
                }
            )
        return items_info

    def set_item_quantity(self, name, quantity):
        """ Change the quantity of cart item found by product name """
        items = self.wait_for_elements(self.ITEM)
        for i, item in enumerate(items):
            if item.find_element(*self.ITEM_NAME).text.strip() == name:
                init_price = item.find_element(*self.ITEM_TOTAL).text
                item.find_element(*self.ITEM_QUANTITY).clear()
                item.find_element(*self.ITEM_QUANTITY).send_keys(quantity)
                item.find_element(*self.ITEM_QUANTITY).send_keys(Keys.ENTER)
                try:
                    WebDriverWait(self.driver, 5).until(
                        lambda x: self.wait_for_elements(self.ITEM)[i].find_element(*self.ITEM_TOTAL).text != init_price
                    )
                except TimeoutError as e:
                    logging.getLogger('auto_test_logger').exception(e)

    def remove_item(self, name):
        """ Remove item found by name from the cart """
        items = self.wait_for_elements(self.ITEM)
        for item in items:
            if item.find_element(*self.ITEM_NAME).text.strip() == name:
                item.find_element(*self.REMOVE_BTN).click()
                self.wait_for_item_to_be_removed(item)

    def proceed_to_sign_in(self):
        """ Proceed to sign in screen of order management """
        proceed_btn = self.wait_for_element(self.PROCEED_BTN, timeout=10)
        proceed_btn.click()
