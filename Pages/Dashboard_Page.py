from Pages.Base_Page import Page
from selenium.webdriver.common.by import By
import time
class DashboardPage(Page):

    LibraryButton = (By.XPATH, "//span[normalize-space()='Library']")
    ExpertOutlook24 = (By.XPATH, "//span[contains(text(),'Expert Outlook 2024')]")
    Download_Button = (By.XPATH, "//span[@class='Text_normal__mZg_p Text_monoBody__8s62l']")
    UnderstandingAI = (By.CSS_SELECTOR, 'li a[href="/library/understanding-ai"]')
    Carts = (By.CSS_SELECTOR, By.CSS_SELECTOR, '[class="TaxonomyCard_cardLink__vio0M"]')

    def click_expert_outlook_24(self, context):

        self.open_url_and_verify_page_contains_url_text(context, url = 'https://www.canvas8.com/library/expert-outlook-2024')

    def click_expert_outlook_23(self, context):

        self.open_url_and_verify_page_contains_url_text(context, url = 'https://www.canvas8.com/library/expert-outlook-2023')

    def click_understandingAI(self, context):
        self.open_url_and_verify_page_contains_url_text(context, url='https://www.canvas8.com/library/understanding-ai')


    def click_emerging_subcultures(self, context):
        self.open_url_and_verify_page_contains_url_text(context, url='https://www.canvas8.com/library/emerging-subcultures')

    def click_geopolitical_conflict(self, context):
        self.open_url_and_verify_page_contains_url_text(context, url='https://www.canvas8.com/library/geopolitical-conflict')





