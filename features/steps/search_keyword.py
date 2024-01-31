from behave import then


@then('User will input search {keyword}')
def search_by_keyword(context, keyword):
    context.app.search_page.search_by_keyword(keyword)


@then('User will enter From Date {from_month} {from_year}')
def search_by_from_date(context, from_month, from_year):
    context.app.search_page.select_from_year(from_year)
    context.app.search_page.select_date_from(from_month)


@then('User will enter To Date {to_month} {to_year}')
def search_by_to_date(context, to_month, to_year):
    context.app.search_page.select_date_to(to_month)
    context.app.search_page.select_to_year(to_year)
