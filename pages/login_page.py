from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self,):
        login, password = str(time.time()) + "@fakemail.com", "wierdP@SS"
        self.input_string(*LoginPageLocators.EMAIL, login)
        self.input_string(*LoginPageLocators.PASSWORD_1, password)
        self.input_string(*LoginPageLocators.PASSWORD_2, password)
        self.button_click(*LoginPageLocators.SUBMIT_REGISTRATION)

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect URL name: no \"login\" in the URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Registration from is not presented"
