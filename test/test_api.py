import allure
import requests
from requests import Response
from pytest_voluptuous import S
from shemas.reqres import *
from models.api_models import *


def test_post_create_user():
    code = 201

    with allure.step("Send request: post create user"):
        create = requests.post(ReadEnv.URL_API + "/api/users", data_create_user())

    with allure.step(f"Check code response {code}"):
        assert create.status_code == code, f"Code of response don't {code}"

    with allure.step("Check schema is correct"):
        assert create.json() == S(post_create_user_schema)

    with allure.step("Check user data"):
        assert create.json()["name"] == data_create_user()["name"],  "Name created user is not corrected"
        assert create.json()["job"] == data_create_user()["job"], "Job created user is not corrected"
        assert isinstance(create.json()["id"], str), "Id is not corrected"
        assert isinstance(create.json()["createdAt"], str), "Data is not corrected"


def test_post_register_user():
    with allure.step("Send request: post register user"):
        code = 200

        register = requests.post(ReadEnv.URL_API + "/api/register", data_register_user())

    with allure.step(f"Check code response {code}"):
        assert register.status_code == code, f"Code of response don't {code}"

    with allure.step("Check schema is correct"):
        assert register.json() == S(post_register_user_schema)

    with allure.step("Check user data"):
        assert register.json()["id"] == 4, "Id is not corrected"
        assert isinstance(register.json()["id"], int), "Id is not int"
        assert register.json()["token"] == "QpwL5tke4Pnpja7X4", "Token is not corrected"
        assert isinstance(register.json()["token"], str), "Token is not string"

def test_put_user():
    with allure.step("Send request: put user"):
        code = 200
        id_user = 2
        update = requests.put(ReadEnv.URL_API + f"/api/users/{id_user}", data_edit_user())

    with allure.step(f"Check code response {code}"):
        assert update.status_code == code, f"Code of response don't {code}"

    with allure.step("Check schema is correct"):
        assert update.json() == S(put_user_schema)

    with allure.step("Check user data"):
        assert update.json()["name"] == data_edit_user()["name"], "Name test user is not corrected"
        assert update.json()["job"] == data_edit_user()["job"], "Job test user is not corrected"


def test_get_single_user():
    with allure.step("Send request: get single user for id"):
        id_user = 5
        code = 200
        response: Response = requests.get(ReadEnv.URL_API + f"/api/users/{id_user}")

    with allure.step(f"Check code response {code}"):
        assert response.status_code == code, f"Code of response don't {code}"

    with allure.step("Check schema is correct"):
        assert response.json() == S(get_single_user_schema)

    with allure.step(f"Check test user data from id {id_user}"):
        assert response.json()["data"]["id"] == id_user, "Id is not corrected"
        assert response.json()["data"]["email"] == "charles.morris@reqres.in"
        assert response.json()["data"]["first_name"] == "Charles", "Name test user is not corrected"
        assert response.json()["data"]["last_name"] == "Morris", "Last name test user is not corrected"
        assert response.json()["data"]["avatar"] == "https://reqres.in/img/faces/5-image.jpg"\
            , "Avatar is not corrected"

def test_delete_user():
    with allure.step('send delete request'):
        id_user = 2
        code = 204

        result = requests.delete(ReadEnv.URL_API + f"/api/users/{id_user}")

    with allure.step(f"Check code response {code}"):
        assert result.status_code == code, f"Code of response don't {code}"


