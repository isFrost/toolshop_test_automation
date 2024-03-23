import datetime
import pytest
from utils.data_provider import DataProvider
from utils.login_helper import LoginHelper
from pages.contact_page import ContactPage


class TestOrderManagement:
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.user = DataProvider.get_data('registered_user.json')
        self.driver.get(DataProvider.get_data('base_url.json')['base_url'])
        self.driver.maximize_window()

    @pytest.mark.skip(reason='auto test is not ready - manual test fails, no contact message can be sent')
    def test_send_message(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.go_to_contact_form()
        contact_page = ContactPage(self.driver)
        subject = 'Customer service'
        message = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.' \
                  + str(datetime.datetime.now())
        contact_page.send_message(subject, message)

    @pytest.mark.skip(reason='auto test is not ready - manual test fails, no contact message can be sent')
    def test_send_message_with_attachment(self):
        pass

    def test_message_size_validation(self):
        home_page = LoginHelper.login(self.driver, self.user)
        home_page.go_to_contact_form()
        contact_page = ContactPage(self.driver)
        subject = 'Customer service'
        message = 'Short message' + str(datetime.datetime.now())
        contact_page.send_message(subject, message)
        assert 'Message must be minimal 50 characters' in contact_page.get_message_validation_error()
        message = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been ' \
                  'the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of ' \
                  'type and scrambled it to make a type specimen book.' + str(datetime.datetime.now())
        contact_page.send_message(subject, message)
        assert 'The message field must not be greater than 250 characters.' in contact_page.get_send_validation_error()

    @pytest.mark.skip(reason='auto test is not ready - manual test fails, no contact message can be sent')
    def test_reply_to_message(self):
        pass
