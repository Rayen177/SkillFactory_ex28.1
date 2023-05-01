from pages.restore_password_page import RestorePasswordPage

EMAIL = 'rayen177@gmail.com'
LINK = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=3FT0po2oZ68/'
PHONE = '9250214548'

def test_restore_password_by_email(browser):
    restore_page = RestorePasswordPage(browser, LINK)
    restore_page.open()
    restore_page.restore_password_by_email(EMAIL)

def test_restore_password_by_phone(browser):
    restore_page = RestorePasswordPage(browser, LINK)
    restore_page.open()
    restore_page.restore_password_by_phone(PHONE)
