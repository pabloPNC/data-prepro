from pydantic import BaseModel


class Monster(BaseModel):
    name: str
    size: str
    aligment: str
    ac: int
    hp: int
    speed: int
    stre: int
    dex: int
    con: int
    wis: int
    cha: int
    vulnerabilities: list[str]
    immunities: list[str]
    senses: list[str]
    languages: list[str]
    cr: int
    actions: list[str]

