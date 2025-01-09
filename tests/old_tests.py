from tarots import Card, CardRound, PlayedCard, Seed, Deck, Game, Player

def test1() -> None:      


    c = [Card.random() for _ in range(7)]


    for i in range(6):
        ci = c[i]
        for j in range(6):
            cj = c[j+1]
            print(f"comparing {ci} and {cj}")
            print(Card.compare_cards(ci,cj))
            print("#"*10)
   
    return None

def test2() -> None:

    t = CardRound.random(5)

    print(t)

    print("\n")

    winner = t.winner
    print(f"winner is {winner}")

    return None

def test3() -> None:
    c = [Card.random() for _ in range(7)]

    c = PlayedCard.random_ordering(c)

    for ci in c:
        print(ci)

    print("\n")
    print("#"*10)
    print("now sorted\n")

    c.sort()
    for ci in c:
        print(ci)


    return None

def test4() -> None:

    c1 = PlayedCard(seed=Seed.spades, number=5, order=0)
    c2 = PlayedCard(seed=Seed.clubs, number=7, order=1)    

    c = [c1,c2]
    c.sort()

    print(f"{c}")

    return None

def test5() -> None:

    c = Card.random(10)
    print(c)

    cgroup = Card.group_cards(c)
    print(cgroup)

def test6() -> None:

    d = Deck.standard()
    print(d)

    d.shuffle()
    print(d)

    num_players = 3
    hands, prize = d.deal(num_players)
    for i,hand in enumerate(hands):
        print("\n")
        print("#"*10)
        print(f"player {i+1} hand: {hand}")
        print("The value of the hand is: ", hand.value)

    print("\n")
    print("#"*10)
    print(f"prize: {prize}")

def big_test() -> None:

    names5 = ["Nenno", "Tziu", "Bolly", "Macchia", "Su Bugginu"]

    names = ["Bolly", "Macchia", "Su Bugginu"]

    players = [Player(name) for name in names]

    game = Game(players)

    game.setup_game()
    

    #d = Deck.standard()

    #debts = game.debts
    #print(debts)

    

   # for player in game.players:
     #   print(f"{player.name} debt = {player.debt}")


    #for player in game.players:
      #  print("#"*10)
       # print(f"{player.name} score = {player.score}")
        #print(f"{player.won_cards_value_notation}")



    return None

def test_round() -> None:

    
    game = Game.placeholder()
    game.setup_game()

    players = game.players


    return None

def test_print_hand_output() -> None:
    """
    Test the output of print(hand).
    """
    d = Deck.standard()
    d.shuffle()
    
    num_players = 3
    hands, prize = d.deal(num_players)
    
    for i, hand in enumerate(hands):
        print(f"\nPlayer {i+1} hand:")
        print(hand)
        print(f"The value of the hand is: {hand.value}")

    print("\nPrize:")
    print(prize)

def main():
    test_print_hand_output()

if __name__ == "__main__":
    main()