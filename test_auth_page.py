import pytest
from pages.auth_page import AuthPage
from pages.locators import AuthPageLocators

LINK = 'https://b2c.passport.rt.ru'
PHONE = '925-021-45-48'
PASSWORD = 'TestTest77'
EMAIL = 'rayen177@gmail.com'
LOGIN = 'test_user'
UNREG_PHONE = '9260254744'

@pytest.mark.smoke
# Проверка расположения элементов на странице авторизации
def test_left_right_blocks_on_auth_page(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.should_be_left_right_blocks_on_auth_page()

# проверка авторизации используя правильные номер телефона\пароль
def test_auth_by_phone_pass(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.auth_by_phone_pass(PHONE, PASSWORD)

@pytest.mark.parametrize('phone_incorrect', ('', '925-021-45-4'))
# негативная проверка авторизации с неправильным номером телефона
def test_auth_by_phone_fail(browser, phone_incorrect):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.auth_by_phone_fail(phone_incorrect, PASSWORD)

@pytest.mark.parametrize('pass_incorrect', ('Примерпароля', 'Rhtvybq', 'rhtvybq22', 'rzWvu2SolwBVxrAT2QUejFH2ySCFPtI70z2A8TTIu6k0s6FQ4SNU8uWeSsq4XUrUIflGjFEDxIWLJv8r5zu4JITfMlKt4XNEFLEMOO56qxZsWSsEXOzxqo1DIyG8AfeOE9OMu3K7zBHPfp0zs5jksb6PZA0WOUYRIoEhKGmjNY7iPqabFa6GUKlRj5zPD09hPkewu8cYQrgiabvZgcQBTNv3Ta7MvtUgbxvnAzajJ2Z9TZn6tYVSSZWhO3lxnTLv'))
# негативная проверка авторизации по номеру телефона с неправильным паролем
def test_auth_by_password_fail(browser, pass_incorrect):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.auth_by_password_fail(PHONE, pass_incorrect)

# проверка авторизации по адресу почты
def test_auth_by_email_pass(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()

    # первый вариант - использовать уже сущ функцию для телефона. Т.к. система рапознает почту и автоматически переключает на таб почта
    # auth_page.auth_by_phone_pass(EMAIL, PASSWORD)

    # или другой вариант, когда мы выбирает таб почта и потом вводим данные
    auth_page.auth_by_email_pass(EMAIL, PASSWORD)

@pytest.mark.parametrize('email_incorrect', ('rayen177gmail.com', 'rayen177@gmail'))
# негативная проверка авторизации с неправильным адресом почты
def test_auth_by_email_fail(browser, email_incorrect):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()

    auth_page.auth_by_email_fail(email_incorrect, PASSWORD)

# проверка авторизации по логину
def test_auth_by_login_pass(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()

    # первый вариант - использовать уже сущ функцию для телефона. Т.к. система рапознает логин и автоматически переключает на таб логин
    # auth_page.auth_by_phone_pass(LOGIN, PASSWORD)

    # или другой вариант, когда мы выбираем таб логин и потом вводим данные
    auth_page.auth_by_login_pass(LOGIN, PASSWORD)

# проверка перехода на страницу регистрации нового польователя со страницы авторизации
def test_go_to_registration_page(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.go_to_registration_page()

# проверка возможности открыть пользовательского соглашения со страницы авторизации
def test_go_to_agreement(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.go_to_agreement()

# проверка возможности перейти в соц сети со страницы авторизации
@pytest.mark.parametrize('social_net', (('vk', AuthPageLocators.VK_LINK), ('ok.ru', AuthPageLocators.OD_LINK),
                                        ('mail', AuthPageLocators.MAIL_LINK), ('google', AuthPageLocators.GOOGLE_LINK),
                                        ('yandex', AuthPageLocators.YA_LINK)))
def test_go_to_social_nets(browser, social_net):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.go_to_social_nets(*social_net)

# проверка возможности авторизоваться с незарегистрированным телефоном
def test_auth_with_unregistered_phone(browser):
    auth_page = AuthPage(browser, LINK)
    auth_page.open()
    auth_page.auth_with_unregistered_phone(UNREG_PHONE, PASSWORD)
