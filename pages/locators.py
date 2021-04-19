from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    FACT_BOOK_NAME = (By.CSS_SELECTOR, "#messages div.alert-success strong")
    FACT_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
