from selenium.common import NoSuchElementException, TimeoutException
from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage(BasePage):
    def should_be_left_right_blocks_on_auth_page(self):
        left_block = self.is_element_exist(AuthPageLocators.LEFT_SIDE)
        right_block = self.is_element_exist(AuthPageLocators.RIGHT_SIDE)
        tab_phone = self.is_element_exist(AuthPageLocators.TAB_PHONE)
        tab_mail = self.is_element_exist(AuthPageLocators.TAB_MAIL)
        tab_login = self.is_element_exist(AuthPageLocators.TAB_LOGIN)
        tab_ls = self.is_element_exist(AuthPageLocators.TAB_LS)
        assert self.browser.find_element(*AuthPageLocators.AUTH_TEXT).text == 'Авторизация' and \
               tab_phone and tab_mail and tab_login and tab_ls, 'Auth block on auth page has issue'
        assert self.is_element_exist(AuthPageLocators.LOGO_ROSTELECOM), 'LOGO ROSTELECOM absent'
        assert left_block and right_block, 'LEFT or RIGHT block of auth page doesn\'t exist'

    def auth_by_phone_pass(self, phone, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_PHONE)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(phone)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()
        assert WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(AuthPageLocators.LOGO_ACCOUNT)), 'User is not authorized'

    def auth_by_phone_fail(self, phone, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_PHONE)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(phone)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()

        try:
            self.browser.find_element(*AuthPageLocators.INCORRECT_PHONE_NUMBER)

        except NoSuchElementException:
            assert False, 'Provided the correct format of phone number but should not be'

        assert self.browser.find_element(*AuthPageLocators.INCORRECT_PHONE_NUMBER).text == 'Введите номер телефона' \
               or self.browser.find_element(*AuthPageLocators.INCORRECT_PHONE_NUMBER).text == 'Неверный формат телефона'

    def auth_by_password_fail(self, phone, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_PHONE)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(phone)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()
        assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(AuthPageLocators.INCORRECT_DATA)).text == 'Неверный логин или пароль', 'Provided password correct but should not be'

    def auth_by_email_pass(self, email, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_MAIL)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(email)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()
        assert WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(AuthPageLocators.LOGO_ACCOUNT)), 'User is not authorized by email'

    def auth_by_email_fail(self, email, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_MAIL)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(email)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()

        try:
            WebDriverWait(self.browser, 10).until_not(
                EC.presence_of_element_located(AuthPageLocators.TAB_MAIL_ACTIVE))

        except TimeoutException:
            assert False, 'The provided email is correct but should be not'
        assert True

    def auth_by_login_pass(self, login, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_LOGIN)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(login)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()

        assert WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            AuthPageLocators.LOGO_ACCOUNT)), 'User is not authorized by login'

    def go_to_registration_page(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.REGISTRATION_LINK)).click()
        assert 'registration' in self.browser.current_url, 'Registration form is not load'

    def go_to_agreement(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.AGREEMENT_LINK)).click()
        win_1 = self.browser.window_handles[1]
        self.browser.switch_to.window(win_1)
        assert 'agreement' in self.browser.current_url, 'Agreement doc is not load'

    def go_to_social_nets(self, text_net, social_net_locator):
        WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable(social_net_locator)).click()
        assert text_net in self.browser.current_url, f'The link to social net {text_net} doesn\'t work'

    def auth_with_unregistered_phone(self, unreg_phone, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(AuthPageLocators.TAB_PHONE)).click()
        self.browser.find_element(*AuthPageLocators.PHONE_FIELD).send_keys(unreg_phone)
        self.browser.find_element(*AuthPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(*AuthPageLocators.BUTTON_SUBMIT).click()

        try:
            assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                AuthPageLocators.INCORRECT_DATA))
        except NoSuchElementException:
            assert False, 'The authorization for unregistered phone impossible'
        assert True
