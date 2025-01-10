import unittest
from tarots import Deck, Card, Seed, Hand  # Assuming these classes exist

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck.standard()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 78)  # Assuming a standard tarot deck

    def test_deck_shuffle(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, original_order)

    def test_deck_draw_card(self):
        card = self.deck.draw_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(self.deck.cards), 77)

    def test_deck_add_card(self):
        card = Card(Seed.tarots, 0)
        self.deck.add_card(card)
        self.assertIn(card, self.deck.cards)

    def test_deck_remove_card(self):
        card = self.deck.cards[0]
        self.deck.remove_card(card)
        self.assertNotIn(card, self.deck.cards)

    def test_deck_str(self):
        self.assertIsInstance(str(self.deck), str)

    def test_deck_repr(self):
        self.assertIsInstance(repr(self.deck), str)

    def test_deck_sort(self):
        self.deck.shuffle()
        self.deck.sort()
        self.assertEqual([card.number for card in self.deck.cards[-22:]], list(range(22)))  # Assuming major arcana are 0-21

    def test_deck_clear(self):
        self.deck.clear()
        self.assertEqual(len(self.deck.cards), 0)

    def test_deck_contains(self):
        card = Card(Seed.tarots, 0)
        self.assertIn(card, self.deck)
        card_not_in_deck = Card(Seed.tarots, 100)
        self.assertNotIn(card_not_in_deck, self.deck)

    def test_deck_len(self):
        self.assertEqual(len(self.deck), 78)

    def test_deck_getitem(self):
        self.assertIsInstance(self.deck[0], Card)

    def test_deck_setitem(self):
        new_card = Card(Seed.tarots, 0)
        self.deck[0] = new_card
        self.assertEqual(self.deck[0], new_card)

    def test_deck_delitem(self):
        del self.deck[0]
        self.assertEqual(len(self.deck), 77)

    def test_deck_iter(self):
        cards = [card for card in self.deck]
        self.assertEqual(len(cards), 78)

    def test_deck_deal_3(self):
        hands, prize = self.deck.deal(3)
        self.assertIsInstance(hands[0], Hand)
        self.assertIsInstance(prize[0], Card)
        self.assertEqual(len(hands), 3)
        self.assertEqual(len(hands[0].cards), (78 - 3) // 3)
        self.assertEqual(len(prize), 3)
        total_cards = sum([len(hand.cards) for hand in hands]) + len(prize)
        self.assertEqual(total_cards, 78)

    def test_deck_deal_4(self):
        hands, prize = self.deck.deal(4)
        self.assertIsInstance(hands[0], Hand)
        self.assertIsInstance(prize[0], Card)
        self.assertEqual(len(hands), 4)
        self.assertEqual(len(hands[0].cards), (78 - 2) // 4)
        self.assertEqual(len(prize), 2)
        total_cards = sum([len(hand.cards) for hand in hands]) + len(prize)
        self.assertEqual(total_cards, 78)

    def test_deck_deal_5(self):
        hands, prize = self.deck.deal(5)
        self.assertIsInstance(hands[0], Hand)
        self.assertIsInstance(prize[0], Card)
        self.assertEqual(len(hands), 5)
        self.assertEqual(len(hands[0].cards), (78 - 3) // 5)
        self.assertEqual(len(prize), 3)
        total_cards = sum([len(hand.cards) for hand in hands]) + len(prize)
        self.assertEqual(total_cards, 78)

if __name__ == '__main__':
    unittest.main()
