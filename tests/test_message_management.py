import datetime
import pytest
import allure
from utils.data_provider import DataProvider
from utils.login_helper import LoginHelper
from pages.contact_page import ContactPage


class TestOrderManagement:
    @allure.title('Preparation: setup user, get URL, open browser')
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.user = DataProvider.get_data('registered_user.json')
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS08: Message Management')
    @allure.sub_suite('TC01: Send a new message')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=1588930122&range=B2', name='TS08TC01')
    @pytest.mark.skip(reason='Auto test is not ready - manual test fails, contact message can not be sent')
    def test_send_message(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.go_to_contact_form()
        contact_page = ContactPage(self.driver)
        subject = 'Customer service'
        message = f'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ' \
                  f'{str(datetime.datetime.now())}'
        contact_page.send_message(subject, message)

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS08: Message Management')
    @allure.sub_suite('TC02: Send a new message with attachment')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=1588930122&range=B3', name='TS08TC02')
    @pytest.mark.skip(reason='Auto test is not ready - manual test fails, contact message can not be sent')
    def test_send_message_with_attachment(self):
        pass

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS08: Message Management')
    @allure.sub_suite('TC03: Message size validation')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=1588930122&range=B4', name='TS08TC03')
    def test_message_size_validation(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.go_to_contact_form()
        contact_page = ContactPage(self.driver)
        subject = 'Customer service'
        message = f'Short message {str(datetime.datetime.now())}'
        contact_page.send_message(subject, message)
        assert 'Message must be minimal 50 characters' in contact_page.get_message_validation_error()
        message = f'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been ' \
                  f'the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of ' \
                  f'type and scrambled it to make a type specimen book. {str(datetime.datetime.now())}'
        contact_page.send_message(subject, message)
        assert 'The message field must not be greater than 250 characters.' in contact_page.get_send_validation_error()

    @allure.parent_suite('Test Tools Shop')
    @allure.suite('TS08: Message Management')
    @allure.sub_suite('TC04: Reply to message')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link('https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit#gid'
                 '=1588930122&range=B5', name='TS08TC04')
    @pytest.mark.skip(reason='Auto test is not ready - manual test fails, contact message can not be sent')
    def test_reply_to_message(self):
        pass
