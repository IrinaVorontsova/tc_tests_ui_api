import allure

from constants.read_env import ReadEnv
from models.authorisation_model import Authorization
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
            registration.check_tabs(ReadEnv.MAIN_PAGE)


        # with allure.step("Passed data for authorization"):
        #     registration.authorization(vk_header=ReadEnv.VK_HEADER, authorization=user, check_password=ReadEnv.CHECK_PASSWORD)
        #
