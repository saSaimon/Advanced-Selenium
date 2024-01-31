from behave import then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

ALL_ARTICLES = (By.CSS_SELECTOR, '[class="SearchResult_searchResult__r_A_s"]')


@then('Scroll down {n} times')
def scroll(context, n):
    actions = ActionChains(context.driver)
    amount_of_scroll = int(n)

    # Perform scroll down action
    for i in range(amount_of_scroll):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)  # Sleep to allow the page to load

    articles = context.driver.find_elements(*ALL_ARTICLES)
    context.logger.info(f"Number of articles found after scrolling {n} times: {len(articles)}")


@then('User click on the {topic}')
def filter_by_topic(context, topic):
    context.app.search_page.filter_by_topic(topic=topic)

