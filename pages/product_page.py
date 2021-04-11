from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_correct_cart(self):
        self.store_bookname_and_price()
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_correct_name()
        self.should_be_correct_price()

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
