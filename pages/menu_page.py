import random

from selene import have, be

from locators.web_locators import WebLocators


class MenuPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.menu = self.setup_browser.element(WebLocators.menu)
        self.title_page = self.setup_browser.element(WebLocators.title_page)

    def check_menu(self, menu_title):
        self.menu.click()
        self.title_page.should(have.text(menu_title))
        return self

    def check_category(self, category):
        self.setup_browser.element(WebLocators.city_choose(category)) \
            .should(have.text(category)).click()
        return self

    def add_to_cart(self):
        buttons = self.setup_browser.elements(WebLocators.add_to_cart)

        quantity = random.choice(range(1, 5))

        for _ in range(quantity):
            buttons.click()

        return quantity

    def check_add_cart(self, menu_title, category):
        self.check_menu(menu_title)
        self.check_category(category)

        return self.add_to_cart()
