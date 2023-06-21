import pytest
from appium import webdriver as MD
import os
from dotenv import load_dotenv
from selene import browser
from selene import config
from selenium.webdriver.chrome.options import Options
from utils import attach

from utils.data_for_capabilities import apk_path
# удалить под селенид
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def mobile_driver():
    APPIUM = "http://127.0.0.1:4723/wd/hub"
    CAPS = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "AndroidEmulator",
        "app": apk_path()
    }
    mobile_driver = MD.Remote(command_executor=APPIUM, desired_capabilities=CAPS)
    yield mobile_driver
    mobile_driver.quit()


@pytest.fixture(scope="session")
def setup_browser():
    config.window_width = 1600
    config.window_height = 1024
    yield browser
    browser.quit()

# DEFAULT_BROWSER_VERSION = "100.0"
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='100.0'
#     )
#
#
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function')
# def setup_browser(request):
#     browser_version = request.config.getoption('--browser_version')
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#
#     driver = webdriver.Remote(
#         command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser.config.driver = driver
#
#     yield browser
#
#     attach.add_html(browser)
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_video(browser)
#     browser.quit()
