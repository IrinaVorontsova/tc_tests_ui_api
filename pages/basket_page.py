from selene import have, be

from locators.web_locators import WebLocators


class BasketPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.main_logo = self.setup_browser.element(WebLocators.main_logo)
        self.city_spb = self.setup_browser.element(WebLocators.city_spb)