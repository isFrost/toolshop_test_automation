import pytest
from utils.driver_manager import DriverManager
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.fixture(scope='function')
def setup_teardown():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()


class TestCartManagement:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

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
        cart_page.wait_for_total_to_update(product['name'], items[0]['total'])
        items = cart_page.get_cart_items()
        assert items is None

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

    def test_add_out_of_stock_product(self):
        home_page = HomePage(self.driver)
        product = home_page.get_product_cards()[3]
        home_page.open_product(product['name'])
        product_page = ProductPage(self.driver)
        assert product_page.add_to_cart_disabled()
