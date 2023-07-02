import random

from selene import have

from locators.web_locators import WebLocators


class MenuPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.menu = self.setup_browser.element(WebLocators.menu)
        self.title_page = self.setup_browser.element(WebLocators.title_page)
        self.button = self.setup_browser.element(WebLocators.add_to_cart)
        self.quantity = self.setup_browser.element(WebLocators.quantity_cart)
        self.remove = self.setup_browser.element(WebLocators.remove)

    def check_menu(self, menu_title):
        self.menu.click()
        self.title_page.should(have.text(menu_title))
        return self

    def check_category(self, category):
        self.setup_browser.element(WebLocators.category_choose(category)) \
            .should(have.text(category.upper())).click()
        return self

    def add_to_cart(self):
        quantity = random.choice(range(1, 5))

        for _ in range(quantity):
            self.button.click()

        return str(quantity)

    def check_quantity(self):
        self.quantity.should(have.text(self.add_to_cart()))
        return self

    def remove_dish(self):
        self.quantity.click()

        if self.remove.locate():
            self.remove.click()

        return self

    def check_add_cart(self, menu_data):
        self.check_menu(menu_data.menu_title)
        self.check_category(menu_data.category)
        self.check_quantity()
        self.remove_dish()

