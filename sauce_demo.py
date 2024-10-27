import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.Add_to_Cart_Page import InventoryPage  # Import InventoryPage
from Pages.Checkout_page import CheckoutPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver and open the login page
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def test_login_and_add_items(self):
        # Log in
        self.login_page.login_and_validate()

        # Add the last three items to cart and get their titles
        last_titles = self.inventory_page.add_last_three_items_to_cart()

        # Go to cart and verify items
        self.inventory_page.click_shopping_cart()
        self.inventory_page.verify_last_three_items(last_titles)

        # Complete checkout process
        self.checkout_page.click_checkout_button()
        self.checkout_page.input_information()
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
