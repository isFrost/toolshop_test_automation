import pytest
import allure
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


class TestProductBrowsing:
    @allure.title('Preparation: get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC01: Open Hand Tools category')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B2', name='TS02TC01')
    def test_open_hand_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_hand_tools()
        hand_tools_page = CategoryPage(self.driver)
        assert hand_tools_page.get_category() == 'Category: Hand Tools'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC02: Open Power Tools category')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B3', name='TS02TC02')
    def test_open_power_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_power_tools()
        power_tools_page = CategoryPage(self.driver)
        assert power_tools_page.get_category() == 'Category: Power Tools'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC03: Open Other category')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B4', name='TS02TC03')
    def test_open_other_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_other_tools()
        other_tools_page = CategoryPage(self.driver)
        assert other_tools_page.get_category() == 'Category: Other'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC04: Open Special Tools category')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B5', name='TS02TC04')
    def test_open_special_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_special_tools()
        special_tools_page = CategoryPage(self.driver)
        assert special_tools_page.get_category() == 'Category: Special Tools'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC05: Navigate via pagination of product catalog')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B6', name='TS02TC05')
    def test_pagination(self):
        home_page = HomePage(self.driver)
        initial_page_products = home_page.get_product_cards()
        home_page.go_to_next_page()
        next_page_products = home_page.get_product_cards()
        i = 0
        while i < len(initial_page_products):
            assert initial_page_products[i]['name'] != next_page_products[i]['name']
            assert initial_page_products[i]['img_caption'] != next_page_products[i]['img_caption']
            assert initial_page_products[i]['price'] != next_page_products[i]['price']
            i += 1
        home_page.go_to_previous_page()
        next_page_products = home_page.get_product_cards()
        while i < len(initial_page_products):
            assert initial_page_products[i]['name'] == next_page_products[i]['name']
            assert initial_page_products[i]['img_caption'] == next_page_products[i]['img_caption']
            assert initial_page_products[i]['price'] == next_page_products[i]['price']
            i += 1

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC06: Open product page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B7', name='TS02TC06')
    def test_open_product_page(self):
        home_page = HomePage(self.driver)
        products = home_page.get_product_cards()
        selected_product = products[0]
        home_page.open_product(selected_product['name'])
        product_page = ProductPage(self.driver)
        assert product_page.get_name() == selected_product['name']
        assert product_page.get_description() is not None
        assert product_page.get_price() == selected_product['price']
        assert product_page.is_image_loaded()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC07: Open related product')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B8', name='TS02TC07')
    def test_open_related_product(self):
        home_page = HomePage(self.driver)
        products = home_page.get_product_cards()
        selected_product = products[0]
        home_page.open_product(selected_product['name'])
        product_page = ProductPage(self.driver)
        related_products = product_page.get_related_products()
        selected_related_product = related_products[0]
        product_page.open_related_product(selected_related_product['name'])
        related_product_page = ProductPage(self.driver)
        assert related_product_page.get_name() == selected_related_product['name']

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC08: Return to the main page from category')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B9', name='TS02TC08')
    def test_return_home_from_category(self):
        home_page = HomePage(self.driver)
        home_page.go_to_special_tools()
        special_tools_page = CategoryPage(self.driver)
        assert special_tools_page.get_category() == 'Category: Special Tools'
        special_tools_page.go_home()
        assert self.driver.current_url == f'{DataProvider.get_data("base_url.json")["base_url"]}/#/'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS02: Product Browsing')
    @allure.sub_suite('TC09: Return to the main page from product page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=661348406&range=B10', name='TS02TC09')
    def test_return_home_from_product(self):
        home_page = HomePage(self.driver)
        products = home_page.get_product_cards()
        selected_product = products[0]
        home_page.open_product(selected_product['name'])
        product_page = ProductPage(self.driver)
        assert product_page.get_name() == selected_product['name']
        product_page.go_home()
        assert self.driver.current_url == f'{DataProvider.get_data("base_url.json")["base_url"]}/#/'
