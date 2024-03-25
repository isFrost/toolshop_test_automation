from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FavouritesPage(BasePage):
    # Locators
    PRODUCT_CARDS = (By.CSS_SELECTOR, '.card')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.card-title')
    PRODUCT_TEXT = (By.CSS_SELECTOR, '.card-text')
    IMG_CAPTION = (By.CSS_SELECTOR, '.card-img')
    REMOVE_BTN = (By.CSS_SELECTOR, '.btn-danger')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_favourites_list_to_update(self, timeout=5):
        """ Wait until the list of favourite products is not displayed """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.PRODUCT_CARDS)
            )
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def get_products(self):
        """ Gather all favourite products displayed on the page and return array of dictionaries
            each dictionary contains name, description, image caption and element itself.
            Return None if no products are found. """
        cards = self.wait_for_elements(self.PRODUCT_CARDS)
        if cards is None:
            return None
        cards_info = []
        for card in cards:
            cards_info.append(
                {
                    'name': card.find_element(*self.PRODUCT_TITLE).text,
                    'description': card.find_element(*self.PRODUCT_TEXT).text.replace('...', ''),
                    'img_caption': card.find_element(*self.IMG_CAPTION).get_attribute('alt'),
                    'element': card
                }
            )
        return cards_info

    def remove_product(self, name):
        """ Removes product from favourites list by searching the product by provided name and clicking remove button
            on the found line item """
        products = self.get_products()
        for product in products:
            if product['name'] == name:
                remove_btn = product['element'].find_element(*self.REMOVE_BTN)
                remove_btn.click()
        self.wait_for_favourites_list_to_update()
