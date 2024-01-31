from behave import given, then
import time
@given('Test Expert Outlook 2024')
def test_expert_outlook_2024(context):
    context.app.dashboard_page.click_expert_outlook_24(context)


@then('Test Expert Outlook 2023')
def test_export_outlook_2023(context):
    context.app.dashboard_page.click_expert_outlook_23(context)


@then('Test Understanding AI')
def test_understaning_ai(context):
    context.app.dashboard_page. click_understandingAI(context)

@then('Test Emarging SubCultures')
def test_emarging_subculture(context):
    context.app.dashboard_page.click_emerging_subcultures(context)


@then('Test Geopolitical Conflict')
def test_geopolitical_conflict(context):
    context.app.dashboard_page.click_geopolitical_conflict(context)

