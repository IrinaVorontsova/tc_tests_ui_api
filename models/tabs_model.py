from dataclasses import dataclass


@dataclass
class TabsModel:
    main_page: str
    city: str
    menu_title: str
    delivery_title: str
    promos_title: str
    news_title: str
    addresses_title: str
