
class WebLocators:
    @staticmethod
    def city_choose(city):
        return f"//*[@class='city__list']//*[contains(text(), '{city}')]"

    @staticmethod
    def category_choose(category):
        return f"//span[contains(text(),'{category}')]"

    ddos = "#checkbox"
    main_logo = "[class=[class='logo']]"
    city_spb = "[class='location1-popup__btn1']"
    city_yes = "//*[contains(text(), 'Да')]"
    city_other = "[class='location1-popup__btn2 js-location1']"
    city_check = "[class='location1__link js-location1']"
    title_page = "[class='title__container']"
    menu = "[class='navigation__item  navigation__item--menu']"
    delivery = "//header//*[contains(text(), 'Доставка')]"
    promos = "//header//*[contains(text(), 'Акции')][1]"
    news = "//header//*[contains(text(), 'Новости')]"
    addresses = "//header//*[contains(text(), 'Адреса')]"
    banquets = "//header//*[contains(text(), 'Банкеты')]"
    banquet = "//div[1]/header//*[@href='#booking']"
    vacancies = "//header//*[contains(text(), 'Вакансии')]"
    franchise = "//header//*[contains(text(), 'Франшиза')]"
    home_cooking = "//header//*[contains(text(), 'Домашняя')][1]"
    cooking_title = "[class='content-bg__title']"
    add_to_cart = "[class='btn  btn--red  btn--order']"
    cart = "[class='cart']"
    quantity_cart = "[class='cart__value simpleCart_quantity']"
    remove = "[class='simpleCart_remove']"

