from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.get(self.link)

    def is_element_exist(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator))
        except NoSuchElementException:
            return False

        return True

    def get_link(self, locator):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()
        return self.browser.current_url