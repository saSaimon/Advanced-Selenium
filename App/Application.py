from Pages.Login_Page import LoginPage
from Pages.Home_Page import HomePage
from Pages.Content_Page import ContentPage
from Pages.Search_Page import SearchPage
from Pages.Dashboard_Page import DashboardPage
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.content_page = ContentPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)