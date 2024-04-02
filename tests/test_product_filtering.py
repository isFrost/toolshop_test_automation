import pytest
import allure
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestFiltering:
    @allure.title('Preparation: get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def verify_filtered_products_tags(self, catalog_page, products, tags, condition='one'):
        """ Open products form provided product list verify that they have  provided tags"""
        for product in products:
            catalog_page.open_product(product['name'], new_tab=True)
            product_page = ProductPage(self.driver)
            if condition == 'one':
                assert any(tag in product_page.get_tags() for tag in tags)
            elif condition == 'both':
                assert all(tag in product_page.get_tags() for tag in tags)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC04: Filter product: select products from one category')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B5', name='TS03TC04')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC05: Filter products: select products from one brand')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B6', name='TS03TC05')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC06: Filter product: select product from multiple brands')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B7', name='TS03TC06')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC07: Filter products: select product of one category and one brand')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B8', name='TS03TC07')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC08: Filter products by price range: below 60$')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B9', name='TS03TC08')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC09: Filter products by price range: from 60$ to 120$')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B10', name='TS03TC09')
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

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS03: Product Search and Filter')
    @allure.sub_suite('TC10: Filter products by price range: above 120$')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=298515700&range=B11', name='TS03TC10')
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
