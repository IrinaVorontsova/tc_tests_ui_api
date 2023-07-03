# <a id="title1">Дипломный проект, UI тесты для сайта ТОКИО-CITY и API тесты по открытому swagger reqres.in</a>

[ТОКИО-CITY](https://www.tokyo-city.ru/) - сайт онлайн магазина городских ресторанов, доставка еды на дом и в офис

[reqres.in](https://reqres.in/api/) - реальные API для тестирования и разработки

## Технологический стек

 ![Python](/src/Python_logo_and_wordmark.png)![Pytest](/src/Pytest_logo.png)![selene](/src/selene.png)![Selenium](/src/Selenium.png)![requests](/src/requests.png)![Allure Report](/src/Allure_Report.png)![Jenkins](/src/Jenkins.png)![Telegram](/src/Telegram.png)

## Покрытый функционал

1. UI
    - Проверка основной страницы
    - Выбор региона + проверка региона + параметризация по регионам
    - Проверка основных вкладок
    - Проверка меню по основным категориям
    - Добавление товара в корзину + параметризация по категориям
    - Проверка количества добавленного товара
    - Удаление товара из корзины
   
2. API
   - Создание пользователя, метод POST
   - Изменение пользователя, метод PUT
   - Регистрация пользователя, метод POST
   - Проверка данных пользователя по id, метод GET
   - Удаление пользователя, метод DELETE
    
   
## Особенности тестов

UI-тесты параметризированы, запускаются поочередно по трем регионам, и трем разным категориям. 

## Запуск тестов

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/004-irin_vorontsova-tc_ui/)

Необходимо выбрать "Собрать с параметрами".


## Отчеты

Настроена отправка отчета в мессенджер - telegram

![Telegram Notifications](/src/bot_report.png)
### __Allure отчёты:__ 

#### [Allure Report](https://jenkins.autotests.cloud/job/004-irin_vorontsova-tc_ui/26/allure/)


![Allure_MAIN](/src/allure_14.png)


![Allure STEPS](/src/allure_steps.png)

Записывается видео прохождения теста

[![IMAGE ALT TEXT](http://img.youtube.com/watch?v=N3zYjMrHVlM/0.jpg)]
(https://www.youtube.com/watch?v=N3zYjMrHVlM "Video Title")