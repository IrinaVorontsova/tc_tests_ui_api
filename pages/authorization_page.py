from selene import have, be

from constants.read_env import ReadEnv
from locators.web_locators import WebLocators


class AuthorizationPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.vk_header = self.setup_browser.element(WebLocators.exit_vk_text)
        self.login = self.setup_browser.element(WebLocators.exit_vk_text)
        self.check_box = self.setup_browser.element(WebLocators.check_box)
        self.exit = self.setup_browser.element(WebLocators.exit)
        self.enter_password = self.setup_browser.element(WebLocators.enter_password)
        self.password = self.setup_browser.element(WebLocators.password)
        self.continue_ = self.setup_browser.element(WebLocators.continue_)

    def open_browser(self, URL):
        self.setup_browser.open(URL)
        return self

    def check_page(self, vk_header):
        self.vk_header.should(have.text(vk_header))

    def get_login(self, login):
        self.login.should(be.blank).type(login)

    def check_box_click(self):
        self.check_box.click()

    def exit_click(self):
        self.exit.click()

    def enter_password(self, check_password):
        self.enter_password.should(have.text(check_password))
        self.enter_password.click()

    def get_password(self, password):
        self.password.should(be.blank).type(password)

    def click_continue(self):
        self.continue_.click()

    def authorization(self, vk_header, authorization, check_password):
        self.check_page(vk_header)
        self.get_login(authorization.login)
        self.check_box_click()
        self.exit_click()
        self.enter_password(check_password)
        self.get_password(authorization.password)
        self.click_continue()
        return self
