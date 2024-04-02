import time
import pytest
import allure
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.rentals_page import RentalsPage
from pages.rental_page import RentalPage
from pages.cart_page import CartPage


class TestProductSearch:
    @allure.title('Preparation: get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS06: Rentals')
    @allure.sub_suite('TC01: Open Rentals category')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=2026889523&range=B2', name='TS06TC01')
    def test_open_rentals_category(self):
        home_page = HomePage(self.driver)
        home_page.go_to_rentals()
        rentals_page = RentalsPage(self.driver)
        assert rentals_page.get_header() == 'Rentals'

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS06: Rentals')
    @allure.sub_suite('TC02: Open Rentals position')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=2026889523&range=B3', name='TS06TC02')
    def test_open_rentals_position(self):
        home_page = HomePage(self.driver)
        home_page.go_to_rentals()
        rentals_page = RentalsPage(self.driver)
        rental = rentals_page.get_rentals()[0]
        rentals_page.open_rental(rental['name'])
        rental_page = RentalPage(self.driver)
        assert rental_page.get_name() == rental['name']
        assert rental_page.get_description() is not None
        assert rental_page.is_image_loaded()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS06: Rentals')
    @allure.sub_suite('TC03: Add rental to the cart')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=2026889523&range=B4', name='TS06TC03')
    def test_add_rentals_position_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.go_to_rentals()
        rentals_page = RentalsPage(self.driver)
        rental = rentals_page.get_rentals()[0]
        rentals_page.open_rental(rental['name'])
        rental_page = RentalPage(self.driver)
        rental_page.set_duration(3)
        unit_price = rental_page.get_unit_price()
        total_price = rental_page.get_total_price()
        assert unit_price * 3 == total_price
        rental_page.add_to_cart()
        rental_page.open_cart()
        cart_page = CartPage(self.driver)
        time.sleep(3)    # TODO: replace with proper wait
        cart_item = cart_page.get_cart_items()[0]
        assert cart_item['name'] == rental['name']
        assert int(cart_item['quantity']) == 3
        assert float(cart_item['price'][1:]) == unit_price
        assert float(cart_item['total'][1:]) == total_price

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS06: Rentals')
    @allure.sub_suite('TC04: Remove rental from the cart')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=2026889523&range=B5', name='TS06TC04')
    def test_remove_rentals_position_from_cart(self):
        home_page = HomePage(self.driver)
        home_page.go_to_rentals()
        rentals_page = RentalsPage(self.driver)
        rental = rentals_page.get_rentals()[0]
        rentals_page.open_rental(rental['name'])
        rental_page = RentalPage(self.driver)
        rental_page.set_duration(5)
        rental_page.add_to_cart()
        rental_page.open_cart()
        cart_page = CartPage(self.driver)
        time.sleep(3)  # TODO: replace with proper wait
        cart_item = cart_page.get_cart_items()[0]
        assert cart_item['name'] == rental['name']
        cart_page.remove_item(rental['name'])
        time.sleep(3)  # TODO: replace with proper wait
        assert cart_page.get_cart_items() is None
