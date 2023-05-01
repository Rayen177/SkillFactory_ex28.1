from selenium.common import NoSuchElementException, TimeoutException
from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):

    def registration_with_phone(self, name, lastname, phone, password):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_FIELD)).send_keys(name)
        self.browser.find_element(*RegistrationPageLocators.LASTNAME_FIELD).send_keys(lastname)
        self.browser.find_element(*RegistrationPageLocators.REGION_FIELD).click()
        self.browser.find_element(*RegistrationPageLocators.REGION_NAME).click()
        self.browser.find_element(*RegistrationPageLocators.PHONE_EMAIL_FIELD).send_keys(phone)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.REGISTR_BUTTON).click()
        assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(RegistrationPageLocators.CONFIRM_CODE_NEW_WINDOW)).text == 'Подтверждение телефона', 'User is not registrated'

    def registration_password_field_fail(self, password):
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_FIELD).click()

        try:
            self.browser.find_element(*RegistrationPageLocators.ERROR_MESSAGE_FIELD)

        except NoSuchElementException:
            assert False, 'The provided password correct but should not be'
        assert True

    def registration_name_field_fail(self, name):
        self.browser.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(name)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_FIELD).click()

        try:
            self.browser.find_element(*RegistrationPageLocators.ERROR_MESSAGE_FIELD)

        except NoSuchElementException:
            assert False, 'The provided name correct but should not be'
        assert True

    def registration_name_field_pass(self, name):
        self.browser.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(name)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_FIELD).click()

        try:
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE_FIELD))

        except TimeoutException:
            assert False, 'The provided name incorrect'
        assert True
