from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_correct_cart(self):
        self.store_bookname_and_price()
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_correct_name()
        self.should_be_correct_price()

    def should_see_no_success_message_after_adding_to_cart(self):
        self.add_to_cart()
        self.should_not_be_success_message()

    def should_see_no_success_message_on_product_page(self):
        self.should_not_be_success_message()

    def should_success_message_disappear(self):
        self.add_to_cart()
        self.success_message_should_disappear()

    def should_see_success_message(self):
        self.add_to_cart()
        self.should_be_success_message()

    def add_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_link.click()

    def store_bookname_and_price(self):
        bookname = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        self.bookname = bookname.text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        self.price = price.text

    def should_be_correct_name(self):
        css_name = self.browser.find_element(*ProductPageLocators.FACT_BOOK_NAME)
        assert self.bookname == css_name.text, "Incorrect Book"

    def should_be_correct_price(self):
        css_price = self.browser.find_element(*ProductPageLocators.FACT_BOOK_PRICE)
        assert self.price == css_price.text, "Incorrect Price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
