import time

from Pages.Base_Page import Page
from selenium.webdriver.common.by import By


class ContentPage(Page):
    HEADING_TEXT = (By.CSS_SELECTOR, '[class="Text_normal__mZg_p Text_h2__l9odo"]')
    ALL_ARTICLES = (By.CSS_SELECTOR, '[class="SearchResult_searchResult__r_A_s"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[class="Text_normal__mZg_p Text_small__nIJNE"]')

    def heading_is_not_empty(self):
        self.assert_element_text_not_empty(*self.HEADING_TEXT, context=self)

    def test_article_has_no_error(self, context):
        elements = self.find_elements(*self.ALL_ARTICLES)

        for i in range(len(elements)):
            # Store the original window handle (main window)
            original_window = self.driver.current_window_handle

            # Assuming clicking the element opens a new tab
            time.sleep(2)
            elements[i].click()
            time.sleep(2)  # Wait for the new tab to open

            # Switch to the new tab (assuming it's the last one opened)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Perform your checks here
            current_url = self.driver.current_url
            context.logger.info(f"Visiting URL: {current_url}")

            # Perform your checks here
            try:
                self.assert_no_error_message(*self.ERROR_MESSAGE, context=context)
            except AssertionError as ae:
                context.logger.error(f"Assertion failed: {ae}")
                # Log the current URL as error if there is an issue
                context.logger.error(f"Error encountered at URL: {current_url}")

            # Close the current tab
            self.driver.close()

            # Switch back to the original window (main window)
            self.driver.switch_to.window(original_window)
