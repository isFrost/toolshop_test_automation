from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Locators
    PRODUCT_NAME = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/span')
    PRODUCT_DESCRIPTION = (By.XPATH, '//*[@id="description"]')
    PRODUCT_IMG = (By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[1]/figure/div/img')
    PRODUCT_TAGS = (By.CLASS_NAME, '.badge')
    RELATED_PRODUCTS = (By.CLASS_NAME, 'card')
    RELATED_PROD_TITLE = (By.CLASS_NAME, 'card-title')

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
