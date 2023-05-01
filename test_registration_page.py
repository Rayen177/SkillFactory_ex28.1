import pytest
from pages.registration_page import RegistrationPage
from pages.locators import AuthPageLocators
from pages.base_page import BasePage
LINK = 'https://b2c.passport.rt.ru'
NAME = 'Александр'
LASTNAME = 'Невский'
PHONE = '9250214549'
PASSWORD = 'TestTest77'

def test_registration_with_phone(browser):
    base_page = BasePage(browser, LINK)
    base_page.open()
    link = base_page.get_link(AuthPageLocators.REGISTRATION_LINK)

    regist_page = RegistrationPage(browser, link)
    regist_page.registration_with_phone(NAME, LASTNAME, PHONE, PASSWORD)

@pytest.mark.parametrize('incorrect_password', ('Eghtsym', 'eghtsymb', 'восемьси', 'the_lenght_of_pasSwor'))
def test_registration_password_field_fail(browser, incorrect_password):
    base_page = BasePage(browser, LINK)
    base_page.open()
    link = base_page.get_link(AuthPageLocators.REGISTRATION_LINK)

    regist_page = RegistrationPage(browser, link)
    regist_page.registration_password_field_fail(incorrect_password)

@pytest.mark.parametrize('incorrect_name', ('fF', 'п', 'здесьРовноТридцатьСимволоввовот'))
def test_registration_name_field_fail(browser, incorrect_name):
    base_page = BasePage(browser, LINK)
    base_page.open()
    link = base_page.get_link(AuthPageLocators.REGISTRATION_LINK)

    regist_page = RegistrationPage(browser, link)
    regist_page.registration_name_field_fail(incorrect_name)

@pytest.mark.parametrize('correct_name', ('Пу', '--', 'здесьРовноТридцатьСимволоввово'))
def test_registration_name_field_pass(browser, correct_name):
    base_page = BasePage(browser, LINK)
    base_page.open()
    link = base_page.get_link(AuthPageLocators.REGISTRATION_LINK)

    regist_page = RegistrationPage(browser, link)
    regist_page.registration_name_field_pass(correct_name)
