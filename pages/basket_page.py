from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_correct_basket(self):
        self.should_be_empty_basket()
        self.should_be_correct_message("Your basket is empty.")

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PURCHASE), \
            "Success message is presented, but should not be"

    def should_be_correct_message(self, msg):
        assert msg == self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
