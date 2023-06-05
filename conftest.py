import pytest
from appium import webdriver as MD
from selenium import webdriver as WD
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.data_for_capabilities import apk_path


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
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = WD.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
