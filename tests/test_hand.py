import unittest
from tarots import Hand, Card, Seed  # Assuming these classes exist

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)])

    def test_hand_initialization(self):
        self.assertEqual(len(self.hand.cards), 2)

    def test_hand_add_card(self):
        card = Card(Seed.tarots, 2)
        self.hand.add_card(card)
        self.assertIn(card, self.hand.cards)

    def test_hand_remove_card(self):
        card = self.hand.cards[0]
        self.hand.remove_card(card)
        self.assertNotIn(card, self.hand.cards)

    def test_hand_str(self):
        self.assertEqual(str(self.hand), '[1: The Magician, 0: The Fool]')

    def test_hand_repr(self):
        self.assertEqual(repr(self.hand), '[1: The Magician, 0: The Fool]')

    def test_hand_sort(self):
        self.hand.add_card(Card(Seed.tarots, 2))
        self.hand.sort()
        self.assertEqual([card.number for card in self.hand.cards], [2, 1, 0])

    def test_hand_value(self):
        self.assertEqual(self.hand.value, 12 + 13)  # Assuming value is sum of card values

    def test_hand_clear(self):
        self.hand.clear()
        self.assertEqual(len(self.hand.cards), 0)

    def test_hand_contains(self):
        card = Card(Seed.tarots, 0)
        self.assertIn(card, self.hand)
        card_not_in_hand = Card(Seed.tarots, 3)
        self.assertNotIn(card_not_in_hand, self.hand)

    def test_hand_len(self):
        self.assertEqual(len(self.hand), 2)

    def test_hand_getitem(self):
        self.assertEqual(self.hand[0], Card(Seed.tarots, 1))
        self.assertEqual(self.hand[1], Card(Seed.tarots, 0))

    def test_hand_setitem(self):
        new_card = Card(Seed.tarots, 2)
        self.hand[0] = new_card
        self.assertEqual(self.hand[0], new_card)

    def test_hand_delitem(self):
        del self.hand[0]
        self.assertEqual(len(self.hand), 1)
        self.assertEqual(self.hand[0], Card(Seed.tarots, 0))

    def test_hand_iter(self):
        cards = [card for card in self.hand]
        self.assertEqual(cards, [Card(Seed.tarots, 1), Card(Seed.tarots, 0)])

    def test_hand_add(self):
        hand1 = Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)])
        hand2 = Hand([Card(Seed.tarots, 2), Card(Seed.tarots, 3)])
        combined_hand = hand1 + hand2
        self.assertEqual(len(combined_hand.cards), 4)
        self.assertIn(Card(Seed.tarots, 0), combined_hand.cards)
        self.assertIn(Card(Seed.tarots, 1), combined_hand.cards)
        self.assertIn(Card(Seed.tarots, 2), combined_hand.cards)
        self.assertIn(Card(Seed.tarots, 3), combined_hand.cards)

    def test_hand_add_with_duplicates(self):
        hand1 = Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)])
        hand2 = Hand([Card(Seed.tarots, 1), Card(Seed.tarots, 2)])
        combined_hand = hand1 + hand2
        self.assertEqual(len(combined_hand.cards), 3)
        self.assertIn(Card(Seed.tarots, 0), combined_hand.cards)
        self.assertIn(Card(Seed.tarots, 1), combined_hand.cards)
        self.assertIn(Card(Seed.tarots, 2), combined_hand.cards)

if __name__ == '__main__':
    unittest.main()
