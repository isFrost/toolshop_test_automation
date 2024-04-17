import pytest
import allure
from utils.data_provider import DataProvider
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.cart_sign_in_page import CartSignInPage
from pages.cart_address_page import CartAddressPage
from pages.cart_payment_page import CartPaymentPage
from utils.login_helper import LoginHelper


class TestOrderManagement:
    @allure.title('Preparation: setup user, get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.user = DataProvider.get_data('registered_user.json')
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS05: Order Management')
    @allure.sub_suite('TC05: Validate auto population of billing details')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=495501177&range=B2', name='TS05TC01')
    def test_billing_auto_population(self):
        home_page = LoginHelper.login(self.driver, self.user)
        products = home_page.get_product_cards()
        home_page.open_product(products[2]['name'])
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.proceed_to_sign_in()
        cart_sign_in_page = CartSignInPage(self.driver)
        cart_sign_in_page.proceed()
        cart_address_page = CartAddressPage(self.driver)
        billing_info = cart_address_page.get_billing_info()
        assert billing_info['address'] == self.user['address']
        assert billing_info['city'] == self.user['city']
        assert billing_info['state'] == self.user['state']
        assert billing_info['country_code'] == self.user['country_code']
        assert billing_info['postcode'] == self.user['postcode']

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS05: Order Management')
    @allure.sub_suite('TC02: Order checkout')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=495501177&range=B3', name='TS05TC02')
    def test_order_checkout(self):
        home_page = LoginHelper.login(self.driver, self.user)
        products = home_page.get_product_cards()
        home_page.open_product(products[4]['name'])
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.proceed_to_sign_in()
        cart_sign_in_page = CartSignInPage(self.driver)
        cart_sign_in_page.proceed()
        cart_address_page = CartAddressPage(self.driver)
        cart_address_page.proceed()
        cart_payment_page = CartPaymentPage(self.driver)
        cart_payment_page.pay_with_credit_card()
        assert cart_payment_page.pay_with_credit_card() == 'Payment was successful'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS05: Order Management')
    @allure.sub_suite('TC03: Automatic removal of products after the order is confirmed')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=495501177&range=B4', name='TS05TC04')
    @pytest.mark.skip(reason='Functionality is not yet supported by the site')
    def test_remove_items_on_order_confirmation(self):
        home_page = LoginHelper.login(self.driver, self.user)
        products = home_page.get_product_cards()
        home_page.open_product(products[1]['name'])
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        product_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.proceed_to_sign_in()
        cart_sign_in_page = CartSignInPage(self.driver)
        cart_sign_in_page.proceed()
        cart_address_page = CartAddressPage(self.driver)
        cart_address_page.proceed()
        cart_payment_page = CartPaymentPage(self.driver)
        cart_payment_page.pay_with_credit_card()
        cart_payment_page.go_home()
        home_page.open_cart()
        assert cart_page.get_cart_items() is None

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS05: Order Management')
    @allure.sub_suite('TC04: Automatic invoice generation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=495501177&range=B5', name='TS05TC04')
    @pytest.mark.skip(reason='Functionality is not yet supported by the site')
    def test_invoice_generation(self):
        pass
