import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.Base_Page import Page


class SearchPage(Page):
    SELECT_FROM_MONTH = (By.NAME, "search-filters-from-months")
    SELECT_FROM_YEAR = (By.NAME, "search-filters-from-years")

    SELECT_TO_MONTH = (By.NAME, "search-filters-to-months")
    SELECT_TO_YEAR = (By.NAME, "search-filters-to-years")

    SEARCH = (By.CLASS_NAME, "SearchInput_searchInput__l7gKe")

    TOPICS = (By.CSS_SELECTOR, '[class="Text_lighter__LoWNB Text_small__nIJNE"]')

    def select_date_from(self, from_month):
        self.click(*self.SELECT_FROM_MONTH)
        self.select_dropdown_by_value(*self.SELECT_FROM_MONTH, value=from_month)

    def select_from_year(self, from_year):
        self.click(*self.SELECT_FROM_YEAR)
        self.select_dropdown_by_value(*self.SELECT_FROM_YEAR, value=from_year)

    def select_date_to(self, to_month):
        self.click(*self.SELECT_TO_MONTH)
        self.select_dropdown_by_value(*self.SELECT_TO_MONTH, value=to_month)

    def select_to_year(self, to_year):
        self.click(*self.SELECT_TO_YEAR)
        self.select_dropdown_by_value(*self.SELECT_TO_YEAR, value=to_year)

    def search_by_keyword(self, keyword):
        search_field = self.driver.find_element(*self.SEARCH)
        search_field.clear()
        search_field.send_keys(keyword)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def filter_by_topic(self, topic):
        topics = self.find_elements(*self.TOPICS)

        for i in range(len(topics)):
            text = topics[i].text

            if topic in text:
                topics[i].click()
                break







