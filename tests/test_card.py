import unittest
from tarots import Card, Seed  # Assuming these classes exist

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(Seed.tarots, 0)

    def test_card_seed(self):
        self.assertEqual(self.card.seed, Seed.tarots)

    def test_card_number(self):
        self.assertEqual(self.card.number, 0)

    def test_card_str(self):
        self.assertEqual(str(self.card), '0: The Fool')

    def test_card_repr(self):
        self.assertEqual(repr(self.card), '0: The Fool')

    def test_card_equality(self):
        card1 = Card(Seed.tarots, 0)
        card2 = Card(Seed.tarots, 0)
        self.assertEqual(card1, card2)

    def test_card_inequality(self):
        card1 = Card(Seed.tarots, 0)
        card2 = Card(Seed.tarots, 1)
        self.assertNotEqual(card1, card2)

    def test_card_less_than(self):
        card1 = Card(Seed.tarots, 0)
        card2 = Card(Seed.tarots, 1)
        self.assertLess(card1, card2)

    def test_card_less_than_or_equal(self):
        card1 = Card(Seed.tarots, 0)
        card2 = Card(Seed.tarots, 1)
        self.assertLessEqual(card1, card2)
        self.assertLessEqual(card1, card1)

    def test_card_greater_than(self):
        card1 = Card(Seed.tarots, 1)
        card2 = Card(Seed.tarots, 0)
        self.assertGreater(card1, card2)

    def test_card_greater_than_or_equal(self):
        card1 = Card(Seed.tarots, 1)
        card2 = Card(Seed.tarots, 0)
        self.assertGreaterEqual(card1, card2)
        self.assertGreaterEqual(card1, card1)

    def test_card_value(self):
        card = Card(Seed.tarots, 0)
        self.assertEqual(card.value, 12)

    def test_card_notation(self):
        card = Card(Seed.spades, 5)
        self.assertEqual(card.notation, '5s')

    def test_card_random(self):
        card = Card.random()
        self.assertIsInstance(card, Card)

if __name__ == '__main__':
    unittest.main()