from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RentalsPage(BasePage):
    # Locators
    HEADER = (By.CSS_SELECTOR, '.col > h1:nth-child(1)')
    RENTAL_CARDS = (By.CSS_SELECTOR, '.card')
    CARD_TITLE = (By.CSS_SELECTOR, '.card-title')
    CARD_TEXT = (By.CSS_SELECTOR, '.card-text')
    CARD_IMG = (By.CSS_SELECTOR, 'img')

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return self.wait_for_element(self.HEADER).text

    def get_rentals(self):
        cards = self.wait_for_elements(self.RENTAL_CARDS)
        cards_info = []
        for card in cards:
            cards_info.append(
                {
                    'name': card.find_element(*self.CARD_TITLE).text,
                    'description': card.find_element(*self.CARD_TEXT).text,
                    'img_caption': card.find_element(*self.CARD_IMG).get_attribute('alt'),
                    'element': card,
                    'url': card.get_attribute('href')
                }
            )
        return cards_info

    def open_rental(self, name, new_tab=False):
        rentals = self.get_rentals()
        for rental in rentals:
            if rental['name'] == name:
                if new_tab:
                    self.driver.execute_script('window.open();')
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.get(rental['url'])
                else:
                    rental['element'].click()
