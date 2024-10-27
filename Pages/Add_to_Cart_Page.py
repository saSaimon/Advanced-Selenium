from selenium.webdriver.common.by import By
from Pages.Base_Page import Page

class InventoryPage(Page):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[normalize-space(text())='Add to cart']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[class="btn btn_secondary btn_small btn_inventory "]')
    SHOPPING_CART = (By.CSS_SELECTOR, 'shopping_cart_container')

    def add_last_three_items_to_cart(self):

        items = self.find_elements(*self.INVENTORY_ITEMS)
        count = 0
        for i in range(len(items) - 3, len(items)):
            count = count+1
            add_to_cart_button = items[i].find_element(*self.ADD_TO_CART_BUTTON)
            add_to_cart_button.click()

        remove_buttons = self.find_elements(*self.REMOVE_BUTTON)
        assert len(remove_buttons) == count

    def click_shopping_cart(self):

        self.open_url('https://www.saucedemo.com/cart.html')
