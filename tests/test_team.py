import unittest
from tarots import Seed, Card, Hand, Player, Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Alice", Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)]))
        self.player2 = Player("Bob", Hand([Card(Seed.tarots, 2), Card(Seed.tarots, 3)]))
        self.team = Team([self.player1, self.player2])

    def test_team_initialization(self):
        self.assertEqual(len(self.team.players), 2)

    def test_team_add_player(self):
        player3 = Player("Charlie", Hand([Card(Seed.tarots, 4)]))
        self.team.add_player(player3)
        self.assertIn(player3, self.team.players)

    def test_team_remove_player(self):
        self.team.remove_player(self.player1)
        self.assertNotIn(self.player1, self.team.players)

    def test_team_add_card(self):
        card = Card(Seed.tarots, 5)
        self.team.add_card(card)
        self.assertIn(card, self.team.won_cards.cards)

    def test_team_remove_card(self):
        card = Card(Seed.tarots, 0)
        self.team.add_card(card)
        self.team.remove_card(card)
        self.assertNotIn(card, self.team.won_cards.cards)

if __name__ == '__main__':
    unittest.main()
