import requests
from enum import Enum


class PokemonFields(Enum):
    NAME = "name"
    URL = "url"


Pokemon = dict[PokemonFields, str]


class Crawler:
    def __init__(self, url: str):
        self.url = url
        self.next_url = None
        self.pokemon_data = {}

    def start(self):
        data = requests.get(self.url).json()
        self.extract(data)
        while self.next_url is not None:
            data = requests.get(self.next_url).json()
            self.extract(data)

    def extract(self, data: dict[str, str | dict]) -> dict:
        self.next_url = data["next"]
        results: list[Pokemon] = data["results"]
        for pokemon in results:
            self.pokemon_data[pokemon["name"]] = requests.get(
                pokemon["url"]
            ).json()
