import unittest
from tarots import Seed, Card, Hand, Deck, Player, PlayedCard

class TestSeed(unittest.TestCase):

    def test_seed_comparison(self):
        self.assertTrue(Seed.spades < Seed.coins)
        self.assertTrue(Seed.spades <= Seed.coins)
        self.assertTrue(Seed.coins > Seed.spades)
        self.assertTrue(Seed.coins >= Seed.spades)
        self.assertTrue(Seed.spades == Seed.spades)
        self.assertTrue(Seed.spades != Seed.coins)

    def test_seed_notation(self):
        self.assertEqual(Seed.spades.notation, 's')
        self.assertEqual(Seed.value_to_notation(1), 's')
        self.assertEqual(Seed.from_notation('s'), Seed.spades)

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
        self.assertEqual(self.hand.value, 12 + 13)

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

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck.standard()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 78)

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
        self.assertEqual([card.number for card in self.deck.cards[-22:]], list(range(22)))

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
        self.assertEqual(self.player.score, 0)

    def test_player_update_score(self):
        self.player.debt = 10
        self.player.won_cards = Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)])
        self.player.update_score()
        self.assertEqual(self.player.score, (12 + 13 - 10) // 3)

    def test_player_clear_hand(self):
        self.player.clear_hand()
        self.assertEqual(len(self.player.hand.cards), 0)

    def test_player_add_won_card(self):
        card = Card(Seed.tarots, 2)
        self.player.add_won_card(card)
        self.assertIn(card, self.player.won_cards.cards)

    def test_player_remove_won_card(self):
        card = Card(Seed.tarots, 2)
        self.player.add_won_card(card)
        self.player.remove_won_card(card)
        self.assertNotIn(card, self.player.won_cards.cards)

    def test_player_has_won_card(self):
        card = Card(Seed.tarots, 2)
        self.player.add_won_card(card)
        self.assertTrue(self.player.has_won_card(card))

    def test_player_has_won_cards(self):
        cards = [Card(Seed.tarots, 2), Card(Seed.tarots, 3)]
        self.player.add_won_cards(cards)
        self.assertTrue(self.player.has_won_cards(cards))

    def test_player_has_won_seed(self):
        card = Card(Seed.tarots, 2)
        self.player.add_won_card(card)
        self.assertTrue(self.player.has_won_seed(Seed.tarots))

    def test_player_has_won_seeds(self):
        cards = [Card(Seed.tarots, 2), Card(Seed.spades, 3)]
        self.player.add_won_cards(cards)
        self.assertTrue(self.player.has_won_seeds([Seed.tarots, Seed.spades]))

class TestPlayedCard(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Alice", Hand([Card(Seed.tarots, 0), Card(Seed.tarots, 1)]))
        self.player_2 = Player("Bob", Hand([Card(Seed.tarots, 2), Card(Seed.tarots, 3)]))
        self.card_1 = Card(Seed.tarots, 0)
        self.card_2 = Card(Seed.tarots, 2)
        self.played_card_1 = PlayedCard.from_card(self.card_1, 0, self.player_1)
        self.played_card_2 = PlayedCard.from_card(self.card_2, 1, self.player_2)

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
