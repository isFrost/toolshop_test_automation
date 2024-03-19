import pytest
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestFiltering:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def verify_filtered_products_tags(self, catalog_page, products, tags, condition='one'):
        for product in products:
            catalog_page.open_product(product['name'], new_tab=True)
            product_page = ProductPage(self.driver)
            if condition == 'one':
                assert any(tag in product_page.get_tags() for tag in tags)
            elif condition == 'both':
                assert all(tag in product_page.get_tags() for tag in tags)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def test_filter_by_single_category(self):
        category = 'Hammer'
        home_page = HomePage(self.driver)
        home_page.filter_products(category)
        products = home_page.get_product_cards()
        self.verify_filtered_products_tags(home_page, products, category)
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            self.verify_filtered_products_tags(home_page, products, category)

    def test_filer_by_single_brand(self):
        brand = 'ForgeFlex Tools'
        home_page = HomePage(self.driver)
        home_page.filter_products(brand)
        products = home_page.get_product_cards()
        self.verify_filtered_products_tags(home_page, products, brand)
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            self.verify_filtered_products_tags(home_page, products, brand)

    def test_filter_by_multiple_brands(self):
        brands = ['ForgeFlex Tools', 'MightyCraft Hardware']
        home_page = HomePage(self.driver)
        home_page.filter_products(brands[0])
        home_page.filter_products(brands[1])
        products = home_page.get_product_cards()
        self.verify_filtered_products_tags(home_page, products, brands)
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            self.verify_filtered_products_tags(home_page, products, brands)

    def test_filter_by_brand_and_category(self):
        tags =['Wrench ', 'ForgeFlex Tools']
        home_page = HomePage(self.driver)
        home_page.filter_products(tags[0])
        home_page.filter_products(tags[1])
        products = home_page.get_product_cards()
        self.verify_filtered_products_tags(home_page, products, tags)
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            self.verify_filtered_products_tags(home_page, products, tags)

    def test_filter_by_price_below_60(self):
        home_page = HomePage(self.driver)
        home_page.set_max_price(60)
        products = home_page.get_product_cards()
        for product in products:
            assert float(product['price'][1:]) <= 60.0
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            for product in products:
                assert float(product['price'][1:]) <= 60.0

    def test_filter_by_price_between_60_and_120(self):
        home_page = HomePage(self.driver)
        home_page.set_max_price(120)
        home_page.set_min_price(60)
        products = home_page.get_product_cards()
        for product in products:
            assert 60.0 <= float(product['price'][1:]) <= 120.0
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            for product in products:
                assert 60.0 <= float(product['price'][1:]) <= 120.0

    def test_filter_by_price_above_120(self):
        home_page = HomePage(self.driver)
        home_page.set_max_price(200)
        home_page.set_min_price(120)
        products = home_page.get_product_cards()
        for product in products:
            assert float(product['price'][1:]) >= 120.0
        while home_page.has_next():
            home_page.go_to_next_page()
            products = home_page.get_product_cards()
            for product in products:
                assert float(product['price'][1:]) <= 120.0
