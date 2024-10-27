from selenium.webdriver.common.by import By

from Pages.Base_Page import Page

class CheckoutPage(Page):

    CHECKOUTBUTTON = By.ID, 'checkout'
    FIRSTNAME = By.ID, 'first-name'
    LASTNAME = By.ID, 'last-name'
    POSTALCODE = By.ID, 'postal-code'
    CONTINUEBUTTON = By.ID, 'continue'
    FINISHBUTTON = By.ID, 'finish'
    TEXT = By.XPATH, "//h2[@class='complete-header']"

    def click_checkout_button(self):
        self.click(*self.CHECKOUTBUTTON)

    def input_information(self):
        self.input_text('Sadiqul', *self.FIRSTNAME)
        self.input_text('Alam', *self.LASTNAME)
        self.input_text('43144', *self.POSTALCODE)

    def click_continue(self):
        self.click(*self.CONTINUEBUTTON)

    def click_finish(self):
        self.click(*self.FINISHBUTTON)
        self.verify_partial_text('Thank', *self.TEXT)