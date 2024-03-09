from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    # Locators
    PRODUCT_CARDS = (By.CLASS_NAME, 'card')
    PAGINATION_ITEMS = (By.CSS_SELECTOR, 'ul.pagination li.page-item a')
    CARD_IMG = (By.CSS_SELECTOR, 'img.card-img-top')
    CARD_TITLE = (By.CSS_SELECTOR, 'h5.card-title')
    CARD_PRICE = (By.CSS_SELECTOR, '.card-footer span span')
    SEARCH_FIELD = (By.XPATH, '/html/body/app-root/div/app-overview/div[3]/div[1]/form[2]/div/input')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button.btn:nth-child(3)')
    RESET_SEARCH_BTN = (By.CSS_SELECTOR, 'button.btn:nth-child(2)')
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, '.col-md-9 > h3:nth-child(1)')
    CATALOG_CONTAINER = (By.CSS_SELECTOR, '.col-md-9 > div:nth-child(2)')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_search_to_complete(self, timeout=5):
        """ Wait until catalog container fains attribute search_completed """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(self.CATALOG_CONTAINER, 'data-test', 'search_completed')
        )

    def wait_for_search_reset(self, timeout=5):
        """ Wait until search results are reset: container element reloads and visible again """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.CATALOG_CONTAINER))

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
        if cards:
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

    def search_product(self, product):
        """ Return list of product cards after search query is entered """
        search_field = self.wait_for_element_to_be_clickable(self.SEARCH_FIELD)
        search_field.send_keys(product)
        search_btn = self.wait_for_element(self.SEARCH_BTN)
        search_btn.click()
        self.wait_for_search_to_complete()
        search_results = self.get_product_cards()
        return search_results

    def reset_search(self):
        """ Resets the results of the search """
        reset_btn = self.wait_for_element(self.RESET_SEARCH_BTN)
        reset_btn.click()
        self.wait_for_search_reset()
