from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Locators
    PRODUCT_CARDS = (By.CLASS_NAME, 'card')
    PAGINATION_ITEMS = (By.CSS_SELECTOR, 'ul.pagination li.page-item a')
    CARD_IMG = (By.CSS_SELECTOR, 'img.card-img-top')
    CARD_TITLE = (By.CSS_SELECTOR, 'h5.card-title')
    CARD_PRICE = (By.CSS_SELECTOR, '.card-footer span span')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_next_page(self):
        """ Go to the nexxt page of the product catalog """
        pagination = self.wait_for_elements(self.PAGINATION_ITEMS)
        next_btn = next((i for i in pagination if i.text == '»'), None)
        next_btn.click()

    def go_to_previous_page(self):
        """ Go to the previous page of the product catalog """
        pagination = self.wait_for_elements(self.PAGINATION_ITEMS)
        prev_btn = next((i for i in pagination if i.text == '«'), None)
        prev_btn.click()

    def get_product_cards(self):
        """ Return list of product cards displayed on the current page of product catalog """
        cards = self.wait_for_elements(self.PRODUCT_CARDS)
        cards_info = []
        for card in cards:
            cards_info.append(
                {
                    'name': card.find_element(*self.CARD_TITLE).text,
                    'img_caption': card.find_element(*self.CARD_IMG).get_attribute('alt'),
                    'price': card.find_element(*self.CARD_PRICE).text,
                    'element': card
                }
            )
        return cards_info

    def open_product(self, name):
        """ Open product with the specified name """
        cards = self.get_product_cards()
        for card in cards:
            if card['name'] == name:
                card['element'].click()
