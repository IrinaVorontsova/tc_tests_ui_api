import requests
from dotenv import load_dotenv

from constants.read_env import ReadEnv

load_dotenv()

def data_create_user():
    data = {
        "name": "Anton",
        "job": "1C developer"
    }
    return data


def data_edit_user():
    data = {
        "name": "Sveta",
        "job": "witcher"
    }
    return data


def data_register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return data


def data_authorization():
    authorization = requests.post("/api/login", data={
        "email": ReadEnv.EMAIL_API,
        "password": ReadEnv.PASSWORD_API
    })
    cookie_value = authorization.cookies.get("token")
    token = {}
    if cookie_value is not None:
        token.update({"token": cookie_value})

    return token