
class WebLocators:
    #exit_vk_text = "[class='VkIdForm__header']" #gettext Вход ВКонтакте
    exit_vk_text="[class='msg_text']"
    login = "#index_email"
    check_box = "[class='VkIdCheckbox__checkboxOn']"
    exit = "[class='FlatButton__in']"
    enter_password = "[class='vkc__VKDisplayTitle__title vkc__VKDisplayTitle__demiboldWeight vkc__VKDisplayTitle__titleLevel2']" #gettext Введите пароль
    password = "[name='password']"
    continue_ = "[class='vkuiButton__content vkuiText vkuiText--sizeY-compact vkuiText--w-2']"

class PageLocators:
    def set_month_birth(month):
        return f'option[value="{month}"]'

    def set_year_birth(year):
        return f'option[value="{year}"]'

    def set_day_birth(day):
        return f"react-datepicker__day--{day}"

    first_name = '#firstName'
    last_name = '#lastName'
    email = '#userEmail'

    gender_male = '[for="gender-radio-1"]'
    gender_female = '[for="gender-radio-2"]'
    gender_other = '[for="gender-radio-3"]'

    phone = '#userNumber'

    date_birth_field = '#dateOfBirthInput'
    date_birth_month = f'select[class="react-datepicker__month-select"] {set_month_birth("10")}'
    date_birth_year = f'select[class="react-datepicker__year-select"] {set_year_birth("2000")}'
    date_birth_day = f'*[class="react-datepicker__day {set_day_birth("020")}"]'
