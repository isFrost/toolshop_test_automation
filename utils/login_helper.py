from utils.data_provider import DataProvider
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from pages.profile_page import ProfilePage


class LoginHelper:
    @staticmethod
    def login(driver, user):
        """ Method checks if able to sign in as the provided user if not registers a new one """
        home_page = HomePage(driver)
        home_page.go_to_signin_page()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])
        if login_page.get_error():
            driver.refresh()
            login_page.go_to_register_page()
            user['email'] = f'{DataProvider.get_timestamp()}@mailinator.com'
            register_page = RegisterPage(driver)
            register_page.register_user(user)
            login_page.go_home()
            home_page.go_to_signin_page()
            login_page.login(user['email'], user['password'])
            DataProvider.set_data('registered_user.json', user)
        account_page = AccountPage(driver)
        account_page.open_profile()
        profile_page = ProfilePage(driver)
        profile_page.go_home()
        return home_page
