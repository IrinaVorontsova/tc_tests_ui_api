from os import getenv
from dotenv import load_dotenv


class ReadEnv:
    load_dotenv()

    URL = getenv("URL")
    MAIN_PAGE = getenv("MAIN_PAGE")
    SPB = getenv("SPB")
    MSK = getenv("MSK")
    PTZ = getenv("PTZ")
    VLN = getenv("VLN")
    MENU_TITLE = getenv("MENU_TITLE")
    DELIVERY_TITLE = getenv("DELIVERY_TITLE")
    PROMOS_URL = getenv("PROMOS_URL")
    NEWS_TITLE = getenv("NEWS_TITLE")
    ADDRESSES_TITLE = getenv("ADDRESSES_TITLE")
    BANQUET = getenv("BANQUET")
    COOKING = getenv("COOKING")
    VACANCIES = getenv("VACANCIES")
    FRANCHISE = getenv("FRANCHISE")
    SUSHI = getenv("SUSHI")
    POLLS = getenv("POLLS")
    SETS = getenv("SETS")


