from Pages.Base_Page import Page
from selenium.webdriver.common.by import By


class HomePage(Page):
    HOME_LINK = (By.CSS_SELECTOR, '#__next > div > footer > div > ul > li:nth-child(1) > a')

    def verify_home_text_present(self):
        self.verify_text('Home', *self.HOME_LINK)
