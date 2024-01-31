from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, url):
        """ Navigate to a specified URL. """
        self.driver.get(url)

    def find_element(self, *locator):
        """ Find a single element by a locator tuple (By, value). """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element not found with locator: {locator}")
            return None

    def find_elements(self, *locator):
        """ Find multiple elements by a locator tuple (By, value). """
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            print(f"Elements not found with locator: {locator}")
            return []

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_click(self, *locator):
        """ Click on an element identified by a locator tuple. """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            print(f"Element not clickable with locator: {locator}")

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def verify_text(self, expected_text, *locator):
        """ Verify if the element text matches the expected text. """
        element = self.find_element(*locator)
        if element:
            actual_text = element.text
            assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        """ Verify if the element text contains the expected partial text. """
        element = self.find_element(*locator)
        if element:
            actual_text = element.text
            assert expected_partial_text in actual_text, f'Expected partial text "{expected_partial_text}" not found in "{actual_text}"'

    def wait_for_element(self, *locator):
        """ Wait for an element to be present in the DOM. """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element not found in DOM with locator: {locator}")
            return None

    def select_dropdown_by_value(self, *locator, value):
        """ Select a value from a dropdown list. """
        element = self.find_element(*locator)
        if element:
            select = Select(element)
            select.select_by_value(value)

    def switch_to_frame(self, locator):
        """ Switch to an iframe using its locator. """
        frame = self.wait_for_element(locator)
        if frame:
            self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """ Switch back to the main document from an iframe. """
        self.driver.switch_to.default_content()

    def handle_alert(self, accept=True):
        """ Handle a JavaScript alert. """
        try:
            alert = self.wait.until(EC.alert_is_present())
            if accept:
                alert.accept()
            else:
                alert.dismiss()
        except TimeoutException:
            print("No alert present.")

    def switch_to_window(self, window_number):
        """ Switch to a different window or tab. """
        windows = self.driver.window_handles
        if len(windows) > window_number:
            self.driver.switch_to.window(windows[window_number])
        else:
            print(f"Window number {window_number} not available.")

    def scroll_into_view(self, locator):
        """ Scroll the page until an element is in view. """
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def perform_drag_and_drop(self, *source_locator, target_locator):
        """ Perform a drag-and-drop action from one element to another. """
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        if source_element and target_element:
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def switch_to_previous_window(self):
        """ Switch to the previous window or tab. """
        all_windows = self.driver.window_handles
        if len(all_windows) > 1:
            # Switch to the second-to-last handle in the list, which is the previous window
            self.driver.switch_to.window(all_windows[-2])
        else:
            print("No previous window or tab found.")

    def send_keys(self, *locator, keys):
        """ Send keys to a specific element. """
        element = self.find_element(*locator)
        if element:
            element.send_keys(keys)

    def key_down(self, key, element=None):
        """ Simulate pressing a key down. """
        action = ActionChains(self.driver)
        if element:
            action.key_down(key, element)
        else:
            action.key_down(key).perform()

    def key_up(self, key, element=None):
        """ Simulate releasing a key. """
        action = ActionChains(self.driver)
        if element:
            action.key_up(key, element)
        else:
            action.key_up(key).perform()

    def send_keys_to_body(self, keys):
        """ Send keys to the body of the page. """
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(keys)

    def press_enter(self, *locator):
        """ Press the ENTER key on a specific element. """
        self.send_keys(locator, Keys.ENTER)

    def press_escape(self, *locator):
        """ Press the ESCAPE key on a specific element. """
        self.send_keys(*locator, Keys.ESCAPE)

    def press_tab(self, *locator):
        """ Press the TAB key on a specific element. """
        self.send_keys(locator, Keys.TAB)

    def scroll_down(self, amount):
        """ Scroll down the page by a specified amount. """
        self.driver.execute_script(f"window.scrollBy(0, {amount});")

    def scroll_up(self, amount):
        """ Scroll up the page by a specified amount. """
        self.driver.execute_script(f"window.scrollBy(0, -{amount});")

    def right_click(self, *locator):
        """ Right-click on an element identified by a locator. """
        element = self.find_element(*locator)
        if element:
            ActionChains(self.driver).context_click(element).perform()
        else:
            print("Element not found for right-click.")

    def double_click(self, *locator):
        """ Double-click on an element identified by a locator. """
        element = self.find_element(*locator)
        if element:
            ActionChains(self.driver).double_click(element).perform()
        else:
            print("Element not found for double-click.")




    def single_click(self, *locator):
        """ Single click on an element identified by a locator. """
        self.click(*locator)  # Reusing the existing click method.

    def wait_and_click(self, *locator):
        """ Wait for an element to be clickable and then click it. """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def scroll_into_view_and_click(self, *locator):
        """ Scroll the element into view and then click it. """
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def javascript_click(self, *locator):
        """ Use JavaScript to click on an element. """
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def move_to_element_and_click(self, *locator):
        """ Use ActionChains to move to an element and then click it. """
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def hover_the_element(self, *locator):
        """ Hover over an element identified by a locator. """
        element = self.find_element(*locator)
        if element:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        else:
            print(f"Element not found with locator: {locator}")

    def assert_element_text_not_empty(self, *locator, context):
        """ Asserts that the text of the element identified by the locator is not empty. """
        try:
            element = self.driver.find_element(*locator)
            text = element.text.strip()
            assert text, f"Text of element with locator {locator} is empty."
            # self.logger.info(f"Text found in element with locator {locator}: {text}")
        except NoSuchElementException as e:
            # self.logger.error(f"Element with locator {locator} not found: {e}")
            pass  # Optionally, handle the exception here.
        except AssertionError as ae:
            context.logger.error(f"Assertion failed: {ae}")

    def assert_no_error_message(self, *locator, context):
        """ Asserts that there is no element with a specific class indicating an error. """
        try:
            element = self.driver.find_element(*locator).text
            assert '404' not in element, "Error element found on the page."
            # self.logger.info("No error element found on the page.")
        except NoSuchElementException as e:
            # self.logger.info("Test Passed: No error element found on the page.")
            pass  # Optionally, handle the exception here.
        # except AssertionError as ae:
        #     context.logger.error(f"Assertion failed: {ae}")
        #     # context.logger.error(f"Error on page {self.driver.current_url}")

    def verify_api_call_status_code(self, context, url, expected_status_code=200):
        # Access the request via driver.requests after the driver has made the API call
        for request in self.driver.requests:
            if request.response and request.url == url:
                # Check if the status code of the response matches the expected status code
                if request.response.status_code == expected_status_code:
                    context.logger.info(f'API call to {url} returned status code {expected_status_code}')
                    return True
                else:
                    context.logger.error(
                        f'API call to {url} returned status code {request.response.status_code}, expected {expected_status_code}')
                    return False
        context.logger.warning(f'No API call made to {url} or the call has not completed yet.')
        return False

    def url_slicing(self, url):


        # Split the URL by slashes and take the last part
        parts = url.split('/')
        last_part = parts[-1]

        # Replace hyphens with spaces to get the final string
        extracted_string = last_part.replace('-', ' ')

        return extracted_string

    def open_url_and_verify_page_contains_url_text(self, context, url):

        self.driver.get(url)
        current_url = self.driver.current_url
        total_carts = len(self.driver.find_elements(By.CSS_SELECTOR, '[class="TaxonomyCard_cardLink__vio0M"]'))
        context.logger.info(f'This page contains {total_carts} articles.')

        try:

            page_source = context.driver.page_source.lower()
            assert self.url_slicing(current_url) in page_source, 'Text not found in the page.'
            self.verify_api_call_status_code(context, url='https://services-prod.canvas8.com/content/cms', expected_status_code=200)

        except AssertionError as ae:
            context.logger.error(f"Assertion failed: {ae}")
            # Log the current URL as error if there is an issue
            context.logger.error(f"Error encountered at URL: {current_url}")



