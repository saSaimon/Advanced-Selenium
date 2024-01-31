from behave import then


@then('User can see the content related to the subject')
def content_page_is_loading(context):
    try:
        context.app.content_page.heading_is_not_empty()
        context.logger.info("Content page loaded with subject-related content")
    except AssertionError as e:
        context.logger.error(f"Content page heading is empty: {e}")
        raise


@then('Test all articles have content')
def every_article_has_content(context):
    try:
        context.app.content_page.test_article_has_no_error(context)
        context.logger.info("All articles have content")
    except AssertionError as e:
        context.logger.error(f"An article without content found: {e}")
        raise
