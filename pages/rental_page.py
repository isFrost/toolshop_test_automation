from selenium.webdriver import ActionChains
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By


class RentalPage(ProductPage):
    # Locators
    DURATION_SLIDER = (By.CSS_SELECTOR, '.ngx-slider-pointer-min')
    DURATION_VALUE = (By.CSS_SELECTOR, '.ngx-slider-model-value')
    UNIT_PRICE = (By.CSS_SELECTOR, 'div.col-md-6:nth-child(2) > span:nth-child(3) > span:nth-child(1)')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#total-price')

    def __init__(self, driver):
        super().__init__(driver)

    def set_duration(self, duration):
        slider = self.wait_for_element(self.DURATION_SLIDER)
        value = self.wait_for_element(self.DURATION_VALUE)
        action = ActionChains(self.driver)
        while float(value.text) != duration:
            action.click_and_hold(slider).move_by_offset(50, 0).release().perform()

    def get_unit_price(self):
        return float(self.wait_for_element(self.UNIT_PRICE).text)

    def get_total_price(self):
        return float(self.wait_for_element(self.TOTAL_PRICE).text)
