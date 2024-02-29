import time
import pytest
from utils.driver_manager import DriverManager
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture(scope='function')
def setup_teardown():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()


class TestProductBrowsing:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_open_hand_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_hand_tools()
        hand_tools_page = CategoryPage(self.driver)
        assert hand_tools_page.get_category() == 'Category: Hand Tools'

    def test_open_power_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_power_tools()
        power_tools_page = CategoryPage(self.driver)
        assert power_tools_page.get_category() == 'Category: Power Tools'

    def test_open_other_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_other_tools()
        other_tools_page = CategoryPage(self.driver)
        assert other_tools_page.get_category() == 'Category: Other'

    def test_open_special_tools(self):
        home_page = HomePage(self.driver)
        home_page.go_to_special_tools()
        special_tools_page = CategoryPage(self.driver)
        assert special_tools_page.get_category() == 'Category: Special Tools'

    def test_pagination(self):
        home_page = HomePage(self.driver)
        initial_page_products = home_page.get_product_cards()
        home_page.go_to_next_page()
        time.sleep(3)    # TODO: replace with proper wait
        next_page_products = home_page.get_product_cards()
        i = 0
        while i < len(initial_page_products):
            assert initial_page_products[i]['name'] != next_page_products[i]['name']
            assert initial_page_products[i]['img_caption'] != next_page_products[i]['img_caption']
            assert initial_page_products[i]['price'] != next_page_products[i]['price']
            i += 1
        home_page.go_to_previous_page()
        time.sleep(3)    # TODO: replace with proper wait
        next_page_products = home_page.get_product_cards()
        while i < len(initial_page_products):
            assert initial_page_products[i]['name'] == next_page_products[i]['name']
            assert initial_page_products[i]['img_caption'] == next_page_products[i]['img_caption']
            assert initial_page_products[i]['price'] == next_page_products[i]['price']
            i += 1

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

    def test_return_home_from_category(self):
        home_page = HomePage(self.driver)
        home_page.go_to_special_tools()
        special_tools_page = CategoryPage(self.driver)
        assert special_tools_page.get_category() == 'Category: Special Tools'
        special_tools_page.go_home()
        assert self.driver.current_url == f'{DataProvider.get_data("base_url.json")["base_url"]}/#/'

    def test_return_home_from_product(self):
        home_page = HomePage(self.driver)
        products = home_page.get_product_cards()
        selected_product = products[0]
        home_page.open_product(selected_product['name'])
        product_page = ProductPage(self.driver)
        assert product_page.get_name() == selected_product['name']
        product_page.go_home()
        assert self.driver.current_url == f'{DataProvider.get_data("base_url.json")["base_url"]}/#/'
