from pages.home_page import HomePage
from selenium.webdriver.common.by import By


class CategoryPage(HomePage):
    # Locators
    CATEGORY_NAME = (By.XPATH, '/html/body/app-root/div/app-category/div[1]/h2')

    def __init__(self, driver):
        super().__init__(driver)

    def get_category(self):
        """ Returns the text of the header with category name """
        category = self.wait_for_element(self.CATEGORY_NAME)
        return category.text
