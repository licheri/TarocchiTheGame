import unittest
from tarots import Team, Player, Hand, Card, Seed  # Assuming these classes exist

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team([Player("Player 1"), Player("Player 2")])
        self.player_1 = self.team.players[0]
        self.player_2 = self.team.players[1]

    def test_team_initialization(self):
        self.assertEqual(len(self.team.players), 2)
        self.assertIn(self.player_1, self.team.players)
        self.assertIn(self.player_2, self.team.players)

    def test_team_add_card(self):
        card = Card(Seed.tarots, 4)
        self.team.add_card(card)
        self.assertIn(card, self.team.won_cards.cards)

    def test_team_remove_card(self):
        card = Card(Seed.tarots, 0)
        self.team.add_card(card)
        self.team.remove_card(card)
        self.assertNotIn(card, self.team.won_cards.cards)

    def test_team_add_player(self):
        player_3 = Player("Charlie", Hand([Card(Seed.tarots, 4)]))
        self.team.add_player(player_3)
        self.assertIn(player_3, self.team.players)

    def test_team_remove_player(self):
        self.team.remove_player(self.player_1)
        players = self.team.players
        print(self.team)    
        print(f"players: {players}")
        print(f"player 1: {self.player_1}")
        print(f"is player 1 in players: {self.player_1 in players}")
        print(f"players: {players}")
        self.assertNotIn(self.player_1, self.team.players)
        self.assertNotIn(self.player_1, self.team)

    def test_team_value(self):
        card1 = Card(Seed.tarots, 0)
        card2 = Card(Seed.tarots, 1)
        self.team.add_card(card1)
        self.team.add_card(card2)
        self.assertEqual(self.team.value, card1.value+card2.value )  # Assuming value is sum of card values

    def test_team_has_card(self):
        card = Card(Seed.tarots, 0)
        self.team.add_card(card)
        self.assertTrue(self.team.has_card(card))

    def test_team_has_seed(self):
        self.assertFalse(self.team.has_seed(Seed.tarots))

    def test_team_reset_team_won_cards(self):
        self.team.reset_team_won_cards()
        self.assertEqual(len(self.team.won_cards.cards), 0)

    def test_team_reset_players_won_cards(self):
        self.team.reset_players_won_cards()
        self.assertEqual(len(self.player_1.won_cards.cards), 0)
        self.assertEqual(len(self.player_2.won_cards.cards), 0)

    def test_team_update_team_won_cards(self):
        card = Card(Seed.tarots, 0)
        self.player_1.add_won_card(card)
        print(self.player_1.won_cards.cards)
        self.team.update_team_won_cards()
        self.assertIn(card, self.team.won_cards.cards)

    def test_team_update_players_won_cards(self):
        card = Card(Seed.tarots, 0)
        self.team.add_card(card)
        self.team.update_players_won_cards()
        self.assertIn(card, self.player_1.won_cards.cards)
        self.assertIn(card, self.player_2.won_cards.cards)

    def test_team_set_debt(self):
        self.player_1.asking = True
        self.team.set_debt()
        self.assertEqual(self.player_1.debt, 63)
        self.assertEqual(self.player_2.debt, 57)

if __name__ == '__main__':
    unittest.main()
