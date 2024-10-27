import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.Add_to_Cart_Page import InventoryPage  # Import InventoryPage
from Pages.Checkout_page import CheckoutPage


class TestECommerceFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver and open the login page once for the entire test case
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.saucedemo.com/')
        cls.login_page = LoginPage(cls.driver)
        cls.inventory_page = InventoryPage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)

    def test_1_login(self):
        # Log in
        self.login_page.login_and_validate()

    def test_2_add_items_to_cart(self):
        # Add the last three items to the cart and get their titles
        self.last_titles = self.inventory_page.add_last_three_items_to_cart()

        # Go to cart and verify items
        self.inventory_page.click_shopping_cart()
        self.inventory_page.verify_last_three_items(self.last_titles)

    def test_3_complete_checkout(self):
        # Complete the checkout process
        self.checkout_page.click_checkout_button()
        self.checkout_page.input_information()
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()

    @classmethod
    def tearDownClass(cls):
        # Quit the driver once after all tests are done
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
