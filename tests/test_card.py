import unittest
from tarots import Seed, Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(Seed.tarots, 0)

    def test_card_initialization(self):
        self.assertEqual(self.card.seed, Seed.tarots)
        self.assertEqual(self.card.number, 0)

    def test_card_str(self):
        self.assertEqual(str(self.card), "0: The Fool")

    def test_card_repr(self):
        self.assertEqual(repr(self.card), "0: The Fool")

    def test_card_notation(self):
        self.assertEqual(self.card.notation, "0t")

    def test_card_random(self):
        card = Card.random()
        self.assertIsInstance(card, Card)

    def test_card_comparison(self):
        card1 = Card(Seed.tarots, 1)
        card2 = Card(Seed.spades, 1)
        self.assertTrue(card1 > card2)
        self.assertTrue(card2 < card1)
        self.assertTrue(card1 != card2)

    def test_card_value(self):
        self.assertEqual(self.card.value, 12)

if __name__ == '__main__':
    unittest.main()