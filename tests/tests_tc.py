import allure
import pytest

from constants.read_env import ReadEnv
from models.tabs_model import MainTabsSpb, MainTabsOtherCity, TabsNewWindow
from pages.start_page import StartPage


class TestsTC:

    @allure.description("Test tabs clickable")
  #  @pytest.mark.parametrize("city", [ReadEnv.MSK, ReadEnv.PTZ, ReadEnv.VLN])
    @pytest.mark.parametrize("city", [ReadEnv.SPB])
    def test_tc_ui(self, setup_browser, city):
        with allure.step("Tests data initialized"):
            main_tabs_spb = MainTabsSpb(
                main_page=ReadEnv.MAIN_PAGE,
                city=ReadEnv.SPB,
                menu_title=ReadEnv.MENU_TITLE,
                delivery_title=ReadEnv.DELIVERY_TITLE,
                promos_url=ReadEnv.PROMOS_URL,
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
                promos_url=ReadEnv.PROMOS_URL,
                news_title=ReadEnv.NEWS_TITLE)

        with allure.step("Initialize form page"):
            registration = StartPage(setup_browser)

        with allure.step("Open test urls"):
            registration.open_browser(ReadEnv.URL)

       # with allure.step("Check tabs Spb"):
            # registration.check_main_tabs_spb(main_tabs_spb)

        with allure.step("Check tabs where open in new windows"):
            registration.check_other_window_tabs(tabs_new_window)

       # with allure.step("Chech other regions":
            #registration.check_main_tabs_city_other(main_tabs_city_other)

