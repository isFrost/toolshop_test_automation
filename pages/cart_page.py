from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    # Locators
    ITEM = (By.CSS_SELECTOR, '.table > tbody > tr')
    ITEM_NAME = (By.CLASS_NAME, 'product-title')
    ITEM_QUANTITY = (By.CLASS_NAME, 'quantity')
    ITEM_PRICE = (By.CSS_SELECTOR, 'td:nth-child(4)')
    ITEM_TOTAL = (By.CSS_SELECTOR, 'td:nth-child(5)')
    ITEM_XPATH = '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/table/tbody/tr'
    ITEM_TOTAL_XPATH = '/td[5]/span'
    REMOVE_BTN = (By.CSS_SELECTOR, 'a.btn')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_total_to_update(self, name, initial_text, timeout=5):
        """ Wait until the total price of the car item is updated for an item found by its name """
        items = self.wait_for_elements(self.ITEM)
        for item in items:
            if item.find_element(*self.ITEM_NAME).text.strip() == name:
                try:
                    xpath = f'{self.ITEM_XPATH}[{items.index(item) + 1}]{self.ITEM_TOTAL_XPATH}'
                    WebDriverWait(self.driver, timeout).until(
                        EC.none_of(EC.text_to_be_present_in_element((By.XPATH, xpath), initial_text))
                    )
                except TimeoutError as e:
                    print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

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
        for item in items:
            if item.find_element(*self.ITEM_NAME).text.strip() == name:
                item.find_element(*self.ITEM_QUANTITY).clear()
                item.find_element(*self.ITEM_QUANTITY).send_keys(quantity)
                item.find_element(*self.ITEM_QUANTITY).send_keys(Keys.ENTER)

    def remove_item(self, name):
        """ Remove item found by name from the cart """
        items = self.wait_for_elements(self.ITEM)
        for item in items:
            if item.find_element(*self.ITEM_NAME).text.strip() == name:
                item.find_element(*self.REMOVE_BTN).click()
