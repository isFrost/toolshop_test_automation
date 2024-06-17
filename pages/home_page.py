from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import logging


class HomePage(BasePage):
    # Locators
    PRODUCT_CARDS = (By.CLASS_NAME, 'card')
    PAGINATION_ITEMS = (By.CSS_SELECTOR, 'ul.pagination li.page-item a')
    PAGINATION_ITEM_WRAPPER = (By.CSS_SELECTOR, 'ul.pagination li.page-item')
    CARD_IMG = (By.CSS_SELECTOR, 'img.card-img-top')
    CARD_TITLE = (By.CSS_SELECTOR, 'h5.card-title')
    CARD_PRICE = (By.CSS_SELECTOR, '.card-footer span span')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search-query')
    SEARCH_BTN = (By.CSS_SELECTOR, 'button.btn:nth-child(4)')
    RESET_SEARCH_BTN = (By.CSS_SELECTOR, 'button.btn:nth-child(3)')
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, '.col-md-9 > h3:nth-child(1)')
    CATALOG_CONTAINER = (By.CSS_SELECTOR, 'app-root div.container app-overview div.row div.col-md-9 div.container')
    SORT_INPUT = (By.CSS_SELECTOR, '.form-select')
    FILTER_CHECKBOXES = (By.CSS_SELECTOR, '#filters .checkbox label')
    MIN_PRICE_SLIDER = (By.CSS_SELECTOR, 'span.ngx-slider-span:nth-child(5)')
    MIN_PRICE_VALUE = (By.CSS_SELECTOR, '.ngx-slider-model-value')
    SLIDER_BAR = (By.CSS_SELECTOR, '.ngx-slider-full-bar')
    LOWER_PRICE_LIMIT = (By.CSS_SELECTOR, 'ngx-slider-floor')
    MAX_PRICE_SLIDER = (By.CSS_SELECTOR, 'span.ngx-slider-span:nth-child(6)')
    MAX_PRICE_VALUE = (By.CSS_SELECTOR, '.ngx-slider-model-high')
    HIGHER_PRICE_LIMIT = (By.CSS_SELECTOR, '.ngx-slider-ceil')
    SEARCH_ERROR = (By.CSS_SELECTOR, '.col-md-9 > div:nth-child(2) > div:nth-child(1)')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_search_to_complete(self, timeout=10, attribute='search_completed'):
        """ Wait until catalog container fains attribute search_completed """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element_attribute(self.CATALOG_CONTAINER, 'data-test', attribute)
            )
        except TimeoutException as e:
            logging.getLogger('auto_test_logger').exception(e)

    def wait_for_search_reset(self, timeout=10):
        """ Wait until search results are reset: product card in the list of results is no longer displayed """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element(self.driver.find_elements(*self.PRODUCT_CARDS)[-1])
            )
        except TimeoutException as e:
            logging.getLogger('auto_test_logger').exception(e)

    def wait_for_next_catalog_page(self, timeout=10):
        """ Wait for products displayed on the page to be updated when navigating to next pagination item
            Checks if previous catalog page is stale
            Default timeout for wait is 10s. Custom timeout can be passed as argument
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.staleness_of(self.driver.find_element(*self.CATALOG_CONTAINER))
            )
        except TimeoutException as e:
            logging.getLogger('auto_test_logger').exception(e)

    def wait_for_products_to_load(self, timeout=10):
        try:
            cards = self.driver.find_elements(*self.PRODUCT_CARDS)
            WebDriverWait(self.driver, timeout).until(
                EC.staleness_of(cards[0])
            )
        except TimeoutException as e:
            logging.getLogger('auto_test_logger').exception(e)

    def go_to_next_page(self):
        """ Go to the nexxt page of the product catalog """
        pagination = self.wait_for_elements(self.PAGINATION_ITEMS)
        next_btn = next((i for i in pagination if i.text == '»'), None)
        next_btn.click()
        self.wait_for_products_to_load()

    def go_to_previous_page(self):
        """ Go to the previous page of the product catalog """
        pagination = self.wait_for_elements(self.PAGINATION_ITEMS)
        prev_btn = next((i for i in pagination if i.text == '«'), None)
        prev_btn.click()

    def has_next(self):
        pagination = self.wait_for_elements(self.PAGINATION_ITEM_WRAPPER)
        if pagination is None:
            return False
        next_btn = next((i for i in pagination if i.text == '»'), None)
        return False if 'disabled' in next_btn.get_attribute('class') else True

    def get_product_cards(self):
        """ Return list of product cards displayed on the current page of product catalog """
        cards = self.wait_for_elements(self.PRODUCT_CARDS, timeout=5)
        cards_info = []
        if cards:
            for card in cards:
                cards_info.append(
                    {
                        'name': card.find_element(*self.CARD_TITLE).text,
                        'img_caption': card.find_element(*self.CARD_IMG).get_attribute('alt'),
                        'price': card.find_element(*self.CARD_PRICE).text,
                        'element': card,
                        'url': card.get_attribute('href')
                    }
                )
        return cards_info

    def open_product(self, name, new_tab=False):
        """ Open product with the specified name """
        cards = self.get_product_cards()
        for card in cards:
            if card['name'] == name:
                if new_tab:
                    self.driver.execute_script('window.open();')
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.get(card['url'])
                else:
                    card['element'].click()

    def search_product(self, product):
        """ Return list of product cards after search query is entered """
        search_field = self.wait_for_element_to_be_clickable(self.SEARCH_FIELD)
        search_field.send_keys(product)
        search_btn = self.wait_for_element(self.SEARCH_BTN)
        search_btn.click()
        self.wait_for_search_to_complete()

    def get_search_error(self):
        """ Return message displayed when the search has no results """
        return self.wait_for_element(self.SEARCH_ERROR).text

    def reset_search(self):
        """ Resets the results of the search """
        reset_btn = self.wait_for_element(self.RESET_SEARCH_BTN)
        reset_btn.click()
        self.wait_for_search_reset()

    def sort_alphabetically_asc(self):
        """ Sorts products by name in ascending order """
        sort_select = Select(self.wait_for_element(self.SORT_INPUT))
        sort_select.select_by_visible_text('Name (A - Z)')
        self.wait_for_search_to_complete(attribute='sorting_completed')

    def sort_alphabetically_desc(self):
        """ Sorts products by name in descending order """
        sort_select = Select(self.wait_for_element(self.SORT_INPUT))
        sort_select.select_by_visible_text('Name (Z - A)')
        self.wait_for_search_to_complete(attribute='sorting_completed')

    def sort_price_desc(self):
        """ Sorts products by price in ascending order """
        sort_select = Select(self.wait_for_element(self.SORT_INPUT))
        sort_select.select_by_visible_text('Price (High - Low)')
        self.wait_for_search_to_complete(attribute='sorting_completed')

    def sort_price_asc(self):
        """ Sorts products by price in ascending descending """
        sort_select = Select(self.wait_for_element(self.SORT_INPUT))
        sort_select.select_by_visible_text('Price (Low - High)')
        self.wait_for_search_to_complete(attribute='sorting_completed')

    def filter_products(self, criteria):
        """ Filters products by the provided criteria """
        filter_options = self.wait_for_elements(self.FILTER_CHECKBOXES)
        for option in filter_options:
            if criteria in option.text:
                checkbox = option.find_element(By.CSS_SELECTOR, '.icheck')
                checkbox.click()
                self.wait_for_search_to_complete(attribute='filter_completed')
                break

    def set_price_limit(self, price, limit='max'):
        """ Sets max or min price limit to the provided price. Foe limit=max is provided sets upper price limit,
            for other values e.g. limit=min sets lover price limit """
        slider = {'price': self.MAX_PRICE_VALUE, 'pointer': self.MAX_PRICE_SLIDER} if limit == 'max' \
            else {'price': self.MIN_PRICE_VALUE, 'pointer': self.MIN_PRICE_SLIDER}   # select min or max slider
        step = int(self.wait_for_element(self.SLIDER_BAR).size['width'])    # initialize slider step
        pointer = self.wait_for_element(slider['pointer'])    # get slider pointer
        value = int(self.wait_for_element(slider['price']).text)    # get current price of the slider
        action = ActionChains(self.driver)    # initialize action object
        while value != price:    # move slider until required value is set
            action.click_and_hold(pointer).move_by_offset(step, 0).release().perform()  # move slider by the step
            value = int(self.wait_for_element(slider['price']).text)  # get current price of the slider
            if value < price:
                step = abs(step / 2) if abs(step / 2) > 2 else 2
            else:
                step = -abs(step / 2) if abs(step / 2) > 2 else -2   # if updated price is larger then
            # required price divide step by 2 and make the value negative to move slider to the right, if less - set
            # positive value to move slider to the left, then repeat the cycle
        self.wait_for_products_to_load()
