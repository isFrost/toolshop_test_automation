from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Locators
    PRODUCT_NAME = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/span')
    PRODUCT_DESCRIPTION = (By.XPATH, '//*[@id="description"]')
    PRODUCT_IMG = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[1]/figure/div/img')
    PRODUCT_TAGS = (By.CLASS_NAME, 'badge')
    RELATED_PRODUCTS = (By.CLASS_NAME, 'card')
    RELATED_PROD_TITLE = (By.CLASS_NAME, 'card-title')
    INCREASE_QUANTITY = (By.XPATH, '//*[@id="btn-increase-quantity"]')
    REDUCE_QUANTITY = (By.XPATH, '//*[@id="btn-decrease-quantity"]')
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="btn-add-to-cart"]')
    ADD_TO_FAVOURITES = (By.CSS_SELECTOR, '#btn-add-to-favorites')
    POPUP = (By.CSS_SELECTOR, 'div#toast-container div')

    def __init__(self, driver):
        super().__init__(driver)

    def get_name(self):
        """ Return the name of the currently opened product """
        name = self.wait_for_element(self.PRODUCT_NAME)
        return name.text

    def get_description(self):
        """ Return the description of the currently opened product """
        description = self.wait_for_element(self.PRODUCT_DESCRIPTION)
        return description.text

    def get_price(self):
        """ Return the price of the currently opened product """
        price = self.wait_for_element(self.PRODUCT_PRICE)
        return price.text

    def is_image_loaded(self):
        """ Return the image caption of the currently opened product """
        img = self.wait_for_element(self.PRODUCT_IMG)
        return img.size['width'] > 0 and img.size['height'] > 0

    def get_related_products(self):
        """ Return list related products """
        related_cards = self.wait_for_elements(self.RELATED_PRODUCTS)
        related_cards_info = []
        for card in related_cards:
            related_cards_info.append(
                {
                    'name': card.find_element(*self.RELATED_PROD_TITLE).text,
                    'element': card
                }
            )
        return related_cards_info

    def open_related_product(self, prod_name):
        """ Open related product with a specific name """
        products = self.get_related_products()
        for product in products:
            if product['name'] == prod_name:
                product['element'].click()
        self.wait_for_url_to_change()

    def increase_quantity(self):
        """ Click on increase button to increase product quantity """
        increase_btn = self.wait_for_element_to_be_clickable(self.INCREASE_QUANTITY)
        increase_btn.click()

    def reduce_quantity(self):
        """ Click on reduce button to reduce product quantity """
        reduce_btn = self.wait_for_element_to_be_clickable(self.REDUCE_QUANTITY)
        reduce_btn.click()

    def add_to_cart(self):
        """ Add product to cart """
        add_btn = self.wait_for_element_to_be_clickable(self.ADD_TO_CART_BTN)
        add_btn.click()

    def add_to_cart_disabled(self):
        """ Check if button Add to Cart is disabled """
        add_btn = self.wait_for_element(self.ADD_TO_CART_BTN)
        return True if add_btn.get_attribute('disabled') else False

    def get_tags(self):
        """ Return the list of product tags """
        return [tag.text for tag in self.wait_for_elements(self.PRODUCT_TAGS)]

    def add_to_favourites(self):
        """ Add product to favourite list by clicking Add ot favourites button """
        add_btn = self.wait_for_element(self.ADD_TO_FAVOURITES)
        add_btn.click()

    def get_popup(self):
        """ Return the text of the pop-up message """
        return self.wait_for_element(self.POPUP).text
