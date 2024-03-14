import pytest
from utils.data_provider import DataProvider
from pages.home_page import HomePage


class TestProductSearch:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_alphabetic_sort_asc(self):
        home_page = HomePage(self.driver)
        home_page.sort_alphabetically_asc()
        products = home_page.get_all_product_cards()
        print(products[len(products) - 1])
        assert products == sorted(products, key=lambda product: product['name'])

    def test_alphabetic_sort_desc(self):
        home_page = HomePage(self.driver)
        home_page.sort_alphabetically_desc()
        products = home_page.get_all_product_cards()
        assert products == sorted(products, key=lambda product: product['name'], reverse=True)

    def test_price_sort_asc(self):
        home_page = HomePage(self.driver)
        home_page.sort_price_asc()
        products = home_page.get_all_product_cards()
        assert products == sorted(products, key=lambda product: float(product['price'][1:]))

    def test_price_sort_desc(self):
        home_page = HomePage(self.driver)
        home_page.sort_price_desc()
        products = home_page.get_all_product_cards()
        assert products == sorted(products, key=lambda product: float(product['price'][1:]), reverse=True)
