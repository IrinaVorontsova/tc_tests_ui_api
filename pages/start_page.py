from selene import have, be

from constants.read_env import ReadEnv
from locators.web_locators import WebLocators


class StartPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.main_logo = self.setup_browser.element(WebLocators.main_logo)
        self.other_city = self.setup_browser.element(WebLocators.city_other)
        self.city_check = self.setup_browser.element(WebLocators.city_check)
        self.title_page = self.setup_browser.element(WebLocators.title_page)
        self.menu = self.setup_browser.element(WebLocators.menu)
        self.delivery = self.setup_browser.element(WebLocators.delivery)
        self.promos = self.setup_browser.element(WebLocators.promos)
        self.news = self.setup_browser.element(WebLocators.news)
        self.addresses = self.setup_browser.element(WebLocators.addresses)
        self.banquets = self.setup_browser.element(WebLocators.banquets)
        self.vacancies = self.setup_browser.element(WebLocators.vacancies)
        self.franchise = self.setup_browser.element(WebLocators.franchise)
        self.home_cooking = self.setup_browser.element(WebLocators.home_cooking)
        self.cooking_title = self.setup_browser.element(WebLocators.cooking_title)

    def open_browser(self, URL):
        self.setup_browser.open(URL)
        return self

    def check_logo(self, main_page):
        self.setup_browser.should(have.title(main_page))
        return self

    def choose_city(self, city):
        self.other_city.click()
        self.setup_browser.element(WebLocators.city_choose(city))\
            .should(have.text(city)).click()
        self.city_check.should(have.text(city))
        return self

    def check_menu(self, menu_title):
        self.menu.click()
        self.title_page.should(have.text(menu_title))
        return self

    def check_delivery(self, delivery_title):
        self.delivery.click()
        self.title_page.should(have.text(delivery_title))
        return self

    def check_promos(self, promos_title):
        self.promos.click()
        self.title_page.should(have.text(promos_title))
        return self

    def check_news(self, news_title):
        self.news.click()
        self.title_page.should(have.text(news_title))
        return self

    def check_addresses(self, addresses_title):
        self.addresses.click()
        self.title_page.should(have.text(addresses_title))
        return self

    def check_banquets(self):
        self.banquets.click()

    def check_vacancies(self):
        self.vacancies.click()

    def check_franchise(self):
        self.franchise.click()

    def check_home_cooking(self, cooking):
        self.home_cooking.click()
        self.cooking_title.should(have.text(cooking))
        return self

    def check_tabs(self, main_page, city, menu_title, delivery_title):
        self.check_logo(main_page)
        self.choose_city(city)
        self.check_menu(menu_title)
        self.check_delivery(delivery_title)
        # self.check_promos()
        # self.check_news()
        # self.check_addresses()
        # self.check_banquets()
        # self.check_vacancies()
        # self.check_franchise()
        # self.check_home_cooking()
        return self

    # def check_page(self, vk_header):
    #     self.vk_header.should(have.text(vk_header))
    #
    # def get_login(self, login):
    #     self.login.should(be.blank).type(login)
    #
    # def check_box_click(self):
    #     self.check_box.click()
    #
    # def exit_click(self):
    #     self.exit.click()
    #
    # def enter_password(self, check_password):
    #     self.enter_password.should(have.text(check_password))
    #     self.enter_password.click()
    #
    # def get_password(self, password):
    #     self.password.should(be.blank).type(password)
    #
    # def click_continue(self):
    #     self.continue_.click()
    #
    # def authorization(self, vk_header, authorization, check_password):
    #     self.check_page(vk_header)
    #     self.get_login(authorization.login)
    #     self.check_box_click()
    #     self.exit_click()
    #     self.enter_password(check_password)
    #     self.get_password(authorization.password)
    #     self.click_continue()
    #     return self
