import pytest
from utils.data_provider import DataProvider
from utils.login_helper import LoginHelper
from pages.product_page import ProductPage
from pages.favourites_page import FavouritesPage
from pages.home_page import HomePage


class TestOrderManagement:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.user = DataProvider.get_data('registered_user.json')
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_add_product_to_favourites(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.get_product_cards()[0]['element'].click()
        product_page = ProductPage(self.driver)
        product = {
            'name': product_page.get_name(),
            'description': product_page.get_description()
        }
        product_page.add_to_favourites()
        product_page.open_favourites()
        favourites_page = FavouritesPage(self.driver)
        added_product = favourites_page.get_products()[0]
        assert added_product['name'] == product['name']
        assert added_product['description'] in product['description']

    def test_remove_product_from_favourites(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.get_product_cards()[0]['element'].click()
        product_page = ProductPage(self.driver)
        product = {
            'name': product_page.get_name(),
            'description': product_page.get_description()
        }
        product_page.add_to_favourites()
        product_page.open_favourites()
        favourites_page = FavouritesPage(self.driver)
        added_product = favourites_page.get_products()[0]
        assert added_product['name'] == product['name']
        assert added_product['description'] in product['description']
        favourites_page.remove_product(added_product['name'])
        assert favourites_page.get_products() is None

    def test_add_product_to_favourites_without_login(self):
        home_page = HomePage(self.driver)
        home_page.get_product_cards()[0]['element'].click()
        product_page = ProductPage(self.driver)
        product_page.add_to_favourites()
        assert product_page.get_popup() == 'Unauthorized, can not add product to your favorite list.'

