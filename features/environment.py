import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
from App.Application import Application
from selenium.webdriver.support.wait import WebDriverWait
from Logger.logging_config import setup_logging
import logging
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/bestsellers.feature


def browser_init(context, browser_name, headless):

    """
    :param context: Behave context
    """
    logging.getLogger('seleniumwire').setLevel(logging.WARNING)

    seleniumwire_options = {
        'port': 12345  # Specify an unused port here
    }
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)



    """with chrome"""
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

    """new chrome driver calling option"""
    # context.driver = webdriver.Chrome()


    # driver_path = GeckoDriverManager().install()  # Use GeckoDriverManager for Firefox
    # context.driver = webdriver.Firefox(executable_path=driver_path)  # Use Firefox WebDriver here

    """### OTHER BROWSERS ###"""
    context.browser_name = browser_name
    if browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, seleniumwire_options=seleniumwire_options, options=firefox_options)


    elif browser_name == 'safari':
        context.driver = webdriver.Safari()


    elif browser_name == 'edge':
        edge_options = EdgeOptions()
        if headless:
            edge_options.add_argument("--headless")
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        context.driver = webdriver.Edge(service=service, seleniumwire_options=seleniumwire_options, options=edge_options)


    else:  # Defaults to Chrome if no match
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, seleniumwire_options=seleniumwire_options, options=chrome_options)



    """### HEADLESS MODE ####"""
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    #
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    # """### BROWSERSTACK ###"""
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    """with selenium grid"""
    # hub_url = 'http://192.168.0.101:4444/wd/hub'
    #
    # if browser_name.lower() == 'firefox':
    #     options = FirefoxOptions()
    # elif browser_name.lower() == 'edge':
    #     options = EdgeOptions()
    # else:  # Default to Chrome
    #     options = ChromeOptions()
    #
    # if headless:
    #     options.add_argument('--headless')
    #
    # context.driver = webdriver.Remote(
    #     command_executor=hub_url, seleniumwire_options=seleniumwire_options,
    #     options=options
    # )

    context.logger = setup_logging()
    context.driver.maximize_window()
    # context.driver.set_window_size(2024, 200200)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)



# Other setup code...





def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_name = os.getenv('BROWSER', 'chrome')  # Default to Chrome if not specified
    headless_mode = os.getenv('HEADLESS', 'false').lower() == 'true'
    browser_init(context, browser_name, headless_mode)
    starting_message = f"Started scenario in {context.browser_name}:  {scenario.name}"
    context.logger.info(starting_message)

    print(starting_message)


def before_step(context, step):
    before_message = f"Started step: {step}"
    context.logger.info(before_message)
    print(before_message)


def after_step(context, step):
    if step.status == 'failed':
        failure_message = f"Step failed in {context.browser_name}: {step.name}"
        context.logger.error(failure_message)
        print('\nStep failed: ', failure_message)
    elif step.status  == 'passed':
        context.logger.info(f'Step passed: {step.name}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
