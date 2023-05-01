from time import sleep
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import AuthByCodePageLocators

class AuthByCodePage(BasePage):
    def auth_by_code_phone(self, phone):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(AuthByCodePageLocators.EMAIL_PHONE_FIELD)).send_keys(phone)
        sleep(20)
        self.browser.find_element(*AuthByCodePageLocators.BUTTON_RECEIVE_CODE).click()
        assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(AuthByCodePageLocators.CONFIRM_CODE_NEW_WINDOW)).text == 'Код подтверждения отправлен', 'User is not registered using temporary code'

    def go_to_auth_page_from_auth_by_code_page(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(AuthByCodePageLocators.BUTTON_AUTH_PAGE)).click()
        assert 'authenticate' in self.browser.current_url, 'Auth page does not load'