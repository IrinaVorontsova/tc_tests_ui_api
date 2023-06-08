from os import getenv
from dotenv import load_dotenv


class ReadEnv:
    load_dotenv()

    URL = getenv("URL")
    LOGIN = getenv("LOGIN")
    PASSWORD = getenv("PASSWORD}")
