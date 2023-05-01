from pages.auth_by_code_page import AuthByCodePage

PHONE = '905-588-48-35'
LINK = 'https://lk.rt.ru/'

def test_auth_by_code_phone(browser):
    auth_code = AuthByCodePage(browser, LINK)
    auth_code.open()
    auth_code.auth_by_code_phone(PHONE)

def test_go_to_auth_page_from_auth_by_code_page(browser):
    auth_code = AuthByCodePage(browser, LINK)
    auth_code.open()
    auth_code.go_to_auth_page_from_auth_by_code_page()


