import time
import pytest
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.rentals_page import RentalsPage
from pages.rental_page import RentalPage
from pages.cart_page import CartPage


class TestProductSearch:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_open_rentals_category(self):
        home_page = HomePage(self.driver)
        home_page.go_to_rentals()
        rentals_page = RentalsPage(self.driver)
        assert rentals_page.get_header() == 'Rentals'

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

