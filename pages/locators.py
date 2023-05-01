from selenium.webdriver.common.by import By

class AuthPageLocators:
    LEFT_SIDE = (By.ID, 'page-left')
    RIGHT_SIDE = (By.ID, 'page-right')
    AUTH_TEXT = (By.CLASS_NAME, 'card-container__title')
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_MAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')
    LOGO_ROSTELECOM = (By.CLASS_NAME, 'rt-logo.what-is-container__logo')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input#username')
    PASS_FIELD = (By.CSS_SELECTOR, 'input#password')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button#kc-login')
    LOGO_ACCOUNT = (By.XPATH, '//*[@class ="rt-base-icon rt-base-icon--fill-path"]')
    INCORRECT_PHONE_NUMBER = (By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')
    INCORRECT_DATA = (By.XPATH, '//*[@data-error="Неверный логин или пароль"]')
    TAB_MAIL_ACTIVE = (By.CSS_SELECTOR, 'div#t-btn-tab-mail.rt-tab.rt-tab--small.rt-tab--active')
    REGISTRATION_LINK = (By.ID, 'kc-register')
    AGREEMENT_LINK = (By.XPATH, '//*[@href="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"]')
    VK_LINK = (By.ID, 'oidc_vk')
    OD_LINK = (By.ID, 'oidc_ok')
    MAIL_LINK = (By.ID, 'oidc_mail')
    GOOGLE_LINK = (By.ID, 'oidc_google')
    YA_LINK = (By.ID, 'oidc_ya')

class RegistrationPageLocators:
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LASTNAME_FIELD = (By.CSS_SELECTOR, 'input[name="lastName"]')
    REGION_FIELD = (By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']")
    REGION_NAME = (By.XPATH, '//div[11]') # Брянская обл
    PHONE_EMAIL_FIELD = (By.CSS_SELECTOR, 'input#address')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input#password')
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, 'input#password-confirm')
    REGISTR_BUTTON = (By.CSS_SELECTOR, 'button[name="register"]')
    CONFIRM_CODE_NEW_WINDOW = (By.XPATH, '//div[@class="card-container__wrapper"]//h1[@class="card-container__title"]')
    ERROR_MESSAGE_FIELD = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')

class AuthByCodePageLocators:
    EMAIL_PHONE_FIELD = (By.ID, 'address')
    BUTTON_RECEIVE_CODE = (By.ID, 'otp_get_code')
    CONFIRM_CODE_NEW_WINDOW = (By.XPATH, '//div[@class="card-container__wrapper"]//h1[@class="card-container__title"]')
    BUTTON_AUTH_PAGE = (By.ID, 'standard_auth_btn')

class RestorePasswordPageLocators:
    EMAIL_PHONE_FIELD = (By.CSS_SELECTOR, 'input#username')
    BUTTON_RESET = (By.ID, 'reset')
    RADIO_BUTTON_EMAIL = (By.XPATH, '//*[text()="По e-mail"]')
    RADIO_BUTTON_PHONE = (By.XPATH, '//*[text()="По номеру телефона"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded reset-choice-form__reset-btn"]')
    AUTH_TEXT = (By.CLASS_NAME, 'card-container__title')
