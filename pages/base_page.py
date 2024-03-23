from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    # Locators
    HOME_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[1]/a')
    SIGN_IN_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[4]/a')
    CONTACT_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[3]/a')
    CATEGORY_DROPDOWN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/a')
    HAND_TOOLS_CAT = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/ul/li[1]/a')
    POWER_TOOLS_CAT = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/ul/li[2]/a')
    OTHER_TOOLS_CAT = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/ul/li[3]/a')
    SPECIAL_TOOLS_CAT = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/ul/li[4]/a')
    RENTALS_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[2]/ul/li[6]/a')
    USER_MENU = (By.CSS_SELECTOR, '#menu')
    SIGN_OUT_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[4]/ul/li[7]/a')
    CART_BTN = (By.XPATH, '/html/body/app-root/app-header/nav/div/div/ul/li[5]/a')
    CART_ICON = (By.XPATH, '//*[@id="lblCartCount"]')
    MESSAGES_MENU_ITEM = (By.CSS_SELECTOR, 'ul.show > li:nth-child(5) > a:nth-child(1)')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=5):
        """ Method waits for the element to be visible """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def wait_for_elements(self, locator, timeout=5):
        """ Method waits for all located elements to be visible """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def wait_for_element_to_be_clickable(self, locator, timeout=5):
        """ Method waits for the element to be clickable """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def wait_until_value_updated(self, locator, timeout=5):
        """ Waits until the value of the element is updated """
        element = self.wait_for_element(locator)
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: element.get_attribute('value') != '')
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def wait_for_url_to_change(self, timeout=5):
        """ Waits until current URL is changed """
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(self.driver.current_url))
        except TimeoutException as e:
            print(f'Error: {e}')  # TODO: Add proper logging for errors and info messages

    def go_to_signin_page(self):
        """ Open login page """
        sign_in_btn = self.wait_for_element(self.SIGN_IN_BTN)
        sign_in_btn.click()

    def go_home(self):
        """ Return to Home page """
        home_btn = self.wait_for_element(self.HOME_BTN)
        home_btn.click()

    def go_to_contact_form(self):
        """ Open contact form """
        contact_btn = self.wait_for_element(self.CONTACT_BTN)
        contact_btn.click()

    def expand_category_dropdown(self):
        """ Expand dropdown menu of site categories """
        categories_dropdown = self.wait_for_element(self.CATEGORY_DROPDOWN)
        categories_dropdown.click()

    def go_to_hand_tools(self):
        """ Open Hand Tools category """
        self.expand_category_dropdown()
        hand_tools_btn = self.wait_for_element(self.HAND_TOOLS_CAT)
        hand_tools_btn.click()

    def go_to_power_tools(self):
        """ Open Power Tools category """
        self.expand_category_dropdown()
        power_tools_btn = self.wait_for_element(self.POWER_TOOLS_CAT)
        power_tools_btn.click()

    def go_to_other_tools(self):
        """ Open Other category """
        self.expand_category_dropdown()
        other_tools_btn = self.wait_for_element(self.OTHER_TOOLS_CAT)
        other_tools_btn.click()

    def go_to_special_tools(self):
        """ Open Special Tools category """
        self.expand_category_dropdown()
        special_tools_btn = self.wait_for_element(self.SPECIAL_TOOLS_CAT)
        special_tools_btn.click()

    def go_to_rentals(self):
        """ Open Rentals category """
        self.expand_category_dropdown()
        rentals_btn = self.wait_for_element(self.RENTALS_BTN)
        rentals_btn.click()

    def expand_user_menu(self):
        """ Expand menu under user name """
        user_menu = self.wait_for_element(self.USER_MENU)
        user_menu.click()

    def open_user_messages(self):
        """ Open user messages """
        self.expand_user_menu()
        message_item = self.wait_for_element(self.MESSAGES_MENU_ITEM)
        message_item.click()

    def get_current_user(self):
        """ Get the name of user that is currently logged into the site """
        user_menu = self.wait_for_element(self.USER_MENU)
        return user_menu.text if user_menu else None

    def logout(self):
        """ Logout user from the site """
        self.expand_user_menu()
        sign_out_btn = self.wait_for_element_to_be_clickable(self.SIGN_OUT_BTN)
        sign_out_btn.click()

    def cart_quantity_from_icon(self):
        """ Return the quantity of products displayed at cart icon """
        cart_count = self.wait_for_element(self.CART_ICON)
        return cart_count.text

    def open_cart(self):
        """ Open shopping cart """
        cart_btn = self.wait_for_element(self.CART_BTN)
        cart_btn.click()
