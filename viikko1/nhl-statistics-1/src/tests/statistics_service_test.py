import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReader:
    def __init__(self) -> None:
        self.players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

    def get_players(self):
        return self.players

class StatisticsServiceTest(unittest.TestCase):
    def setUp(self):
        self.player_reader = PlayerReader()
        self.stats = StatisticsService(self.player_reader)

    def test_search_returns_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player, self.player_reader.get_players()[2])

    def test_search_returns_none_when_not_found(self):
        player = self.stats.search("Selanne")

        self.assertEqual(player, None)

    def test_team_returns_players_of_team(self):
        players_of_team = self.stats.team("PIT")

        self.assertEqual(players_of_team[0], self.player_reader.get_players()[1])

    def test_top_returns_players_sorted_by_points(self):
        players = self.stats.top(5)

        self.assertEqual(players[0], self.player_reader.get_players()[4])

    def test_top_returns_correct_amount_of_players(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 3)

    def test_top_sorts_with_goals_correctly(self):
        players = self.stats.top(5, SortBy.GOALS)

        self.assertEqual(players[0], self.player_reader.get_players()[1])

    def test_top_sorts_with_assists_correctly(self):
        players = self.stats.top(5, SortBy.ASSISTS)

        self.assertEqual(players[0], self.player_reader.get_players()[4])

    def test_top_returns_none_when_given_invalid_sort_method(self):
        players = self.stats.top(5, None)

        self.assertEqual(players, None)