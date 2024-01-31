import time

from behave import given, then
from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('CANVAS8_USER')
password = os.environ.get('CANVAS8_PASS')

@given('User can enter to the {website}')
def enter_into_website(context, website):
    try:
        context.app.login_page.enter_to_website(url=website)
        context.logger.info(f"Entered into website: {website}")
    except Exception as e:
        context.logger.error(f"Error entering website {website}: {e}")
        raise


@given('User can login')
def login_to_canvas8(context):
    try:
        context.app.login_page.sign_in(username, password)
        # context.logger.info("User logged in successfully")
    except Exception as e:
        context.logger.error(f"Login failed: {e}")
        raise
    time.sleep(5)


@then('Verify Home link is present')
def home_text_is_present(context):
    try:
        context.app.home_page.verify_home_text_present()
        context.logger.info("Verified Home link is present")
    except AssertionError as e:
        context.logger.error(f"Home link verification failed: {e}")
        raise
    except Exception as e:
        context.logger.error(f"Error in verifying Home link: {e}")
        raise
