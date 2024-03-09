import pytest
from utils.data_provider import DataProvider
from pages.home_page import HomePage


class TestProductSearch:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_search_by_product(self):
        home_page = HomePage(self.driver)
        filtered_products = home_page.search_product('Claw Hammer')
        for product in filtered_products:
            assert 'Claw Hammer' in product['name']

    def test_search_non_existing_product(self):
        home_page = HomePage(self.driver)
        filtered_products = home_page.search_product('Non-Existing Product 1111')
        assert len(filtered_products) == 0

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
