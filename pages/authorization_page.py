from constants.read_env import ReadEnv
from locators.web_locators import WebLocators


class AuthorizationPage:
    def __init__(self, setup_browser):
        self.setup_browser = setup_browser
        self.vk_header = self.setup_browser.element(WebLocators.exit_vk_text)
        self.login = self.setup_browser.element(WebLocators.exit_vk_text)
        self.check_box = self.setup_browser.element(WebLocators.check_box)
        self.exit = self.setup_browser.element(WebLocators.exit)
        self.enter_password = self.setup_browser(WebLocators.enter_password)
        self.password = self.setup_browser(WebLocators.password)
        self.continue_ = self.setup_browser(WebLocators.continue_)

    def open_browser(self):
        self.setup_browser.open(ReadEnv.URL)
        return self


    def _set_first_name(self, first_name):
        self.first_name.should(be.blank).type(first_name)
        return self

    def _set_last_name(self, last_name):
        self.last_name.should(be.blank).type(last_name)
        return self

    def _set_email(self, email):
        self.email.should(be.blank).type(email)
        return self

    def _set_gender(self, gender):
        self.gender.should(have.text(gender)).click()
        return self

    def _set_phone(self, phone):
        self.phone.should(be.blank).type(phone)
        return self

    def set_date_birth(self):
        self.setup_browser.element(PageLocators.date_birth_field).click()
        self.setup_browser.element(PageLocators.date_birth_month).click()
        self.setup_browser.element(PageLocators.date_birth_year).click()
        self.setup_browser.element(PageLocators.date_birth_day).click()

        return self

    def _set_hobby_one(self, hobby):
        self.hobby_one.should(be.blank).type(hobby).press_enter()
        return self

    def _set_hobby_two(self, hobby):
        self.hobby_two.should(have.text(hobby)).click()
        return self

    def _set_photo(self, photo):
        self.photo.send_keys(os.getcwd() + "/tests/resources/" + photo)
        return self

    def _set_address(self, address):
        self.address.should(be.blank).type(address)
        return self

    def _set_state(self, state):
        self.state.should(be.blank).type(state).press_enter()
        return self

    def _set_city(self, city):
        self.city.should(be.blank).type(city).press_enter()
        return self

    def click_submit(self):
        self.submit.perform(command.js.click)
        return self

    def registration_user(self, user):
        self._set_first_name(user.first_name)
        self._set_last_name(user.last_name)
        self._set_email(user.email)
        self._set_gender(user.gender)
        self._set_phone(user.phone_number)
        self.set_date_birth()
        self._set_hobby_one(user.interests)
        self._set_hobby_two(user.hobby)
        self._set_photo(user.photo_path)
        self._set_address(user.address)
        self._set_state(user.state)
        self._set_city(user.city)
        self.click_submit()
        return self

    def assert_saved_form(self, user):
        name = user.first_name + ' ' + user.last_name
        birthday = user.birth_day + ' ' + user.birth_month + ',' + user.birth_year
        state_city = user.state + ' ' + user.city

        self.setup_browser.element(PageLocators.element_form_one).all(PageLocators.element_form_two).even.should(
            have.exact_texts(
                name,
                user.email,
                user.gender,
                f'{user.phone_number}',
                birthday,
                user.interests,
                user.hobby,
                user.photo_path,
                user.address,
                state_city
            )
        )
        self.setup_browser.element(PageLocators.close_form).perform(command.js.click)

        return self
