import pytest
import allure
from utils.data_provider import DataProvider
from pages.home_page import HomePage


class TestProductSearch:
    @allure.title('Preparation: get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC11: Sort products by name in ascending order')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B12', name='TS03TC11')
    def test_alphabetic_sort_asc(self):
        home_page = HomePage(self.driver)
        home_page.sort_alphabetically_asc()
        products = home_page.get_product_cards()
        while home_page.has_next():
            home_page.go_to_next_page()
            products.extend(home_page.get_product_cards())
        assert products == sorted(products, key=lambda product: product['name'])

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC12: Sort products by name in descending order')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B13', name='TS03TC12')
    def test_alphabetic_sort_desc(self):
        home_page = HomePage(self.driver)
        home_page.sort_alphabetically_desc()
        products = home_page.get_product_cards()
        while home_page.has_next():
            home_page.go_to_next_page()
            products.extend(home_page.get_product_cards())
        assert products == sorted(products, key=lambda product: product['name'], reverse=True)

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC13: Sort products by price from low to high')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B14', name='TS03TC13')
    def test_price_sort_asc(self):
        home_page = HomePage(self.driver)
        home_page.sort_price_asc()
        products = home_page.get_product_cards()
        while home_page.has_next():
            home_page.go_to_next_page()
            products.extend(home_page.get_product_cards())
        assert products == sorted(products, key=lambda product: float(product['price'][1:]))

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC14: Sort products from price from high to low')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B15', name='TS03TC14')
    def test_price_sort_desc(self):
        home_page = HomePage(self.driver)
        home_page.sort_price_desc()
        products = home_page.get_product_cards()
        while home_page.has_next():
            home_page.go_to_next_page()
            products.extend(home_page.get_product_cards())
        assert products == sorted(products, key=lambda product: float(product['price'][1:]), reverse=True)
