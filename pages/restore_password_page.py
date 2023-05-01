from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import RestorePasswordPageLocators


class RestorePasswordPage(BasePage):
    def restore_password_by_email(self, email):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(RestorePasswordPageLocators.EMAIL_PHONE_FIELD)).send_keys(email)
        self.browser.find_element(*RestorePasswordPageLocators.BUTTON_RESET).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(RestorePasswordPageLocators.RADIO_BUTTON_EMAIL)).click()
        self.browser.find_element(*RestorePasswordPageLocators.BUTTON_SUBMIT).click()
        assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(RestorePasswordPageLocators.AUTH_TEXT)).text == 'Восстановление пароля', 'Password can\'t be restored with email'

    def restore_password_by_phone(self, phone):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(RestorePasswordPageLocators.EMAIL_PHONE_FIELD)).send_keys(phone)
        self.browser.find_element(*RestorePasswordPageLocators.BUTTON_RESET).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(RestorePasswordPageLocators.RADIO_BUTTON_PHONE)).click()
        self.browser.find_element(*RestorePasswordPageLocators.BUTTON_SUBMIT).click()
        assert WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(RestorePasswordPageLocators.AUTH_TEXT)).text == 'Восстановление пароля', 'Password can\'t be restored with phone'