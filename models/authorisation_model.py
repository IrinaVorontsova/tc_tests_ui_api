from dataclasses import dataclass


@dataclass
class Authorization:
    login: str
    password: str
