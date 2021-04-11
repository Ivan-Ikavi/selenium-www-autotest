from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-primary")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    FACT_BOOK_NAME = (By.CSS_SELECTOR, "#messages div.alert-success strong")
    FACT_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
