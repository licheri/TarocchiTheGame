import unittest
from tarots import PlayedCard, Card, Seed, Player, Hand  # Assuming these classes exist

class TestPlayedCard(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Alice", Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)]))
        self.player_2 = Player("Bob", Hand([Card(Seed.tarots, 2), Card(Seed.tarots, 3)]))
        self.card_1 = Card(Seed.tarots, 0)
        self.card_2 = Card(Seed.tarots, 2)
        self.played_card_1 = PlayedCard.from_card(self.card_1, 0,self.player_1)
        self.played_card_2 = PlayedCard.from_card(self.card_2, 1,self.player_2)

    def test_playedcard_initialization(self):
        self.assertEqual(self.played_card_1.card, self.card_1)
        self.assertEqual(self.played_card_1.player, self.player_1)

    def test_playedcard_str(self):
        self.assertEqual(str(self.played_card_1), "0) 0: The Fool from Alice")

    def test_playedcard_repr(self):
        self.assertEqual(repr(self.played_card_1), "0) 0: The Fool from Alice")

    def test_playedcard_equality(self):
        self.assertEqual(self.played_card_1, self.played_card_1)

    def test_playedcard_inequality(self):
        self.assertNotEqual(self.played_card_1, self.played_card_2)

    def test_playedcard_less_than(self):
        self.assertLess(self.played_card_1, self.played_card_2)

    def test_playedcard_greater_than(self):
        self.assertGreater(self.played_card_2, self.played_card_1)

if __name__ == '__main__':
    unittest.main()
