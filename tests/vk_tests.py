import allure

from constants.read_env import ReadEnv
from models.tabs_model import TabsModel
from pages.start_page import StartPage


class TestsVK:
    def test_vk_ui(self, setup_browser):
        # with allure.step("Authorization data"):
        #     user = Authorization(
        #         login=ReadEnv.LOGIN,
        #         password=ReadEnv.PASSWORD)

        with allure.step("Initialize form page"):
            registration = StartPage(setup_browser)

        with allure.step("Open test urls"):
            registration.open_browser(ReadEnv.URL)
            registration.check_tabs(main_page=ReadEnv.MAIN_PAGE, city=ReadEnv.SPB, menu_title=ReadEnv.MENU_TITLE, delivery_title=ReadEnv.DELIVERY_TITLE,
                                    promos_title=ReadEnv.PROMOS_TITLE, news_title=ReadEnv.NEWS_TITLE, addresses_title=ReadEnv.ADDRESSES_TITLE, cooking=ReadEnv.COOKING,
                                    banquet=ReadEnv.BANQUET)


        # with allure.step("Passed data for authorization"):
        #     registration.authorization(vk_header=ReadEnv.VK_HEADER, authorization=user, check_password=ReadEnv.CHECK_PASSWORD)
        #
