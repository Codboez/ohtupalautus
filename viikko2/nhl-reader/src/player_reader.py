import requests
from player import Player

class PlayerReader:
    def __init__(self, url) -> None:
        self.__url = url

        json = self.get_players_as_json()
        self.players = self.turn_players_as_json_to_player_objects(json)

    def get_players_as_json(self):
        return requests.get(self.__url).json()

    def turn_players_as_json_to_player_objects(self, response):
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players