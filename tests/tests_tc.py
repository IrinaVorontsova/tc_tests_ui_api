import allure
import pytest

from constants.read_env import ReadEnv
from models.tabs_model import MainTabsSpb, MainTabsOtherCity, TabsNewWindow
from pages.start_page import StartPage


class TestsTC:

    @allure.description("Test tabs clickable")
    @pytest.mark.parametrize("city", [ReadEnv.MSK, ReadEnv.PTZ, ReadEnv.VLN])
    def test_tc_ui(self, setup_browser, city):
        with allure.step("Tests data initialized"):
            main_tabs_spb = MainTabsSpb(
                main_page=ReadEnv.MAIN_PAGE,
                city=ReadEnv.SPB,
                menu_title=ReadEnv.MENU_TITLE,
                delivery_title=ReadEnv.DELIVERY_TITLE,
                promos_title=ReadEnv.PROMOS_TITLE,
                news_title=ReadEnv.NEWS_TITLE,
                addresses_title=ReadEnv.ADDRESSES_TITLE,
                cooking=ReadEnv.COOKING)

            tabs_new_window=TabsNewWindow(
                banquets=ReadEnv.BANQUET,
                vacancies=ReadEnv.VACANCIES,
                franchise=ReadEnv.FRANCHISE)

            main_tabs_city_other = MainTabsOtherCity(
                main_page=ReadEnv.MAIN_PAGE,
                city=city,
                menu_title=ReadEnv.MENU_TITLE,
                promos_title=ReadEnv.PROMOS_TITLE,
                news_title=ReadEnv.NEWS_TITLE)

        with allure.step("Initialize form page"):
            registration = StartPage(setup_browser)

        with allure.step("Open test urls"):
            registration.open_browser(ReadEnv.URL)
           # registration.check_main_tabs_spb(main_tabs_spb)
            registration.check_main_tabs_city_other(main_tabs_city_other)


        # with allure.step("Passed data for authorization"):
        #     registration.authorization(vk_header=ReadEnv.VK_HEADER, authorization=user, check_password=ReadEnv.CHECK_PASSWORD)
        #
