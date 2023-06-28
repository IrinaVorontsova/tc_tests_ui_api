from selene import have, be
from selenium.common import NoSuchWindowException

from constants.read_env import ReadEnv
from locators.web_locators import WebLocators
from utils.switch_to_window import SwitchToWindow


class StartPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.ddos = self.setup_browser.element(WebLocators.ddos)
        self.main_logo = self.setup_browser.element(WebLocators.main_logo)
        self.city_spb = self.setup_browser.element(WebLocators.city_spb)
        self.city_ok = self.setup_browser.element(WebLocators.city_yes)
        self.city_check = self.setup_browser.element(WebLocators.city_check)
        self.title_page = self.setup_browser.element(WebLocators.title_page)
        self.menu = self.setup_browser.element(WebLocators.menu)
        self.delivery = self.setup_browser.element(WebLocators.delivery)
        self.promos = self.setup_browser.element(WebLocators.promos)
        self.news = self.setup_browser.element(WebLocators.news)
        self.addresses = self.setup_browser.element(WebLocators.addresses)
        self.banquets = self.setup_browser.element(WebLocators.banquets)
        self.banquet = self.setup_browser.element(WebLocators.banquet)
        self.vacancies = self.setup_browser.element(WebLocators.vacancies)
        self.franchise = self.setup_browser.element(WebLocators.franchise)
        self.home_cooking = self.setup_browser.element(WebLocators.home_cooking)
        self.cooking_title = self.setup_browser.element(WebLocators.cooking_title)

    def open_browser(self, URL):
        self.setup_browser.open(URL)
        return self

    def check_logo(self, main_page):
        try:
            self.setup_browser.should(have.title(main_page))
        except:
            self.setup_browser.should(have.title("DDoS-Guard"))
            self.ddos.click()
            self.setup_browser.should(have.title(main_page))
        return self

    def choose_city(self, city):
        self.city_spb.click()
        self.setup_browser.element(WebLocators.city_choose(city))\
            .should(have.text(city)).click()
        self.city_check.should(have.text(city))
        return self

    def choose_city_other(self, city):
        self.city_check.click()
        self.setup_browser.element(WebLocators.city_choose(city)) \
            .should(have.text(city)).click()
        self.city_ok.click()
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

    def check_promos(self, promos_url):
        self.promos.click()
        self.setup_browser.should(have.url_containing(promos_url))
        return self

    def check_news(self, news_title):
        self.news.click()
        self.title_page.should(have.text(news_title))
        return self

    def check_addresses(self, addresses_title):
        self.addresses.click()
        self.title_page.should(have.text(addresses_title))
        return self

    def check_banquets(self, banquet):
        try:
            SwitchToWindow.switch_to_windows_selene(setup_browser=self.setup_browser, element=self.banquets, text=banquet)
        except NoSuchWindowException:
            self.open_browser(ReadEnv.URL)
            self.choose_city(ReadEnv.SPB)

    def check_vacancies(self, vacantion):
        try:
            SwitchToWindow.switch_to_windows_selene(setup_browser=self.setup_browser, element=self.vacancies,
                                                    text=vacantion)
        except NoSuchWindowException:
            self.open_browser(ReadEnv.URL)
            self.choose_city(ReadEnv.SPB)

    def check_franchise(self, franchise):
        try:
            SwitchToWindow.switch_to_windows_selene(setup_browser=self.setup_browser, element=self.franchise,
                                                    text=franchise)
        except NoSuchWindowException:
            self.open_browser(ReadEnv.URL)
            self.choose_city(ReadEnv.SPB)

    def check_home_cooking(self, cooking):
        self.home_cooking.click()
        self.cooking_title.should(have.text(cooking))
        return self

    def check_main_tabs_spb(self, main_tabs_spb):
        self.check_logo(main_tabs_spb.main_page)
        self.choose_city(main_tabs_spb.city)
        self.check_menu(main_tabs_spb.menu_title)
        self.check_delivery(main_tabs_spb.delivery_title)
        self.check_promos(main_tabs_spb.promos_url)
        self.check_news(main_tabs_spb.news_title)
        self.check_addresses(main_tabs_spb.addresses_title)
        self.check_home_cooking(main_tabs_spb.cooking)
        return self

    def check_other_window_tabs(self, tabs_new_window):
        self.check_banquets(tabs_new_window.banquet)
        self.check_vacancies(tabs_new_window.vacantion)
        self.check_franchise(tabs_new_window.franchise)
        return self

    def check_main_tabs_city_other(self, main_tabs_city_other):
        self.check_logo(main_tabs_city_other.main_page)
        self.choose_city_other(main_tabs_city_other.city)
        self.check_promos(main_tabs_city_other.promos_url)
        self.check_news(main_tabs_city_other.news_title)
        return self
