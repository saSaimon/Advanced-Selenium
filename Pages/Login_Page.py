from selenium.webdriver.common.by import By
from Pages.Base_Page import Page


class LoginPage(Page):
    ACCEPT_BUTTON = (By.CSS_SELECTOR, '[id="hs-eu-confirmation-button"]')
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, '[class="Text_lighter__LoWNB Text_body__coL65"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def enter_to_website(self, url):
        self.open_url(url)

    def sign_in(self, email, password):
        self.click(*self.ACCEPT_BUTTON)
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.REMEMBER_ME_CHECKBOX)
        self.click(*self.LOGIN_BUTTON)
