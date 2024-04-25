import pytest
import allure
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCartManagement:
    @allure.title('Preparation: setup user, get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS04: Cart Management')
    @allure.sub_suite('TC01: Add products to the cart ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/view#gid'
                 '=704316921&range=B2', name='TS04TC01')
    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        product = home_page.get_product_cards()[2]
        home_page.open_product(product['name'])
        product_page = ProductPage(self.driver)
        product_page.increase_quantity()
        product_page.add_to_cart()
        assert product_page.cart_quantity_from_icon() == '2'
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        items = cart_page.get_cart_items()
        assert items[0]['name'] == product['name']
        assert items[0]['quantity'] == '2'
        assert items[0]['price'] == product['price']
        assert items[0]['total'] == f'${round(float(product["price"][1:]) * 2, 2)}'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS04: Cart Management')
    @allure.sub_suite('TC02: Remove product from the cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/view#gid'
                 '=704316921&range=B3', name='TS04TC02')
    def test_remove_product_from_cart(self):
        home_page = HomePage(self.driver)
        product = home_page.get_product_cards()[6]
        home_page.open_product(product['name'])
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        assert product_page.cart_quantity_from_icon() == '1'
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        items = cart_page.get_cart_items()
        assert items[0]['name'] == product['name']
        cart_page.remove_item(product['name'])
        items = cart_page.get_cart_items()
        assert items is None

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS04: Cart Management')
    @allure.sub_suite('TC03: Change product quantity in the cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/view#gid'
                 '=704316921&range=B4', name='TS04TC03')
    def test_change_product_quantity(self):
        home_page = HomePage(self.driver)
        product = home_page.get_product_cards()[5]
        home_page.open_product(product['name'])
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        assert product_page.cart_quantity_from_icon() == '1'
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        items = cart_page.get_cart_items()
        assert items[0]['name'] == product['name']
        assert items[0]['quantity'] == '1'
        assert items[0]['price'] == product['price']
        assert items[0]['total'] == product['price']
        cart_page.set_item_quantity(product['name'], 3)
        cart_page.wait_for_total_to_update(product['name'], items[0]['total'])
        items = cart_page.get_cart_items()
        assert items[0]['quantity'] == '3'
        assert items[0]['total'] == f'${round(float(product["price"][1:]) * 3, 2)}'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS04: Cart Management')
    @allure.sub_suite('TC04: Attempt to add out of stock product to the cart')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/view#gid'
                 '=704316921&range=B5', name='TS04TC04')
    def test_add_out_of_stock_product(self):
        home_page = HomePage(self.driver)
        product = home_page.get_product_cards()[3]
        home_page.open_product(product['name'])
        product_page = ProductPage(self.driver)
        assert product_page.add_to_cart_disabled()
