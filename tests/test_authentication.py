import pytest
from pages.register_page import RegisterPage
from utils.driver_manager import DriverManager
from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.profile_page import ProfilePage


@pytest.fixture(scope='function')
def setup_teardown():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()


class TestAuthentication:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.user = DataProvider.get_data('user.json')
        self.user['email'] = f'{DataProvider.get_timestamp()}@mailinator.com'
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    def test_register(self):
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.go_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_user(self.user)
        login_page.go_home()
        home_page.go_to_signin_page()
        login_page.login(self.user['email'], self.user['password'])
        account_page = AccountPage(self.driver)
        account_page.open_profile()
        profile_page = ProfilePage(self.driver)
        profile_data = profile_page.get_profile_data()
        assert profile_data['first_name'] == self.user['first_name']
        assert profile_data['last_name'] == self.user['last_name']
        assert profile_data['email'] == self.user['email']
        assert profile_data['phone'] == self.user['phone']
        assert profile_data['address'] == self.user['address']
        assert profile_data['city'] == self.user['city']
        assert profile_data['state'] == self.user['state']
        assert profile_data['country'] == self.user['country_code']
        DataProvider.set_data('registered_user.json', self.user)

    def test_login(self):
        self.user = DataProvider.get_data('registered_user.json')
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.login(self.user['email'], self.user['password'])
        account_page = AccountPage(self.driver)
        account_page.open_profile()
        profile_page = ProfilePage(self.driver)
        profile_data = profile_page.get_profile_data()
        assert profile_data['first_name'] == self.user['first_name']
        assert profile_data['last_name'] == self.user['last_name']
        assert profile_data['email'] == self.user['email']
        assert profile_data['phone'] == self.user['phone']
        assert profile_data['address'] == self.user['address']
        assert profile_data['city'] == self.user['city']
        assert profile_data['state'] == self.user['state']
        assert profile_data['country'] == self.user['country_code']

    def test_logout(self):
        self.user = DataProvider.get_data('registered_user.json')
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.login(self.user['email'], self.user['password'])
        account_page = AccountPage(self.driver)
        account_page.open_profile()
        profile_page = ProfilePage(self.driver)
        profile_data = profile_page.get_profile_data()
        assert profile_data['email'] == self.user['email']
        profile_page.logout()
        assert login_page.get_form_title() == 'Login'
        assert login_page.get_current_user() is None

    def test_register_with_invalid_inout(self):
        self.user = DataProvider.get_data('invalid_user_data.json')
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.go_to_register_page()
        register_page = RegisterPage(self.driver)
        register_page.register_user(self.user)
        errors = register_page.get_errors()
        assert errors.get('first_name_error') == 'First name is required.'
        assert errors.get('last_name_error') == 'Last name is required.'
        assert errors.get('birth_date_error') == 'Date of Birth is required.'
        assert errors.get('address_error') == 'Address is required.'
        assert errors.get('postcode_error') == 'Postcode is required.'
        assert errors.get('city_error') == 'City is required.'
        assert errors.get('state_error') == 'State is required.'
        assert errors.get('country_error') == 'Country is required.'
        assert errors.get('phone_error') == 'Only numbers are allowed.'
        assert errors.get('email_error') == 'E-mail format is invalid.'
        assert errors.get('password_error') == 'Password is required.'

    def test_login_non_existing_user(self):
        self.user = DataProvider.get_data('registered_user.json')
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.login('non_existing_user1111@mailinator.com', self.user['password'])
        assert login_page.get_error() == 'Invalid email or password'

    def test_login_with_invalid_password(self):
        self.user = DataProvider.get_data('registered_user.json')
        home_page = HomePage(self.driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(self.driver)
        login_page.login(self.user['email'], 'invalid_password!')
        assert login_page.get_error() == 'Invalid email or password'
