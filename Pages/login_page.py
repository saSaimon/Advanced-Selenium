from selenium.webdriver.common.by import By
from Pages.Base_Page import Page

class LoginPage(Page):

    USERNAME = By.ID, 'user-name'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'login-button'
    TEXT = By.CSS_SELECTOR, '[class="title"]'


    def input_username(self):
        self.input_text('standard_user', *self.USERNAME)

    def input_password(self):
        self.input_text('secret_sauce', *self.PASSWORD)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)


    def validate_if_login_successful(self):
        self.verify_partial_text('Products', *self.TEXT )

    def login_and_validate(self):
        self.input_username()
        self.input_password()
        self.click_login_button()
        self.validate_if_login_successful()




