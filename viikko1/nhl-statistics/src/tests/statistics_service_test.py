import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual("Kurri", player.name)

    def test_search_returns_none_if_not_found(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(3, len(team_players))
        names = [p.name for p in team_players]
        self.assertCountEqual(["Semenko", "Kurri", "Gretzky"], names)

    def test_top_scorers_order_and_amount(self):
        top_players = self.stats.top(2)
        self.assertEqual(3, len(top_players))
        names = [p.name for p in top_players]
        self.assertEqual(["Gretzky", "Lemieux", "Yzerman"], names)
