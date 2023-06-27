from dataclasses import dataclass


@dataclass
class MainTabsSpb:
    main_page: str
    city: str
    menu_title: str
    delivery_title: str
    promos_url: str
    news_title: str
    addresses_title: str
    cooking: str

@dataclass
class MainTabsOtherCity:
    main_page: str
    city: str
    promos_url: str
    news_title: str

@dataclass
class TabsNewWindow:
    banquets: str
    vacancies: str
    franchise: str

