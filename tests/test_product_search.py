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
    @allure.sub_suite('TC01: Search product by name')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B2', name='TS03TC01')
    def test_search_by_product(self):
        home_page = HomePage(self.driver)
        filtered_products = home_page.search_product('Claw Hammer')
        for product in filtered_products:
            assert 'Claw Hammer' in product['name']

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC02: Search non-existing product')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B3', name='TS03TC02')
    def test_search_non_existing_product(self):
        home_page = HomePage(self.driver)
        filtered_products = home_page.search_product('Non-Existing Product 1111')
        assert len(filtered_products) == 0

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC03: Reset search results')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B4', name='TS03TC03')
    def test_reset_test_results(self):
        home_page = HomePage(self.driver)
        initial_product_list = home_page.get_product_cards()
        filtered_products = home_page.search_product('Claw Hammer')
        assert len(filtered_products) != len(initial_product_list)
        home_page.reset_search()
        reset_product_list = home_page.get_product_cards()
        assert len(reset_product_list) == len(initial_product_list)
        for i in range(0, len(reset_product_list)):
            assert reset_product_list[i]['name'] == initial_product_list[i]['name']
            assert reset_product_list[i]['img_caption'] == initial_product_list[i]['img_caption']
            assert reset_product_list[i]['price'] == initial_product_list[i]['price']
