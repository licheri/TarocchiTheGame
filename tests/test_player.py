import unittest
from tarots import Player, Hand, Card, Seed  # Assuming these classes exist

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Alice", Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)]))

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Alice")
        self.assertIsInstance(self.player.hand, Hand)

    def test_player_add_card(self):
        card = Card(Seed.tarots, 2)
        self.player.add_card(card)
        self.assertIn(card, self.player.hand.cards)

    def test_player_remove_card(self):
        card = self.player.hand.cards[0]
        self.player.remove_card(card)
        self.assertNotIn(card, self.player.hand.cards)

    def test_player_str(self):
        self.assertEqual(str(self.player), "Alice")

    def test_player_repr(self):
        self.assertEqual(repr(self.player), "Alice")

    def test_player_score(self):
        self.assertEqual(self.player.score, 0)  # Assuming initial score is 0

    def test_player_update_score(self):
        self.player.debt = 10
        self.player.won_cards = Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)])
        self.player.update_score()
        self.assertEqual(self.player.score, (12 + 13 - 10) // 3)

    def test_player_clear_hand(self):
        self.player.clear_hand()
        self.assertEqual(len(self.player.hand.cards), 0)

if __name__ == '__main__':
    unittest.main()
