from __future__ import annotations
from typing import List
from enum import Enum
import random as rnd


class Seed(Enum):
    """
    The Seed class represents a type of card in a tarot deck. It includes methods for comparison and conversion between notation strings and Seed instances.

    Attributes:
        tarots (int):   Represents the tarot cards.
        spades (int):   Represents the spades suit.
        coins (int):    Represents the coins suit.
        clubs (int):    Represents the clubs suit.
        cups (int):     Represents the cups suit.
    """

    tarots = 0
    spades = 1
    coins = 2
    clubs = 3
    cups = 4

    def __lt__(self, other):
        """
        Compares if the value of the current Seed instance is less than the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is less than the other Seed instance, False otherwise.

        Example:
            >>> Seed.spades < Seed.coins
            True
        """
        return self.value < other.value

    def __le__(self, other):
        """
        Compares if the value of the current Seed instance is less than or equal to the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is less than or equal to the other Seed instance, False otherwise.

        Example:
            >>> Seed.spades <= Seed.coins
            True
        """
        return self.value <= other.value

    def __gt__(self, other):
        """
        Compares if the value of the current Seed instance is greater than the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is greater than the other Seed instance, False otherwise.

        Example:
            >>> Seed.coins > Seed.spades
            True
        """
        return self.value > other.value

    def __ge__(self, other):
        """
        Compares if the value of the current Seed instance is greater than or equal to the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is greater than or equal to the other Seed instance, False otherwise.

        Example:
            >>> Seed.coins >= Seed.spades
            True
        """
        return self.value >= other.value

    def __eq__(self, other):
        """
        Compares if the value of the current Seed instance is equal to the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is equal to the other Seed instance, False otherwise.

        Example:
            >>> Seed.spades == Seed.spades
            True
        """
        return self.value == other.value

    def __ne__(self, other):
        """
        Compares if the value of the current Seed instance is not equal to the value of another Seed instance.

        Parameters:
            other (Seed): The other Seed instance to compare with.

        Returns:
            bool: True if the current Seed instance is not equal to the value of another Seed instance, False otherwise.

        Example:
            >>> Seed.spades != Seed.coins
            True
        """
        return self.value != other.value

    def __str__(self):
        """
        Returns the name of the Seed instance.

        Returns:
            str: The name of the Seed instance.

        Example:
            >>> str(Seed.spades)
            'spades'
        """
        return self.name

    def __repr__(self):
        """
        Returns the name of the Seed instance.

        Returns:
            str: The name of the Seed instance.

        Example:
            >>> repr(Seed.spades)
            'spades'
        """
        return self.name

    def __hash__(self):
        """
        Returns the hash value of the Seed instance.

        Returns:
            int: The hash value of the Seed instance.

        Example:
            >>> hash(Seed.spades)
            1
        """
        return hash(self.value)

    @property
    def notation(self) -> str:
        """
        Returns the notation string of the Seed instance.

        Returns:
            str: The notation string of the Seed instance.

        Example:
            >>> Seed.spades.notation
            's'
        """
        return Seed.value_to_notation(self.value)

    @classmethod
    def value_to_notation(cls, value: int) -> str:
        """
        Converts a Seed value to its corresponding notation string.

        Parameters:
            value (int): The value of the Seed instance.

        Returns:
            str: The notation string corresponding to the Seed value.

        Example:
            >>> Seed.value_to_notation(1)
            's'
        """
        notation_map = {
            0: 't', #tarots
            1: 's', #spades
            2: 'o', #coins
            3: 'c', #clubs
            4: 'u'  #cups
        }
        return notation_map.get(value, "Unknown")

    @classmethod
    def from_notation(cls, text: str) -> Seed:
        """
        Converts a notation string to its corresponding Seed instance.

        Parameters:
            text (str): The notation string.

        Returns:
            Seed: The Seed instance corresponding to the notation string.

        Example:
            >>> Seed.from_notation('s')
            Seed.spades
        """

        notation_map = {
            't': Seed.tarots,
            's': Seed.spades,
            'o': Seed.coins,
            'c': Seed.clubs,
            'u': Seed.cups
        }

        try:
            return notation_map[text]
        except KeyError:
            raise ValueError(f"Invalid notation: {text}")


class Card:
    """
    Represents a playing card with a seed (suit) and a number.
    Attributes:
        seed (Seed): The suit of the card.
        number (int): The number or rank of the card.
    Methods:
        __repr__(): Returns a string representation of the card.
        __str__(): Returns a string representation of the card.
        notation(): Returns the notation of the card.
        random(): Generates a random card.
        __eq__(other): Checks if two cards are equal.
        __ne__(other): Checks if two cards are not equal.
        __lt__(other): Checks if one card is less than another.
        __le__(other): Checks if one card is less than or equal to another.
        __gt__(other): Checks if one card is greater than another.
        __ge__(other): Checks if one card is greater than or equal to another.
        value(): Returns the value of the card.
    """

    def __init__(self, seed: Seed, number):
        self.seed = seed
        self.number = number

        pass

    def __repr__(self):   

        if self.seed == Seed.tarots:
            
            tarot_name = self.tarot_name(self.number)
            return f"{self.number}: {tarot_name}"
        
        if self.number == 1:
            return f"Ace of {self.seed.name}"
        if self.number == 11:
            return f"Knight of {self.seed.name}"
        if self.number == 12:
            return f"Jack of {self.seed.name}"
        if self.number == 13:
            return f"Queen of {self.seed.name}"
        if self.number == 14:
            return f"King of {self.seed.name}"
    
        return f"{self.number} of {self.seed.name}"
        
    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.seed, self.number))

    @classmethod
    def tarot_name(cls, number: int) -> str:
        tarot_names = {
                0:  "The Fool",
                1:  "The Magician",
                2:  "The High Priestess",
                3:  "The Empress",
                4:  "The Emperor",
                5:  "The Hierophant",
                6:  "The Lovers",
                7:  "The Chariot",
                8:  "The Strength",
                9:  "The Hermit",
                10: "The Wheel of Fortune",
                11: "The Justice",
                12: "The Hanged Man",
                13: "The Death",
                14: "The Temperance",
                15: "The Devil",
                16: "The Tower",
                17: "The Star",
                18: "The Moon",
                19: "The Sun",
                20: "The Judgement",
                21: "The World"
            }
        return tarot_names.get(number, "Unknown")


    @property
    def notation(self):
        """
        Returns a string representation of the card's notation.

        The notation is composed of the card's number followed by the seed's notation.

        Returns:
            str: The notation of the card.
        Example:
            >>> card = Card(Seed.spades, 5)
            >>> card.notation
            '5s'
        """
        return f"{self.number}{self.seed.notation}"

    @classmethod
    def random(cls) -> Card:
        """
        Generate a random Card instance.

        This method selects a random seed from the Seed enumeration. If the selected
        seed is Seed.tarots, it generates a random number between 0 and 21 (inclusive).
        Otherwise, it generates a random number between 1 and 14 (inclusive).

        Returns:
            Card: A Card instance with the randomly selected seed and number.
        """

        seed = rnd.choice(list(Seed))
        if seed == Seed.tarots:
            number = rnd.randint(0, 21)
        else:
            number = rnd.randint(1, 14)
        return Card(seed, number)
       
    def __eq__(self, other: Card) -> bool:
        return self.seed == other.seed and self.number == other.number

    def __ne__(self, other: Card) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: Card) -> bool:
        """
        Compare two card objects to determine if the current card is less than the other card.
        The comparison is based on the following rules:
        1. If the cards are the same, return False.
        2. If the current card is a tarots card and the other card is not, return False.
        3. If both cards are tarots cards, compare their numbers.
        4. If the other card is a tarots card and the current card is not, return True.
        5. If the cards have different seeds, compare their seeds.
        6. If one or both cards are figures (number > 10), compare their numbers.
        7. If the seed is cups or coins, compare their numbers in reverse order.
        8. For all other cases, compare their numbers.
        
        Args:
            other (Card): The card to compare against.
        
        Returns:
            bool: True if the current card is less than the other card, False otherwise.
        
        Examples:
            >>> card1 = Card(seed=Seed.tarots, number=5)
            >>> card2 = Card(seed=Seed.spades, number=3)
            >>> card1 < card2  
            False

            >>> card1 = Card(seed=Seed.spades, number=5)
            >>> card2 = Card(seed=Seed.coins, number=7)
            >>> card1 < card2
            True

            >>> card1 = Card(seed=Seed.cups, number=8)
            >>> card2 = Card(seed=Seed.cups, number=5)
            >>> card1 < card2 
            False
        """

        if self == other: #if the cards are the same
            return False
        if self.seed == Seed.tarots: #if self is a tarots card
            if other.seed != Seed.tarots: #if the other card is not a tarots card
                return False
            return self.number < other.number #if the other card is a tarots card and higher
            

        if other.seed == Seed.tarots: #if the other card is a tarots card and self is not
            return True

        if self.seed != other.seed: #if the second card is not the same seed as the first
            return self.seed < other.seed

        if self.number > 10 or other.number > 10: #if one or both cards are figures
            return self.number < other.number

        if self.seed in [Seed.cups, Seed.coins]: #if the seed is cups or coins
            return self.number > other.number

        return self.number < other.number
        
    def __le__(self, other: Card) -> bool:
        """
        Check if this card is less than or equal to another card.
        This method compares the current card with another card to determine if it is less than or equal to the other card.
        Args:
            other (Card): The card to compare against.
        Returns:
            bool: True if this card is less than or equal to the other card, False otherwise.
        Examples:
            >>> card1 = Card(Seed.spades, 2)
            >>> card2 = Card(Seed.spades, 3)
            >>> card1 <= card2
            True
            >>> card1 = Card(Seed.spades, 3)
            >>> card2 = Card(Seed.spades, 3)
            >>> card1 <= card2
            True
            >>> card1 = Card(Seed.spades, 4)
            >>> card2 = Card(Seed.spades, 3)
            >>> card1 <= card2
            False
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: Card) -> bool:
        """
        Determine if this card is greater than another card.
        This method checks if this card is greater than the other card by 
        comparing their ranks. It returns True if this card is greater, 
        otherwise False.
        Args:
            other (Card): The card to compare against.
        Returns:
            bool: True if this card is greater than the other card, False otherwise.
        Examples:
            >>> card1 = Card(seed=Seed.spades, number=10)
            >>> card2 = Card(seed=Seed.hearts, number=5)
            >>> card1 > card2
            True
            >>> card3 = Card(seed=Seed.diamonds, number=3)
            >>> card3 > card1
            False
        """

        return not self.__le__(other)

    def __ge__(self, other: Card) -> bool:
        """
        Check if this card is greater than or equal to another card.
        Args:
            other (Card): The card to compare against.
        Returns:
            bool: True if this card is greater than or equal to the other card, False otherwise.
        Examples:
            >>> card1 = Card(Seed.spades, 14)
            >>> card2 = Card(Seed.cups, 13)
            >>> card1 >= card2
            True
            >>> card3 = Card(Seed.coins, 12)
            >>> card2 >= card3
            False
        """

        return not self.__lt__(other)

    @property
    def value(self) -> int:
        """
        Calculate the value of the card based on its number and seed.
        Returns:
            int: The value of the card.
        Examples:
            >>> card = Card(number=0, seed=Seed.tarots)
            >>> card.value()
            12
            >>> card = Card(number=1, seed=Seed.tarots)
            >>> card.value()
            13
            >>> card = Card(number=20, seed=Seed.tarots)
            >>> card.value()
            13
            >>> card = Card(number=5, seed=Seed.tarots)
            >>> card.value()
            1
            >>> card = Card(number=11, seed=Seed.hearts)
            >>> card.value()
            4
            >>> card = Card(number=9, seed=Seed.spades)
            >>> card.value()
            1
        """

        number = self.number

        if number == 0: #if the card is the fool
            return 12
        
        if self.seed == Seed.tarots: #if the card is a tarot
            return 13 if number in [1, 21] else 1
        
        if number > 10: #if the card is a figure
                return (number - 9)*3 - 2

        return 1 

class Hand:
    """
    A class to represent a hand of cards.
    Attributes:
    ----------
    cards : list[Card]
        A list of Card objects representing the hand.
    Methods:
    -------
    __init__(cards: list[Card]):
        Initializes the Hand with a list of cards.
    __repr__() -> str:
        Returns a string representation of the hand.
    __add__(other: Hand) -> Hand:
        Adds two hands together and returns a new Hand.
    __iter__():
        Returns an iterator for the hand.
    __len__():
        Returns the number of cards in the hand.
    __getitem__(key):
        Returns the card at the specified index.
    __setitem__(key, value):
        Sets the card at the specified index.
    __delitem__(key):
        Deletes the card at the specified index.
    random(cls, num: int) -> Hand:
        Generates a hand with a specified number of random cards.
    cards_of_seed(seed: Seed) -> Hand:
        Returns a new Hand containing only the cards of the specified seed.
    max_card_of_seed(seed: Seed) -> Card:
        Returns the highest card of the specified seed.
    min_card_of_seed(seed: Seed) -> Card:
        Returns the lowest card of the specified seed.
    add_card(card: Card) -> None:
        Adds a card to the hand and sorts the hand.
    add_cards(cards: List[Card]) -> None:
        Adds multiple cards to the hand and sorts the hand.
    remove_card(card: Card) -> None:
        Removes a card from the hand and sorts the hand.
    remove_cards(cards: List[Card]) -> None:
        Removes multiple cards from the hand and sorts the hand.
    has_card(card: Card) -> bool:
        Checks if the hand contains the specified card.
    has_cards(cards: List[Card]) -> bool:
        Checks if the hand contains all the specified cards.
    has_seed(seed: Seed) -> bool:
        Checks if the hand contains any card of the specified seed.
    has_seeds(seeds: List[Seed]) -> bool:
        Checks if the hand contains cards of all the specified seeds.
    value() -> int:
        Returns the total value of the hand.
    group_cards() -> dict[Seed, List[Card]]:
        Groups the cards by their seed and returns a dictionary.
    notation() -> str:
        Returns a string notation of the hand.
    empty(cls) -> Hand:
        Returns an empty hand.
    exchange_cards(cls, hand_1: Hand, hand_2: Hand, card_1: Card, card_2: Card) -> None:
        Exchanges specified cards between two hands.
    """


    def __init__(self, cards: list[Card]):
        self.cards = sorted(cards, reverse=True)
        pass

    def __repr__(self) -> str:
        return f"{self.cards}"
    
    def __add__(self, other: Hand) -> Hand:
        """
        Adds the cards from another Hand to this Hand, removes duplicates, and returns a new Hand.
        
        Args:
            other (Hand): The other Hand to add.
        
        Returns:
            Hand: A new Hand containing the combined cards from both Hands without duplicates.
        
        Example:
            >>> hand1 = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> hand2 = Hand([Card(Seed.coins, 12), Card(Seed.clubs, 11), Card(Seed.spades, 1)])
            >>> combined_hand = hand1 + hand2
            >>> print(combined_hand.cards)
            [1 of spades, 13 of cups, 12 of coins, 11 of clubs]
        """
        new_cards = self.cards + other.cards
        unique_cards = []
        seen = set()
        for card in new_cards:
            if (card.seed, card.number) not in seen:
                unique_cards.append(card)
                seen.add((card.seed, card.number))
        return Hand(unique_cards)

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]
 
    def __hash__(self):
        return hash(tuple(self.cards))

    @classmethod
    def random(cls, num: int) -> Hand:
        """
        Generate a random hand of cards.
        This method generates a specified number of random cards, ensuring that
        no duplicate cards are included in the hand.
        Args:
            num (int): The number of random cards to generate.
        Returns:
            Hand: A hand containing the specified number of unique random cards.
        Example:
            >>> hand = Hand.random(3)
            >>> print(hand)
            [Card(Seed.spades, 5), Card(Seed.cups, 10), Card(Seed.coins, 3)]
        """

        cards = []
        while len(cards) < num:
            card = Card.random()
            if card not in cards:
                cards.append(card)
        return Hand(cards)

    def cards_of_seed(self, seed: Seed) -> Hand:
        """
        Retrieve all cards of a specific seed from the hand.
        Args:
            seed (Seed): The seed to filter cards by.
        Returns:
            Hand: A hand containing all cards of the specified seed.
        Example:
            >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cups_hand = hand.cards_of_seed(Seed.cups)
            >>> print(cups_hand)
            [Card(Seed.cups, 13)]
        """

        return Hand([card for card in self.cards if card.seed == seed])

    def max_card_of_seed(self, seed: Seed) -> Card:
        """
        Returns the card with the maximum value of the specified seed.
        Args:
            seed (Seed): The seed for which the maximum card is to be found.
        Returns:
            Card: The card with the highest value of the specified seed.
        Example:
            >>> hand = Hand([Card(Seed.tarots, 1), Card(Seed.tarots, 13)])
            >>> max_card = hand.max_card_of_seed(Seed.tarots)
            >>> print(max_card)
            13: The Death
        """

        return max(self.cards_of_seed(seed))

    def min_card_of_seed(self, seed: Seed) -> Card:
        """
        Returns the card with the minimum value of the specified seed.
        Args:
            seed (Seed): The seed for which the minimum card is to be found.
        Returns:
            Card: The card with the lowest value of the specified seed.
        Example:
            >>> hand = Hand([Card(Seed.tarots, 1), Card(Seed.tarots, 13)])
            >>> min_card = hand.min_card_of_seed(Seed.tarots)
            >>> print(min_card)
            1: The Magician
        """
        return min(self.cards_of_seed(seed))
    
    def add_card(self, card: Card) -> None:
        """
        Add a card to the hand and sort the cards in descending order.
        Args:
            card (Card): The card to be added to the hand.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([])
            >>> hand.add_card(card1)
            >>> hand.add_card(card2)
            >>> print(hand)
            [13 of cups, 1 of spades]
        """
        
        self.cards.append(card)
        self.cards.sort(reverse=True)

    def add_cards(self, cards: List[Card]) -> None:
        """
        Add a list of Card objects to the current list of cards and sort them in descending order.
        Args:
            cards (List[Card]): A list of Card objects to be added.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([])
            >>> hand.add_cards([card1, card2])
            >>> print(hand)
            [13 of cups, 1 of spades]
        """
        
        self.cards.extend(cards)
        self.cards.sort(reverse=True)

    def remove_card(self, card: Card) -> None:
        """
        Remove a card from the hand and sort the remaining cards in descending order.
        Args:
            card (Card): The card to be removed from the hand.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.remove_card(card1)
            >>> print(hand)
            [13 of cups]
        """
        self.cards.remove(card)
        self.cards.sort(reverse=True)

    def remove_cards(self, cards: List[Card]) -> None:
        """
        Remove multiple cards from the hand and sort the remaining cards in descending order.
        Args:
            cards (List[Card]): A list of Card objects to be removed from the hand.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.remove_cards([card1, card2])
            >>> print(hand)
            []
        """

        for card in cards:
            self.cards.remove(card)
        self.cards.sort(reverse=True)

    def has_card(self, card: Card) -> bool:
        """
        Check if the hand contains a specific card.
        Args:
            card (Card): The card to check for in the hand.
        Returns:
            bool: True if the hand contains the card, False otherwise.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.has_card(card1)
            True
        """
        return card in self.cards

    def has_cards(self, cards: List[Card]) -> bool:
        """
        Check if the hand contains multiple cards.
        Args:
            cards (List[Card]): A list of cards to check for in the hand.
        Returns:
            bool: True if the hand contains all the cards, False otherwise.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.has_cards([card1, card2])
            True
        """
        return all(card in self.cards for card in cards)

    def has_seed(self, seed: Seed) -> bool:
        """
        Check if the hand contains any cards of a specific seed.
        Args:
            seed (Seed): The seed to check for in the hand.
        Returns:
            bool: True if the hand contains any cards of the seed, False otherwise.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.has_seed(Seed.spades)
            True
        """
        return any(card.seed == seed for card in self.cards)

    def has_seeds(self, seeds: List[Seed]) -> bool:
        """
        Check if the hand contains cards of all the specified seeds.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the hand.
        Returns:
            bool: True if the hand contains cards of all the seeds, False otherwise.
        Example:
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.cups, 13)
            >>> hand = Hand([card1, card2])
            >>> hand.has_seeds([Seed.spades, Seed.cups])
            True
        """
        return all(any(card.seed == seed for card in self.cards) for seed in seeds)

    @property
    def value(self) -> int:
        """
        Calculate the total value of the cards in the hand.
        Returns:
            int: The total value of the cards in the hand.
        Example:
            >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> hand.value
            14
        """
        return sum(card.value for card in self.cards)

    @property
    def group_cards(self) -> dict[Seed, List[Card]]:
        """
        Group the cards in the hand by their seed.
        Returns:
            dict[Seed, List[Card]]: A dictionary where the keys are the seeds and the values are lists of cards.
        Example:
            >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13), Card(Seed.spades, 5)])
            >>> groups = hand.group_cards
            >>> print(groups)
            {Seed.spades: [1 of spades, 5 of spades], Seed.cups: [13 of cups]}
        """
        groups = {seed: [] for seed in Seed}
        for card in self.cards:
            groups[card.seed].append(card)
        return groups
    
    @property
    def notation(self) -> str:
        """
        Return a string notation of the hand.
        The notation is a string representation of the cards in the hand grouped by their seed.
        Returns:
            str: A string notation of the hand.
        Example:
            >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13), Card(Seed.spades, 5)])
            >>> hand.notation
            's:[[1, 5], [13]]\nc:[[13]]\n'
        """
        if not self.cards:
            return ""
        
        groups = self.group_cards

        text = ""
        for seed, cards in groups.items():
            if cards:
                text += f"{seed.notation}:[{', '.join(str(card.number) for card in cards)}]\n"
        return text

    @classmethod
    def empty(cls) -> Hand:
        """
        Return an empty hand.
        Returns:
            Hand: An empty hand.
        Example:
            >>> hand = Hand.empty()
            >>> print(hand)
            []
        """
        return Hand([])

    @classmethod
    def exchange_cards(cls, hand_1: Hand, hand_2: Hand, card_1: Card, card_2: Card) -> None:
        """
        Exchange two cards between two hands.
        This method removes the specified cards from the hands and adds them to the other hand.
        Args:
            hand_1 (Hand): The first hand to exchange cards with.
            hand_2 (Hand): The second hand to exchange cards with.
            card_1 (Card): The card to exchange from the first hand.
            card_2 (Card): The card to exchange from the second hand.
        Example:
            >>> hand1 = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> hand2 = Hand([Card(Seed.coins, 12), Card(Seed.clubs, 11)])
            >>> card1 = Card(Seed.spades, 1)
            >>> card2 = Card(Seed.coins, 12)
            >>> Hand.exchange_cards(hand1, hand2, card1, card2)
            >>> print(hand1)
            [13 of cups, 12 of coins]
            >>> print(hand2)
            [11 of clubs, 1 of spades]
            """

        hand_1.remove_card(card_1)
        hand_1.add_card(card_2)
        hand_2.remove_card(card_2)
        hand_2.add_card(card_1)        
        
        return None

    @property
    def is_empty(self) -> bool:
        """
        Check if the hand is empty.
        Returns:
            bool: True if the hand is empty, False otherwise.
        Example:
            >>> hand = Hand([])
            >>> hand.is_empty
            True
        """
        return not bool(self.cards)

    def sort(self) -> Hand:
        """
        Return a new Hand with the cards sorted in descending order.
        Returns:
            Hand: A new Hand with the cards sorted in descending order.
        Example:
            >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13), Card(Seed.spades, 5)])
            >>> sorted_hand = hand.sorted()
            >>> print(sorted_hand)
            [13 of cups, 5 of spades, 1 of spades]
        """
        return Hand(sorted(self.cards, reverse=True))   

    def clear(self) -> None:
        """
        Remove all cards from the hand.
        Example:
        >>> hand = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13), Card(Seed.spades, 5)])
        >>> hand.clear()
        >>> print(hand)
        []
        """
        self.cards.clear()

class Deck:
    """
    A class representing a deck of cards.
    Attributes:
        cards (List[Card]): A list of Card objects representing the deck.
    Methods:
        __init__(cards: List[Card]):
            Initializes the Deck with a list of cards.
        __repr__():
            Returns a string representation of the deck.
        __iter__():
            Returns an iterator for the deck.
        __len__():
            Returns the number of cards in the deck.
        __getitem__(key):
            Returns the card at the specified index.
        __setitem__(key, value):
            Sets the card at the specified index.
        __delitem__(key):
            Deletes the card at the specified index.
        standard() -> Deck:
            Creates a standard deck of cards.
        shuffle():
            Shuffles the deck.
        draw(num: int) -> List[Card]:
            Draws a specified number of cards from the deck.
        draw_card() -> Card:
            Draws a single card from the deck.
        draw_hand(num: int) -> Hand:
            Draws a specified number of cards and returns them as a Hand.
        shuffle_draw(num: int) -> list[Card]:
            Shuffles the deck and draws a specified number of cards.
        deal(num_players: int) -> list[list[Hand], list[Card]]:
            Deals cards to a specified number of players and returns the hands and prize.
        group_cards() -> dict[Seed, List[Card]]:
            Groups the cards by their seed and returns a dictionary.
        notation() -> str:
            Returns a string notation of the deck.
        add_card(card: Card) -> None:
            Adds a card to the deck.
        add_cards(cards: List[Card]) -> None:
            Adds multiple cards to the deck.
        remove_card(card: Card) -> None:
            Removes a card from the deck.
        remove_cards(cards: List[Card]) -> None:
            Removes multiple cards from the deck.
        has_card(card: Card) -> bool:
            Checks if a card is in the deck.
        has_cards(cards: List[Card]) -> bool:
            Checks if multiple cards are in the deck.
        has_seed(seed: Seed) -> bool:
            Checks if the deck contains any cards of the specified seed.
        has_seeds(seeds: List[Seed]) -> bool:
            Checks if the deck contains cards of all the specified seeds.
        value() -> int:
            Returns the total value of the cards in the deck.
        sorted() -> Deck:
            Returns a new Deck with the cards sorted.
        reversed() -> Deck:
            Returns a new Deck with the cards in reverse order.
    """


    def __init__(self, cards: List[Card]):
        """
        Initialize the Tarot deck with a list of cards.
        Args:
            cards (List[Card]): A list of Card objects representing the tarot deck.
        """

        self.cards = cards
        pass

    def __repr__(self):
        """
        Return a string representation of the deck.
        Returns:
            str: A string representation of the deck.
        Example:
            >>> deck = Deck.standard()
            >>> print(deck)
            [0: The Fool, 1: The Magician, 2: The High Priestess, ..., 13 of coins, 14 of coins, ..., 14 of swords]
        """
        return f"{self.cards}"

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def __eq__(self, other: Deck) -> bool:
        """
        Check if two decks are equal.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if the decks are equal, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 == deck2
            True
        """
        if isinstance(other, Deck):
            return self.cards == other.cards
        return False

    def __ne__(self, other: Deck) -> bool:
        """
        Check if two decks are not equal.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if the decks are not equal, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 != deck2
            False
        """
        return not self.__eq__(other)
    
    def __lt__(self, other: Deck) -> bool:
        """
        Check if this deck is less than another deck.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if this deck is less than the other deck, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 < deck2
            False
        """
        return self.cards < other.cards
    
    def __le__(self, other: Deck) -> bool:
        """
        Check if this deck is less than or equal to another deck.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if this deck is less than or equal to the other deck, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 <= deck2
            True
        """
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other: Deck) -> bool:
        """
        Check if this deck is greater than another deck.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if this deck is greater than the other deck, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 > deck2
            False
        """
        return not self.__le__(other)
    
    def __ge__(self, other: Deck) -> bool:
        """
        Check if this deck is greater than or equal to another deck.
        Args:
            other (Deck): The other deck to compare against.
        Returns:
            bool: True if this deck is greater than or equal to the other deck, False otherwise.
        Example:
            >>> deck1 = Deck.standard()
            >>> deck2 = Deck.standard()
            >>> deck1 >= deck2
            True
        """
        return not self.__lt__(other)
    
    def __hash__(self):
        return hash(tuple(self.cards))

    @classmethod
    def standard(cls) -> Deck:
        """
        Create a standard deck of cards.
        Returns:
            Deck: A standard deck of cards.
        Example:
            >>> deck = Deck.standard()
            >>> print(deck)
            [0: The Fool, 1: The Magician, 2: The High Priestess, ..., 13 of coins, 14 of coins, ..., 14 of swords]
        """

        cards = []
        for seed in Seed:

            if seed == Seed.tarots:
                cards.extend([Card(seed, number) for number in range(22)])
            else:
                cards.extend([Card(seed, number) for number in range(1, 15)])
        return Deck(cards)
    
    def shuffle(self):
       
        """
        Shuffle the deck.
        This method shuffles the cards in the deck in random order.
        Example:
        >>> deck = Deck.standard()
        >>> deck.shuffle()
        >>> print(deck)
        [13 of coins, 4 of spades, 1 of cups, ..., 14 of swords]
        """
        
        rnd.shuffle(self.cards)

    def draw(self, num: int) -> List[Card]:
        """
        Draw a specified number of cards from the deck.
        Args:
            num (int): The number of cards to draw.
        Returns:
            List[Card]: A list of Card objects drawn from the deck.
        Example:
            >>> deck = Deck.standard()
            >>> drawn = deck.draw(3)
            >>> print(drawn)
            [0: The Fool, 1: The Magician, 2: The High Priestess]
        """

        drawn = self.cards[:num]
        self.cards = self.cards[num:]
        
        return drawn

    def draw_card(self) -> Card:
        """
        Draw a single card from the deck.
        Returns:
            Card: A Card object drawn from the deck.
        Example:
            >>> deck = Deck.standard()
            >>> card = deck.draw_card()
            >>> print(card)
            0: The Fool
        """
        return self.draw(1)[0]

    def draw_hand(self, num: int) -> Hand:
        """
        Draw a specified number of cards and return them as a Hand.
        Args:
            num (int): The number of cards to draw.
        Returns:
            Hand: A Hand containing the drawn cards.
        Example:
            >>> deck = Deck.standard()
            >>> hand = deck.draw_hand(3)
            >>> print(hand)
            [0: The Fool, 1: The Magician, 2: The High Priestess]
        """

        return Hand(self.draw(num))
    
    def shuffle_draw(self, num: int) -> list[Card]:
        """
        Shuffle the deck and draw a specified number of cards.
        Args:
            num (int): The number of cards to draw.
        Returns:
            list[Card]: A list of Card objects drawn from the deck.
        Example:
            >>> deck = Deck.standard()
            >>> drawn = deck.shuffle_draw(3)
            >>> print(drawn)
            [13 of coins, 4 of spades, 1 of cups]
        """
        self.shuffle()

        return self.draw(num)

    def deal(self, num_players: int) -> tuple[list[Hand], Hand]:
        """
        Deal cards to a specified number of players.
        This method deals cards to a specified number of players and returns the hands and the prize.
        If the number of players is 4, each player receives 4 cards initially and the prize is 2 cards.
        If the number of players is 3 or 5, each player receives 5 cards initially and the prize is 3 cards.
        Args:
            num_players (int): The number of players to deal cards to.
        Returns:
            list[list[Hand], list[Card]]: A list containing the hands of the players and the prize.
        Example:
            >>> deck = Deck.standard()
            >>> hands, prize = deck.deal(4)
            >>> print(hands)
            [[0: The Fool, ...], ...]
            >>> print(prize)
            [13 of coins, 4 of spades, 1 of cups]
        """

        if num_players < 3 or num_players > 5:
            raise ValueError("Number of players must be between 3 and 5")

        if num_players == 4: #if there are 4 players
            prize_draw = 2
            initial_draw = 4
        else: #if there are 3 or 5 players
            prize_draw = 3
            initial_draw = 5

        prize = self.draw_hand(prize_draw) #draw the prize
        hands = [self.draw_hand(initial_draw) for _ in range(num_players)] #draw the initial

        #draw 5 cards per player until the deck is empty
        while self.cards:
            for hand in hands:
                hand.add_cards(self.draw(5))

        return hands, prize

    @property
    def group_cards(self) -> dict[Seed, List[Card]]:
        """
        Group the cards in the deck by their seed.
        Returns:
            dict[Seed, List[Card]]: A dictionary where the keys are the seeds and the values are lists of cards.
        Example:
            >>> deck = Deck.standard()
            >>> groups = deck.group_cards
            >>> print(groups)
            {Seed.spades: [1 of spades, 2 of spades, ..., 14 of spades], Seed.cups: [1 of cups, 2 of cups, ..., 14 of cups], ...}
        """

        groups = {seed: [] for seed in Seed}
        for card in self.cards:
            groups[card.seed].append(card)
        return groups
    
    @property
    def notation(self) -> str:
        """
        Return a string notation of the deck.
        The notation is a string representation of the cards in the deck grouped by their seed.
        Returns:
            str: A string notation of the deck.
        Example:
            >>> deck = Deck.standard()
            >>> print(deck.notation)
            's:[[1, 2, ..., 14], [1, 2, ..., 14], ...]\nc:[[1, 2, ..., 14], [1, 2, ..., 14], ...]\n...'
        """

        if not self.cards:
            return ""

        groups = self.group_cards

        text = ""
        for seed, cards in groups.items():
            if cards:
                text += f"{seed.notation}:[{', '.join(str(card.number) for card in cards)}]\n"
        return text

    @classmethod
    def empty(cls) -> Deck:
        """
        Return an empty deck.
        Returns:
            Deck: An empty deck.
        Example:
            >>> deck = Deck.empty()
            >>> print(deck)
            []
        """
        return Deck([])

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.
        Args:
            card (Card): The card to add to the deck.
        Example:
            >>> deck = Deck.empty()
            >>> card = Card(Seed.spades, 1)
            >>> deck.add_card(card)
            >>> print(deck)
            [1 of spades]
        """
        self.cards.append(card)

    def add_cards(self, cards: List[Card]) -> None:
        """
        Add multiple cards to the deck.
        Args:
            cards (List[Card]): A list of cards to add to the deck.
        Example:
            >>> deck = Deck.empty()
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> deck.add_cards(cards)
            >>> print(deck)
            [1 of spades, 13 of cups]
        """
        self.cards.extend(cards)    

    def remove_card(self, card: Card) -> None:
        """
        Remove a card from the deck.
        Args:
            card (Card): The card to remove from the deck.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = Card(Seed.spades, 1)
            >>> deck.remove_card(card)
            >>> print(deck)
            [13 of cups]
        """
        
        self.cards.remove(card)

    def remove_cards(self, cards: List[Card]) -> None:
        """
        Remove multiple cards from the deck.
        Args:
            cards (List[Card]): A list of cards to remove from the deck.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> deck.remove_cards(cards)
            >>> print(deck)
            []
        """

        for card in cards:
            self.cards.remove(card)
    
    def has_card(self, card: Card) -> bool:
        """
        Check if the deck contains a specific card.
        Args:
            card (Card): The card to check for in the deck.
        Returns:
            bool: True if the deck contains the card, False otherwise.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = Card(Seed.spades, 1)
            >>> deck.has_card(card)
            True
        """
        return card in self.cards
    
    def has_cards(self, cards: List[Card]) -> bool:
        """
        Check if the deck contains multiple cards.
        Args:
            cards (List[Card]): A list of cards to check for in the deck.
        Returns:
            bool: True if the deck contains all the cards, False otherwise.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> deck.has_cards(cards)
            True
        """
        return all(card in self.cards for card in cards)
    
    def has_seed(self, seed: Seed) -> bool:
        """
        Check if the deck contains any cards of a specific seed.
        Args:
            seed (Seed): The seed to check for in the deck.
        Returns:
            bool: True if the deck contains any cards of the seed, False otherwise.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> deck.has_seed(Seed.spades)
            True
        """
        return any(card.seed == seed for card in self.cards)
    
    def has_seeds(self, seeds: List[Seed]) -> bool:
        """ 
        Check if the deck contains cards of all the specified seeds.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the deck.
        Returns:
            bool: True if the deck contains cards of all the seeds, False otherwise.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> deck.has_seeds([Seed.spades, Seed.cups])
            True
        """
        return all(any(card.seed == seed for card in self.cards) for seed in seeds)
    
    @property
    def value(self) -> int:
        """
        Calculate the total value of the cards in the deck.
        Returns:
            int: The total value of the cards in the deck.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> deck.value
            14
        """
        return sum(card.value for card in self.cards)
    
    @property
    def sorted(self) -> Deck:
        """
        Return a new Deck with the cards sorted.
        Returns:
            Deck: A new Deck with the cards sorted.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> sorted_deck = deck.sorted
            >>> print(sorted_deck)
            [13 of cups, 1 of spades]
        """
        return Deck(sorted(self.cards))
    
    @property
    def reversed(self) -> Deck:
        """
        Return a new Deck with the cards in reverse order.
        Returns:
            Deck: A new Deck with the cards in reverse order.
        Example:
            >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> reversed_deck = deck.reversed
            >>> print(reversed_deck)
            [1 of spades, 13 of cups]
        """
        return Deck(list(reversed(self.cards)))
    
    def sort(self) -> None:
        """
        Sort the cards in the deck.
        This method sorts the cards in the deck in ascending order.
        Example:
        >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
        >>> deck.sort()
        >>> print(deck)
        [1 of spades, 13 of cups]
        """
        self.cards.sort()

    def clear(self) -> None:
        """
        Remove all cards from the deck.
        Example:
        >>> deck = Deck([Card(Seed.spades, 1), Card(Seed.cups, 13)])
        >>> deck.clear()
        >>> print(deck)
        []
        """
        self.cards.clear()
       
        
class Player:
    """
    A class representing a player in a card game.
    Attributes:
        name (str): The name of the player.
        hand (Hand): The hand of cards held by the player.
        score (int): The score of the player.
        debt (int): The debt of the player.
        won_cards (Hand): The cards won by the player.
        asking (bool): A flag indicating if the player is asking for cards.
    Methods:
        __init__(name: str, hand: Hand): 
            Initializes the Player with a name and a hand of cards.
        __repr__():
            Returns a string representation of the player.
        __iter__():
            Returns an iterator for the player's hand.
        __getitem__(key):
            Returns the card at the specified index in the player's hand.
        __setitem__(key, value):
            Sets the card at the specified index in the player's hand.
        __delitem__(key):   
            Deletes the card at the specified index in the player's hand.
        add_card(card: Card):
            Add a card to the player's hand.
        add_cards(cards: List[Card]):
            Add multiple cards to the player's hand.
        remove_card(card: Card):
            Remove a card from the player's hand.
        remove_cards(cards: List[Card]):
            Remove multiple cards from the player's hand.
        has_card(card: Card) -> bool:
            Check if the player has a specific card.
        has_cards(cards: List[Card]) -> bool:
            Check if the player has multiple cards.
        has_seed(seed: Seed) -> bool:
            Check if the player has any cards of a specific seed.
        has_seeds(seeds: List[Seed]) -> bool:
            Check if the player has cards of all the specified seeds.
        reset_hand():
            Reset the player's hand to an empty hand.
        reset_won_cards():
            Reset the player's won cards to an empty hand.
        value() -> int:
            Calculate the total value of the cards in the player's hand.
        choose_card() -> Card:
            Choose a card to play.
        choose_own_card() -> Card:
            Choose a card from the player's hand.
        choice_bool() -> bool:
            Choose a boolean value.
        add_won_card(card: Card):
            Add a card to the player's won cards.
        add_won_cards(cards: List[Card]):
            Add multiple cards to the player's won cards.
        remove_won_card(card: Card):
            Remove a card from the player's won cards.
        remove_won_cards(cards: List[Card]):
            Remove multiple cards from the player's won cards.
        has_won_card(card: Card) -> bool:
            Check if the player has a specific card in their won cards.
        has_won_cards(cards: List[Card]) -> bool:
            Check if the player has multiple cards in their won cards.  
        has_won_seed(seed: Seed) -> bool:
            Check if the player has any cards of a specific seed in their won cards.
        has_won_seeds(seeds: List[Seed]) -> bool:
            Check if the player has cards of all the specified seeds in their won cards.
        update_score():
            Update the player's score based on their won cards and debt.
        hand_value_notation() -> dict:
            Return a dictionary of the player's hand cards grouped by their value.
        won_cards_value_notation() -> dict:
            Return a dictionary of the player's won cards grouped by their value.
        notation() -> str:
            Return a string notation of the player.
        exchange_cards(player_1: Player, player_2: Player, card_1: Card, card_2: Card):
            Exchange cards between two players.
        from_list(name_list: list[str]) -> list[Player]:
            Create a list of players from a list of names.
        placeholder(num: int) -> Player|list[Player]:
            Create a placeholder player or a list of placeholder players.
    """

    def __init__(self, name:str, hand: Hand = Hand.empty()):
        self.name = name
        self.hand = hand
        self.score = 0
        self.debt = 0
        self.won_cards = Hand.empty()
        self.asking = False

    def __repr__(self):
        return f"{self.name}"

    def __iter__(self):
        return iter(self.hand)

    def __getitem__(self, key):
        return self.hand[key]

    def __setitem__(self, key, value):
        self.hand[key] = value

    def __delitem__(self, key):
        del self.hand[key]

    def __eq__(self, other: Player) -> bool:
        """
        Check if two players are equal. 
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if the players are equal, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 10
            >>> player1 == player2
            True
        """
        return self.score == other.score

    def __ne__(self, other: Player) -> bool:
        """
        Check if two players are not equal.
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if the players are not equal, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 20
            >>> player1 != player2
            True
        """
        return not self.__eq__(other)
    
    def __lt__(self, other: Player) -> bool:
        """
        Check if this player is less than another player.
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if this player is less than the other player, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 20
            >>> player1 < player2
            True
        """
        return self.score < other.score

    def __le__(self, other: Player) -> bool:
        """
        Check if this player is less than or equal to another player.
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if this player is less than or equal to the other player, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 20
            >>> player1 <= player2
            True
        """
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other: Player) -> bool:
        """
        Check if this player is greater than another player.
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if this player is greater than the other player, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 20
            >>> player1 > player2
            False
        """
        return not self.__le__(other)
    
    def __ge__(self, other: Player) -> bool:
        """
        Check if this player is greater than or equal to another player.
        Args:
            other (Player): The other player to compare against.
        Returns:
            bool: True if this player is greater than or equal to the other player, False otherwise.
        Example:
            >>> player1 = Player("Alice")
            >>> player2 = Player("Bob")
            >>> player1.score = 10
            >>> player2.score = 20
            >>> player1 >= player2
            False
        """
        return not self.__lt__(other)
    
    def __hash__(self):
        return hash(self.name)


    def add_card(self, card: Card) -> None:
        """
        Add a card to the player's hand.
        Args:
            card (Card): The card to add to the player's hand.
        Example:
            >>> player = Player("Alice")
            >>> card = Card(Seed.spades, 1)
            >>> player.add_card(card)
            >>> print(player.hand)
            [1 of spades]
        """

        self.hand.add_card(card)

    def add_cards(self, cards: List[Card]) -> None:
        """
        Add multiple cards to the player's hand.
        Args:
            cards (List[Card]): A list of cards to add to the player's hand.
        Example:
            >>> player = Player("Alice")
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.add_cards(cards)
            >>> print(player.hand)
            [1 of spades, 13 of cups]
        """
        self.hand.add_cards(cards)

    def remove_card(self, card: Card) -> None:
        """
        Remove a card from the player's hand.
        Args:
            card (Card): The card to remove from the player's hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)]))
            >>> card = Card(Seed.spades, 1)
            >>> player.remove_card(card)
            >>> print(player.hand)
            [13 of cups]
        """
        self.hand.remove_card(card)

    def remove_cards(self, cards: List[Card]) -> None:
        """
        Remove multiple cards from the player's hand.
        Args:
            cards (List[Card]): A list of cards to remove from the player's hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)]))
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.remove_cards(cards)
            >>> print(player.hand)
            []
        """

        self.hand.remove_cards(cards)

        return None

    def has_card(self, card: Card) -> bool:
        """
        Check if the player has a specific card.
        Args:
            card (Card): The card to check for in the player's hand.
        Returns:
            bool: True if the player has the card, False otherwise.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = Card(Seed.spades, 1)
            >>> player.has_card(card)
            True
        """

        return self.hand.has_card(card)

    def has_cards(self, cards: List[Card]) -> bool:
        """
        Check if the player has multiple cards.
        Args:
            cards (List[Card]): A list of cards to check for in the player's hand.
        Returns:
            bool: True if the player has all the cards, False otherwise.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.has_cards(cards)
            True
        """

        return self.hand.has_cards(cards)

    def has_seed(self, seed: Seed) -> bool:
        """
        Check if the player has any cards of a specific seed.
        Args:
            seed (Seed): The seed to check for in the player's hand.
        Returns:
            bool: True if the player has any cards of the seed, False otherwise.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.has_seed(Seed.spades)
            True
        """

        return self.hand.has_seed(seed)

    def has_seeds(self, seeds: List[Seed]) -> bool:
        """
        Check if the player has cards of all the specified seeds.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the player's hand.
        Returns:
            bool: True if the player has cards of all the seeds, False otherwise.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.has_seeds([Seed.spades, Seed.cups])
            True
        """

        return self.hand.has_seeds(seeds)

    def clear_hand(self) -> None:
        """
        Reset the player's hand to an empty hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.reset_hand()
            >>> print(player.hand)
            []
        """
    
        self.hand = Hand.empty()
        return None

    def reset_won_cards(self) -> None:
        """
        Reset the player's won cards to an empty hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.reset_won_cards()
            >>> print(player.won_cards)
            []
        """

        self.won_cards = Hand.empty()

        return None

    @property
    def value(self) -> int:
        """
        Calculate the total value of the cards in the player's hand.
        Returns:
            int: The total value of the cards in the player's hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.value
            14
        """

        return self.hand.value
    
    def choose_card(self) -> Card:
        """
        Choose a card.
        Returns:
            Card: The card chosen.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = player.choose_card()
            >>> print(card)
            1 of spades
        """
        return Card.random()

    def choose_own_card(self) -> Card:
        """
        Choose a card from the player's hand.
        Returns:
            Card: The card chosen from the player's hand.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = player.choose_own_card()
            >>> print(card)
            1 of spades
        """

        return rnd.choice(self.hand)

    def choice_bool(self) -> bool:
        """
        Choose a boolean value.
        Returns:
            bool: The boolean value chosen.
        Example:
            >>> player = Player("Alice")
            >>> choice = player.choice_bool()
            >>> print(choice)
            True
        """
        return rnd.choice([True, False]) 

    def add_won_card(self, card: Card) -> None:
        """
        Add a card to the player's won cards.
        Args:
            card (Card): The card to add to the player's won cards.
        Example:
            >>> player = Player("Alice")
            >>> card = Card(Seed.spades, 1)
            >>> player.add_won_card(card)
            >>> print(player.won_cards)
            [1 of spades]
        """

        self.won_cards.add_card(card)

        return None

    def add_won_cards(self, cards: List[Card]) -> None:
        """
        Add multiple cards to the player's won cards.
        Args:
            cards (List[Card]): A list of cards to add to the player's won cards.
        Example:
            >>> player = Player("Alice")
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.add_won_cards(cards)
            >>> print(player.won_cards)
            [1 of spades, 13 of cups]
        """
        self.won_cards.add_cards(cards)

    def remove_won_card(self, card: Card) -> None:
        """
        Remove a card from the player's won cards.
        Args:
            card (Card): The card to remove from the player's won cards.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = Card(Seed.spades, 1)
            >>> player.remove_won_card(card)
            >>> print(player.won_cards)
            [13 of cups]
        """

        self.won_cards.remove_card(card)

    def remove_won_cards(self, cards: List[Card]) -> None:
        """
        Remove multiple cards from the player's won cards.
        Args:
            cards (List[Card]): A list of cards to remove from the player's won cards.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.remove_won_cards(cards)
            >>> print(player.won_cards)
            []
        """
        self.hand.remove_cards(cards)

    def has_won_card(self, card: Card) -> bool:
        """
        Check if the player has a specific card in their won cards.
        Args:
            card (Card): The card to check for in the player's won cards.
        Returns:
            bool: True if the player has the card in their won cards, False otherwise.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> card = Card(Seed.spades, 1)
            >>> player.has_won_card(card)
            True
        """

        return self.won_cards.has_card(card)

    def has_won_cards(self, cards: List[Card]) -> bool:
        """
        Check if the player has multiple cards in their won cards.
        Args:
            cards (List[Card]): A list of cards to check for in the player's won cards.
        Returns:
            bool: True if the player has all the cards in their won cards, False otherwise.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> player.has_won_cards(cards)
            True
        """
        return self.won_cards.has_cards(cards)

    def has_won_seed(self, seed: Seed) -> bool:
        """
        Check if the player has any cards of a specific seed in their won cards.
        Args:
            seed (Seed): The seed to check for in the player's won cards.
        Returns:
            bool: True if the player has any cards of the seed in their won cards, False otherwise.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.has_won_seed(Seed.spades)
            True
        """

        return self.won_cards.has_seed(seed)

    def has_won_seeds(self, seeds: List[Seed]) -> bool:
        """
        Check if the player has cards of all the specified seeds in their won cards.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the player's won cards.
        Returns:
            bool: True if the player has cards of all the seeds in their won cards, False otherwise.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.has_won_seeds([Seed.spades, Seed.cups])
            True
        """

        return self.won_cards.has_seeds(seeds)

    @property
    def value_won(self) -> int:
        """
        Calculate the total value of the cards won by the player.
        Returns:
            int: The total value of the cards won by the player.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player.value_won
            14
        """

        return self.won_cards.value

    @property
    def notation(self) -> str:
        """
        Return a string notation of the player.
        Returns:
            str: A string notation of the player.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> print(player.notation)
            'Alice:\ns[1]\nu[13]'
        """

        return f"{self.name}:\n{self.hand.notation}"

    @classmethod
    def exchange_cards(cls, player_1: Player, player_2: Player, card_1: Card, card_2: Card) -> None:
        """
        Exchange cards between two players.
        Args:
            player_1 (Player): The first player to exchange cards with.
            player_2 (Player): The second player to exchange cards with.
            card_1 (Card): The card to exchange from the first player.
            card_2 (Card): The card to exchange from the second player.
        Example:
            >>> player_1 = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> player_2 = Player("Bob", Hand([Card(Seed.coins, 7), Card(Seed.swords, 10)])
            >>> card_1 = Card(Seed.spades, 1)
            >>> card_2 = Card(Seed.coins, 7)
            >>> Player.exchange_cards(player_1, player_2, card_1, card_2)
            >>> print(player_1.hand)
            [7 of coins, 13 of cups]
            >>> print(player_2.hand)
            [1 of spades, 10 of swords]
        """

        Hand.exchange_cards(player_1.hand, player_2.hand, card_1, card_2)
        
        return None

    def update_score(self) -> None:
        """
        Update the player's score based on their won cards and debt.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)], debt = 2)
            >>> player.update_score()
            >>> print(player.score)
            4
        """

        temp_score = self.won_cards.value - self.debt
        self.score += round(temp_score/3)
        return None

    @property
    def hand_value_notation(self) -> dict:
        """
        Return a dictionary of the player's hand cards grouped by their value.
        Returns:
            dict: A dictionary where the keys are the card values and the values are lists of card notations.
        Example:
            >>> player = Player("Alice", Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> print(player.hand_value_notation)
            {1: ['s:[1]'], 14: ['u:[13]']}
        """

        possible_values = [1,4*3,2*3-2,3*3-2,4*3-2,5*3-2]
        val_dict = {val:[] for val in possible_values}

        for card in self.hand.cards:
            val_dict[card.value].append(card.notation)

        return val_dict

    @property
    def won_cards_value_notation(self) -> dict:
        """
        Return a dictionary of the player's won cards grouped by their value.
        Returns:
            dict: A dictionary where the keys are the card values and the values are lists of card notations.
        Example:
            >>> player = Player("Alice", won_cards = Hand([Card(Seed.spades, 1), Card(Seed.cups, 13)])
            >>> print(player.won_cards_value_notation)
            {1: ['s:[1]'], 14: ['u:[13]']}
        """

        possible_values = [1,4*3,2*3-2,3*3-2,4*3-2,5*3-2]
        val_dict = {val:[] for val in possible_values}

        for card in self.won_cards.cards:
            val_dict[card.value].append(card.notation)

        return val_dict

    @classmethod
    def from_list(cls, name_list: list[str]) -> list[Player]:
        """
        Create a list of players from a list of names.
        Args:
            name_list (list[str]): A list of names for the players.
        Returns:
            list[Player]: A list of players with the specified names.
        Example:
            >>> names = ["Alice", "Bob", "Charlie"]
            >>> players = Player.from_list(names)
            >>> print(players)
            [Alice, Bob, Charlie]
        """

        return [Player(name) for name in name_list]

    @classmethod
    def placeholder(cls, num:int = 1) -> Player|list[Player]:
        """
        Create a placeholder player or a list of placeholder players.
        Args:
            num (int): The number of placeholder players to create.
        Returns:
            Player|list[Player]: A placeholder player or a list of placeholder players.
        Example:
            >>> player = Player.placeholder()
            >>> print(player)
            placeholder
            >>> players = Player.placeholder(3)
            >>> print(players)
            [placeholder0, placeholder1, placeholder2]
        """
        if num == 1:
            return Player("placeholder")
        
        return [Player("placeholder"+str(i)) for i in range(num)]

    def set_debt(self) -> None:
        """
        Set the player's debt based on whether they are asking or not. Set the debt to 21*3 if asking, 19*3 otherwise.
        Example:
            >>> player = Player("Alice")
            >>> player.asking = True
            >>> player.set_debt()
            >>> print(player.debt)
            63
            >>> player.asking = False
            >>> player.set_debt()
            >>> print(player.debt)
            57
        """
        if self.asking:
            self.debt = 21*3
        else:
            self.debt = 19*3
        return None

    @property
    def is_hand_empty(self) -> bool:
        """
        Check if the player's hand is empty.
        Returns:
            bool: True if the player's hand is empty, False otherwise.
        Example:
            >>> player = Player("Alice", Hand.empty())
            >>> player.is_hand_empty
            True
        """
        return self.hand.is_empty

    

class PlayedCard(Card):
    """
    A class representing a card played by a player.
    Attributes:
        seed (Seed): The seed of the card.
        number (int): The number of the card.
        order (int): The order in which the card was played.
        player (Player): The player who played the card.
    Methods:
        __init__(seed: Seed, number: int, order: int, player: Player):
            Initializes the PlayedCard with a seed, number, order, and player.
        __repr__():
            Returns a string representation of the played card.
        __eq__(other: PlayedCard) -> bool:
            Check if the played card is equal to another played card.
        __ne__(other: PlayedCard) -> bool:
            Check if the played card is not equal to another played card.
        __lt__(other: PlayedCard) -> bool:
            Check if the played card is less than another played card.
        __le__(other: PlayedCard) -> bool:
            Check if the played card is less than or equal to another played card.
        __gt__(other: PlayedCard) -> bool:
            Check if the played card is greater than another played card.
        __ge__(other: PlayedCard) -> bool:
            Check if the played card is greater than or equal to another played card.
        from_card(cls, card: Card, order: int, owner: Player = Player.placeholder()) -> PlayedCard:
            Create a PlayedCard from a Card.
        random(cls, maxOrder: int) -> PlayedCard:
            Create a random PlayedCard.
        from_cards(cls, cards: List[Card], players: List[Player]) -> List[PlayedCard]:
            Create a list of PlayedCards from a list of Cards and a list of Players.
        card() -> Card:
            Return the card of the played card.
    """

    def __init__(self, seed: Seed, number: int, order: int, player: Player):
        super().__init__(seed, number)
        self.order = order
        self.player = player

    def __repr__(self):
        """
        Returns a string representation of the played card.
        Returns:
            str: A string representation of the played card.
        Example:
            >>> card = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> print(card)
            '0) 1 of spades from Alice'
        """

        return f"{self.order}) {super().__repr__()} from {self.player.name}"

    def __eq__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is equal to another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        Returns:
            bool: True if the played cards are equal, False otherwise.
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_1 == card_2
            True
        """
        return self.card == other.card
        
    def __ne__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is not equal to another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        Returns:
            bool: True if the played cards are not equal, False otherwise.
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 1, 0, Player("Bob"))
            >>> card_1 != card_2
            True
        """
        return not self.__eq__(other)

    def __lt__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is less than another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        Returns:
            bool: True if the played card is less than the other played card, False otherwise.
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 2, 1, Player("Bob"))
            >>> card_1 < card_2
            True
        """

        if self == other: #if the cards are the same
            return False

        if self.number == 0 or other.number == 0: #if one of the cards is the fool
            return self.number < other.number 

        if self.seed == Seed.tarots: #if self is a tarots card
            return self.card < other.card

        if other.seed == Seed.tarots: #if the other card is a tarots card and self is not
            return True 

        if self.seed != other.seed: #if the second card is not the same seed as the first
            return self.order < other.order

        if self.number > 10 or other.number > 10: #if the card is a figure
            return self.number < other.number

        if self.seed in [Seed.cups, Seed.coins]: #if the seed is cups or coins
            return self.number < other.number
        
        return self.number > other.number #check the higher number
               
    def __le__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is less than or equal to another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        return self.__lt__(other) or self.__eq__(other)
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 1, 0, Player("Bob"))
            >>> card_1 <= card_2
            True
        """
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is greater than another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        Returns:
            bool: True if the played card is greater than the other played card, False otherwise.
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 2, 1, Player("Bob"))
            >>> card_1 > card_2
            False
        """

        return not self.__le__(other)

    def __ge__(self, other: PlayedCard) -> bool:
        """
        Check if the played card is greater than or equal to another played card.
        Args:
            other (PlayedCard): The other played card to compare with.
        Returns:
            bool: True if the played card is greater than or equal to the other played card, False otherwise.
        Example:
            >>> card_1 = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_2 = PlayedCard(Seed.spades, 1, 0, Player("Bob"))
            >>> card_1 >= card_2
            True
        """

        return not self.__lt__(other)

    def __hash__(self):
        return hash(self.card)

    @classmethod
    def from_card(cls, card: Card, order: int, owner: Player = Player.placeholder()) -> PlayedCard:
        """
        Create a PlayedCard from a Card.
        Args:
            card (Card): The card to create a PlayedCard from.
            order (int): The order in which the card was played.
            owner (Player): The player who played the card.
        Returns:
            PlayedCard: A PlayedCard created from the card.
        Example:
            >>> card = Card(Seed.spades, 1)
            >>> played_card = PlayedCard.from_card(card, 0, Player("Alice"))
            >>> print(played_card)
            '0) 1 of spades from Alice'
        """

        return PlayedCard(card.seed, card.number, order, owner)

    @classmethod
    def random(cls,maxOrder: int) -> PlayedCard:
        """
        Create a random PlayedCard.
        Args:
            maxOrder (int): The maximum order for the random PlayedCard.
        Returns:
            PlayedCard: A random PlayedCard.
        Example:
            >>> played_card = PlayedCard.random(3)
            >>> print(played_card)
            '0) 1 of spades from placeholder'
        """

        card = Card.random()
        order = rnd.randint(0,maxOrder)
        return PlayedCard(card.seed, card.number, order, Player.placeholder())

    @classmethod
    def from_cards(cls, cards: List[Card], players: List[Player]) -> List[PlayedCard]:
        """
        Create a list of PlayedCards from a list of Cards and a list of Players.
        Args:
            cards (List[Card]): A list of cards to create PlayedCards from.
            players (List[Player]): A list of players who played the cards.
        Returns:
            List[PlayedCard]: A list of PlayedCards created from the cards.
        Example:
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> players = [Player("Alice"), Player("Bob")]
            >>> played_cards = PlayedCard.from_cards(cards, players)
            >>> print(played_cards)
            ['0) 1 of spades from Alice', '1) 13 of cups from Bob']
        """
        return [PlayedCard.from_card(card, i, Player) for i, card in enumerate(zip(cards,players))]

    @property
    def card(self) -> Card:
        """
        Return the card of the played card.
        Returns:
            Card: The card of the played card.
        Example:
            >>> played_card = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card = played_card.card
            >>> print(card)
            1 of spades
        """

        return Card(seed=self.seed,number=self.number)


class CardRound:
    """
    A class representing a round of cards played by players.
    Attributes:
        played_cards (list[PlayedCard]): The cards played by the players.
    Methods:
        __init__(cards: list[PlayedCard]):
            Initializes the CardRound with a list of played cards.
        __repr__():
            Returns a string representation of the card round.
        __iter__(): 
            Returns an iterator for the played cards.
        __getitem__(key):
            Returns the played card at the specified index.
        __setitem__(key, value):
            Sets the played card at the specified index to the specified value.
        __delitem__(key):
            Deletes the played card at the specified index.
        from_cards(cls, cards: List[Card], players: List[Player]) -> CardRound:
            Create a CardRound from a list of Cards and a list of Players.
        random(cls, num: int) -> CardRound:
            Create a random CardRound.
        winner_played_card() -> PlayedCard:
            Return the played card with the highest value.
        winner_player() -> Player:
            Return the player who played the card with the highest value.
        add_card(card: PlayedCard) -> None:
            Add a card to the card round.
        add_cards(cards: List[PlayedCard]) -> None:
            Add multiple cards to the card round.
        remove_card(card: PlayedCard) -> None:
            Remove a card from the card round.
        remove_cards(cards: List[PlayedCard]) -> None:
            Remove multiple cards from the card round.
        has_card(card: PlayedCard) -> bool:
            Check if the card round has a specific card.
        has_cards(cards: List[PlayedCard]) -> bool:
            Check if the card round has multiple cards.
        has_seed(seed: Seed) -> bool:
            Check if the card round has any cards of a specific seed.
        has_seeds(seeds: List[Seed]) -> bool:
            Check if the card round has cards of all the specified seeds.
        value() -> int:
            Calculate the total value of the cards in the card round.
        sorted() -> CardRound:
            Return a sorted version of the card round.
        reversed() -> CardRound:
            Return a reversed version of the card round.
        ordered() -> CardRound:
            Return an ordered version of the card round.
        reversed_ordered() -> CardRound:
            Return a reversed ordered version of the card round.
        seed() -> Seed:
            Return the seed of the card round.
        empty() -> CardRound:
            Return an empty card round.
    """

    def __init__(self, cards: list[PlayedCard]):
        self.played_cards = cards

    def __repr__(self):
        """
        Returns a string representation of the card round.
        Returns:
            str: A string representation of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> print(card_round)
            '0) 1 of spades from Alice\n'
        """
        return "".join([f"{card}\n" for card in self.played_cards])

    def __iter__(self):
        return iter(self.played_cards)

    def __getitem__(self, key):
        return self.played_cards[key]

    def __setitem__(self, key, value):
        self.played_cards[key] = value

    def __delitem__(self, key):
        del self.played_cards[key]

    @classmethod
    def empty(cls) -> CardRound:
        """
        Return an empty card round.
        Returns:
            CardRound: An empty card round.
        Example:
            >>> card_round = CardRound.empty()
            >>> print(card_round)
            ''
        """
        return CardRound([])
    

    @classmethod
    def from_cards(cls, cards: List[Card], players: List[Player]) -> CardRound:
        """
        Create a CardRound from a list of Cards and a list of Players.
        Args:
            cards (List[Card]): A list of cards to create PlayedCards from.
            players (List[Player]): A list of players who played the cards.
        Returns:
            CardRound: A CardRound created from the cards.
        Example:
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> players = [Player("Alice"), Player("Bob")]
            >>> card_round = CardRound.from_cards(cards, players)
            >>> print(card_round)
            '0) 1 of spades from Alice\n1) 13 of cups from Bob\n'
        """

        return CardRound(PlayedCard.from_cards(cards,players))

    @classmethod
    def random(cls, num: int) -> CardRound:
        """
        Create a random CardRound.
        Args:
            num (int): The number of random played cards to create.
        Returns:
            CardRound: A random CardRound.
        Example:
            >>> card_round = CardRound.random(3)
            >>> print(card_round)
            '0) 1 of spades from placeholder\n1) 1 of spades from placeholder\n2) 1 of spades from placeholder\n'
        """

        return CardRound([PlayedCard.random(i) for i in range(num)])

    @property
    def winner_played_card(self) -> PlayedCard:
        """
        Return the played card with the highest value.
        Returns:
            PlayedCard: The played card with the highest value.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> print(card_round.winner_played_card)
            '0) 1 of spades from Alice'
        """

        return max(self.played_cards)

    @property
    def winner_player(self) -> Player:
        """
        Return the player who played the card with the highest value.
        Returns:
            Player: The player who played the card with the highest value.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> print(card_round.winner_player)
            'Alice'
        """

        return self.winner_played_card.player

    def add_card(self, card: PlayedCard) -> None:
        """
        Add a card to the card round.
        Args:
            card (PlayedCard): The card to add to the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> card = PlayedCard(Seed.cups, 13, 1, Player("Bob"))
            >>> card_round.add_card(card)
            >>> print(card_round)
            '0) 1 of spades from Alice\n1) 13 of cups from Bob\n'
        """
        self.played_cards.append(card)

    def add_cards(self, cards: List[PlayedCard]) -> None:
        """
        Add multiple cards to the card round.
        Args:
            cards (List[PlayedCard]): A list of cards to add to the card round.
        Example:
            >>> card_round = CardRound.empty()
            >>> cards = [PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))]
            >>> card_round.add_cards(cards)
            >>> print(card_round)
            '0) 1 of spades from Alice\n1) 13 of cups from Bob\n'
        """

        self.played_cards.extend(cards)

    def remove_card(self, card: PlayedCard) -> None:
        """
        Remove a card from the card round.
        Args:
            card (PlayedCard): The card to remove from the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> card = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_round.remove_card(card)
            >>> print(card_round)
            '1) 13 of cups from Bob\n'
        """

        self.played_cards.remove(card)

    def remove_cards(self, cards: List[PlayedCard]) -> None:
        """
        Remove multiple cards from the card round.
        Args:
            cards (List[PlayedCard]): A list of cards to remove from the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> cards = [PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))]
            >>> card_round.remove_cards(cards)
            >>> print(card_round)
            ''
        """
        for card in cards:
            self.played_cards.remove(card)

    def has_card(self, card: PlayedCard) -> bool:
        """
        Check if the card round has a specific card.
        Args:
            card (PlayedCard): The card to check for in the card round.
        Returns:
            bool: True if the card round has the card, False otherwise.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> card = PlayedCard(Seed.spades, 1, 0, Player("Alice"))
            >>> card_round.has_card(card)
            True
        """

        return card in self.played_cards

    def has_cards(self, cards: List[PlayedCard]) -> bool:
        """
        Check if the card round has multiple cards.
        Args:
            cards (List[PlayedCard]): A list of cards to check for in the card round.
        Returns:
            bool: True if the card round has all the cards, False otherwise.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> cards = [PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))]
            >>> card_round.has_cards(cards)
            True
        """

        return all(card in self.played_cards for card in cards)

    def has_seed(self, seed: Seed) -> bool:
        """
        Check if the card round has any cards of a specific seed.
        Args:
            seed (Seed): The seed to check for in the card round.
        Returns:
            bool: True if the card round has any cards of the seed, False otherwise.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> card_round.has_seed(Seed.spades)
            True
        """

        return any(card.seed == seed for card in self.played_cards)

    def has_seeds(self, seeds: List[Seed]) -> bool:
        """
        Check if the card round has cards of all the specified seeds.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the card round.
        Returns:
            bool: True if the card round has cards of all the seeds, False otherwise.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> card_round.has_seeds([Seed.spades, Seed.cups])
            False
        """

        return all(any(card.seed == seed for card in self.played_cards) for seed in seeds)

    @property
    def value(self) -> int:
        """
        Calculate the total value of the cards in the card round.
        Returns:
            int: The total value of the cards in the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> print(card_round.value)
            1
        """

        return sum(card.value for card in self.played_cards)

    @property
    def sorted(self) -> CardRound:
        """
        Return a sorted version of the card round.
        Returns:
            CardRound: A sorted version of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> print(card_round.sorted)
            '0) 1 of spades from Alice\n1) 13 of cups from Bob\n'
        """

        return CardRound(sorted(self.played_cards))

    @property
    def reversed(self) -> CardRound:    
        """
        Return a reversed version of the card round.
        Returns:

            CardRound: A reversed version of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> print(card_round.reversed)
            '0) 13 of cups from Bob\n1) 1 of spades from Alice\n'
        """

        return CardRound(reversed(self.played_cards))
    
    @property
    def ordered(self) -> CardRound:
        """
        Return an ordered version of the card round.
        Returns:
            CardRound: An ordered version of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> print(card_round.ordered)
            '0) 1 of spades from Alice\n1) 13 of cups from Bob\n'
        """

        return CardRound(sorted(self.played_cards, key=lambda x: x.order))
    
    @property
    def reversed_ordered(self) -> CardRound:
        """
        Return a reversed ordered version of the card round.
        Returns:
            CardRound: A reversed ordered version of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice")), PlayedCard(Seed.cups, 13, 1, Player("Bob"))])
            >>> print(card_round.reversed_ordered)
            '1) 13 of cups from Bob\n0) 1 of spades from Alice\n'
        """
        return CardRound(sorted(self.played_cards, key=lambda x: x.order, reverse=True))
    
    @property
    def seed(self) -> Seed:
        """
        Return the seed of the card round.
        Returns:
            Seed: The seed of the card round.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> print(card_round.seed)
            'spades'
        """

        return self.played_cards[0].seed

    def put_card_into_play(self, played_card: PlayedCard) -> bool:
        """
        Put a card into play. The card must be of the same seed as the round or a tarot card. 
        If the card is not of the same seed as the round and the player has cards of the same seed as the round, the card cannot be put into play. 
        If the card is not of the same seed as the round and the player has tarot cards, the card must be a tarot card.
        Args:
            played_card (PlayedCard): The card to put into play.
        Returns:
            bool: True if the card was put into play, False otherwise.
        Example:
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> played_card = PlayedCard(Seed.cups, 13, 1, Player("Bob"))
            >>> card_round.put_card_into_play(played_card)
            False
            >>> print(card_round)
            '0) 1 of spades from Alice'
            >>> played_card = PlayedCard(Seed.spades, 2, 1, Player("Bob"))
            >>> card_round.put_card_into_play(played_card)
            True
            >>> print(card_round)
            '0) 1 of spades from Alice\n1) 2 of spades from Bob'
        """

        card = played_card.card
        player = played_card.player

        if self == False: #if the card round is empty
            player.hand.remove_card(card) #remove the card from the player's hand
            self.add_card(played_card) #add the card to the card round
            return True


        if card.seed != self.seed: #if the card is not of the same seed as the round
            if player.has_seed(round.seed): #if the player has cards of the same seed as the round
                print(f"Card must be of the {round.seed} seed")
                return False
            if player.has_seed(Seed.tarots): #if the player has tarots cards
                print(f"{self.seed} cards finished, card must be a tarot")
                return False
        
        player.hand.remove_card(card) #remove the card from the player's hand
        self.add_card(played_card)
        return True 

    @property
    def cards(self) -> list[Card]:
        """Return the cards of the round
        Returns:
            list[Card]: The cards of the round
        """

        return [played_card.card for played_card in self.played_cards]


class Team:
    """
    A class representing a team of players.
    Attributes:
        players (List[Player]): The players in the team.
        won_cards (Hand): The cards won by the team.
    Methods:
        __init__(players: List[Player]):
            Initializes the Team with a list of players.
        __repr__():
            Returns a string representation of the team.
        __bool__():
            Returns True if the team has players, False otherwise.
        __len__():
            Returns the number of players in the team.
        __iter__():
            Returns an iterator for the players in the team.
        __getitem__(key):
            Returns the player at the specified index.
        __setitem__(key, value):
            Sets the player at the specified index to the specified value.
        __delitem__(key):
            Deletes the player at the specified index.
        add_card(card: Card):
            Add a card to the team's won cards.
        add_cards(cards: List[Card]):
            Add multiple cards to the team's won cards.
        remove_card(card: Card):
            Remove a card from the team's won cards.
        remove_cards(cards: List[Card]):
            Remove multiple cards from the team's won cards.
        has_card(card: Card) -> bool:
            Check if the team has a specific card.
        has_cards(cards: List[Card]) -> bool:
            Check if the team has multiple cards.
        has_seed(seed: Seed) -> bool:
            Check if the team has any cards of a specific seed.
        has_seeds(seeds: List[Seed]) -> bool:
            Check if the team has cards of all the specified seeds.
        value() -> int:
            Calculate the total value of the team's won cards.
        add_player(player: Player):
            Add a player to the team.
        add_players(players: list[Player]):
            Add multiple players to the team.
        remove_player(player: Player):
            Remove a player from the team.
        remove_players(players: List[Player]):
            Remove multiple players from the team.
        has_player(player: Player) -> bool:
            Check if the team has a specific player.
        has_players(players: list[Player]) -> bool:
            Check if the team has multiple players.
        reset_team_won_cards():
            Reset the team's won cards.
        reset_players_won_cards():
            Reset all the players' won cards.
        reset_all_won_cards():
            Reset all the won cards.
        update_team_won_cards():
            Add to the team's won cards all the players' won cards.
        update_players_won_cards():
            Assign for all the players the won cards of the team.
        notation() -> str:
            Return the notation of each player.
        find_asking_player() -> List[Player]:
            Find who is the asking player in the team if any.
        asking() -> bool:
            Find if there is an asking player in the team.
        set_debt():
            Set the debt for all players in the team.
    """


    def __init__(self, players: List[Player]) -> None:

        for player in players:
            if not isinstance(player,Player):
                print(f"player who gave error {player}")
                raise TypeError(f"\n\nplayers must be a list of Player type.\nGiven {players}")

        self.players = players
        self.won_cards = Hand.empty()
        pass

    def __repr__(self) -> str:
        """
        Return a string representation of the team
        Returns:
            str: A string representation of the team
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> print(team)
            'the team is composed of:\nAlice\nBob'
        """
        return f"the team is composed of:\n{self.players}"

    def __bool__(self) -> bool:
        return self.players
    
    def __len__(self) -> int:
        return len(self.players)

    def __iter__(self):
        return iter(self.players)

    def __getitem__(self, key):
        return self.players[key]

    def __setitem__(self, key, value):
        self.players[key] = value

    def __delitem__(self, key):
        del self.players[key]

    @classmethod
    def empty(cls) -> Team:
        """Return an empty team"""
        return Team([])

    def add_card(self, card: Card) -> None:
        """
        Add a card to the team's won cards.
        Args:
            card (Card): The card to add to the team's won cards.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> print(team.won_cards)
            '1 of spades'
        """
        self.won_cards.add_card(card)

    def add_cards(self, cards: List[Card]) -> None:
        """
        Add multiple cards to the team's won cards.
        Args:
            cards (List[Card]): A list of cards to add to the team's won cards.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> team.add_cards(cards)
            >>> print(team.won_cards)
            '1 of spades\n13 of cups'
        """
        self.won_cards.add_cards(cards)

    def remove_card(self, card: Card) -> None:
        """
        Remove a card from the team's won cards.
        Args:
            card (Card): The card to remove from the team's won cards.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.remove_card(card)
            >>> print(team.won_cards)
            ''
        """

        self.won_cards.remove_card(card)

    def remove_cards(self, cards: List[Card]) -> None:
        """
        Remove multiple cards from the team's won cards.
        Args:
            cards (List[Card]): A list of cards to remove from the team's won cards.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> team.add_cards(cards)
            >>> team.remove_cards(cards)
            >>> print(team.won_cards)
            ''
        """

        self.won_cards.remove_cards(cards)

    def has_card(self, card: Card) -> bool:
        """
        Check if the team has a specific card.
        Args:
            card (Card): The card to check for in the team's won cards.
        Returns:
            bool: True if the team has the card, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.has_card(card)
            True
        """

        return self.won_cards.has_card(card)

    def has_cards(self, cards: List[Card]) -> bool:
        """
        Check if the team has multiple cards.
        Args:
            cards (List[Card]): A list of cards to check for in the team's won cards.
        Returns:
            bool: True if the team has all the cards, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> cards = [Card(Seed.spades, 1), Card(Seed.cups, 13)]
            >>> team.add_cards(cards)
            >>> team.has_cards(cards)
            True
        """

        return self.won_cards.has_cards(cards)

    def has_seed(self, seed: Seed) -> bool:
        """
        Check if the team has any cards of a specific seed.
        Args:
            seed (Seed): The seed to check for in the team's won cards.
        Returns:
            bool: True if the team has any cards of the seed, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.has_seed(Seed.spades)
            True
        """

        return self.won_cards.has_seed(seed)

    def has_seeds(self, seeds: List[Seed]) -> bool:
        """
        Check if the team has cards of all the specified seeds.
        Args:
            seeds (List[Seed]): A list of seeds to check for in the team's won cards.
        Returns:
            bool: True if the team has cards of all the seeds, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.has_seeds([Seed.spades, Seed.cups])
            False
        """
        
        return self.won_cards.has_seeds(seeds)

    @property
    def value(self) -> int:
        """
        Calculate the total value of the team's won cards.
        Returns:
            int: The total value of the team's won cards.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.value
            1
        """

        return self.won_cards.value

    def add_player(self, player: Player) -> None:
        """
        Add a player to the team.
        Args:
            player (Player): The player to add to the team.
        Example:
            >>> team = Team([Player("Alice")])
            >>> player = Player("Bob")
            >>> team.add_player(player)
            >>> print(team)
            'the team is composed of:\nAlice\nBob'
        """

        self.players.append(player)

    def add_players(self, players: list[Player]) -> None:
        """
        Add multiple players to the team.
        Args:
            players (List[Player]): A list of players to add to the team.
        Example:
            >>> team = Team([Player("Alice")])
            >>> players = [Player("Bob"), Player("Charlie")]
            >>> team.add_players(players)
            >>> print(team)
            'the team is composed of:\nAlice\nBob\nCharlie'
        """
        self.players.extend(players)

    def remove_player(self, player: Player) -> None:
        """
        Remove a player from the team.
        Args:
            player (Player): The player to remove from the team.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> player = Player("Bob")
            >>> team.remove_player(player)
            >>> print(team)
            'the team is composed of:\nAlice'
        """
        print(f"player to remove {player}")
        print(f"players in team {self.players}")
        self.players.remove(player)
        print(f"players in team {self.players}")

        return None

    def remove_players(self, players: List[Player]) -> None:
        """
        Remove multiple players from the team.
        Args:
            players (List[Player]): A list of players to remove from the team.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> players = [Player("Bob"), Player("Charlie")]
            >>> team.remove_players(players)
            >>> print(team)
            'the team is composed of:\nAlice'
        """

        for player in players:
            self.players.remove(player)

    def has_player(self, player: Player) -> bool:
        """
        Check if the team has a specific player.
        Args:
            player (Player): The player to check for in the team.
        Returns:
            bool: True if the team has the player, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> player = Player("Alice")
            >>> team.has_player(player)
            True
        """

        return player in self.players

    def has_players(self, players: list[Player]) -> bool:
        """
        Check if the team has multiple players.
        Args:
            players (List[Player]): A list of players to check for in the team.
        Returns:
            bool: True if the team has all the players, False otherwise.
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> players = [Player("Alice"), Player("Bob")]
            >>> team.has_players(players)
            True
        """

        return all(player in self.players for player in players)
    
    def reset_team_won_cards(self) -> None:
        """
        Reset the team's won cards
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> print(team.won_cards)
            '1 of spades'
            >>> team.reset_team_won_cards()
            >>> print(team.won_cards)
            ''
        """

        self.won_cards = Hand.empty()
        return None
    
    def reset_players_won_cards(self) -> None:
        """
        Reset all the players' won cards
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> print(team.players[0].won_cards)
            '1 of spades'
            >>> print(team.players[1].won_cards)
            '1 of spades'
            >>> team.reset_players_won_cards()
            >>> print(team.players[0].won_cards)
            ''
            >>> print(team.players[1].won_cards)
            ''
        """

        for player in self.players:
            player.won_cards = Hand.empty()
        return None
    
    def reset_all_won_cards(self) -> None:
        self.reset_players_won_cards()
        self.reset_team_won_cards()
        return None
    
    def update_team_won_cards(self) -> None:
        """
        Add to the team's won cards all the players' won cards
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.update_team_won_cards()
            >>> print(team.won_cards)
            '1 of spades'
        """
        for player in self.players: 
            self.won_cards += player.won_cards
        return None
                
    def update_players_won_cards(self) -> None:
        """
        Assign for all the players the won cards of the team
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> card = Card(Seed.spades, 1)
            >>> team.add_card(card)
            >>> team.update_players_won_cards()
            >>> print(team.players[0].won_cards)
            '1 of spades'
            >>> print(team.players[1].won_cards)
            '1 of spades'
        """

        for player in self.players:
            player.won_cards = self.won_cards
        return None
    
    @property
    def notation(self) -> str:
        """
        Return the notation of each player
        Returns:
            str: The notation of each player
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> print(team.notation)
            'Alice\nBob\n'
        """

        text = ""
        for player in self.players:
            text += f"{player.notation}\n"
        return text
    
    @property
    def find_asking_player(self) -> List[Player]:
        """
        Find who is the asking player in the team if any
        Returns:
            List[Player]: The asking player in the team
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> player = Player("Alice")
            >>> player.asking = True
            >>> team.find_asking_player
            'Alice'
        """

        return [player for player in self.players if player.asking]
    
    @property
    def asking(self) -> bool:
        """
        Find if there is an asking player in the team
        Returns:
            bool: True if there is an asking player in the team, False otherwise
        Example:
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> player = Player("Alice")
            >>> player.asking = True
            >>> team.asking
            True
        """

        return any(player.asking for player in self.players)
    
    def set_debt(self) -> None:
        """
        Set the debt for all players in the team
        Example:
            >>> team = Team([Player("Alice", asking=True), Player("Bob", asking=False)])
            >>> team.set_debt()
            >>> print(team.players[0].debt)
            63
            >>> print(team.players[1].debt)
            57
        """

        for player in self.players:
            player.set_debt()



class Game:
    """
    A class representing a game of Tarocchi.
    Attributes:
        players (List[Player]): The players in the game.
        rounds (List[CardRound]): The rounds played in the game.
        teams (List[Team]): The teams in the game.
        cycle_player (List[Player]): The players in the game in the order of the cycle.
        asking_player (Player): The player who is asking in the game.
        dealer (Player): The player who is the dealer in the game.
        non_asking_players (List[Player]): The players who are not asking in the game.
        current_player (Player): The player who is currently playing in the game.
        prize_claimed (bool): True if the prize has been claimed, False otherwise.
    Methods:
        __init__(players: List[Player]):
            Initializes the Game with a list of players.
        __repr__():
            Returns a string representation of the game.
        shuffle_players():
            Shuffle the players in the game.
        rotate_players():
            Rotate the players in the game.
        advance_cycle():
            Advance the cycle of players in the game.
        find_card_owner(card: Card) -> Player:
            Find the player who has a specific card.
        add_team(team: Team):
            Add a team to the game.
        remove_team(team: Team):
            Remove a team from the game.
        add_teams(teams: List[Team]):
            Add multiple teams to the game.
        remove_teams(teams: List[Team]):
            Remove multiple teams from the game.
        empty_teams():
            Remove all the teams from the game.
        empty_rounds():
            Remove all the rounds from the game.
        asking_player_card_request():
            Handle the card request of the asking player.
        set_debts():
            Set the debts for all players in the game.
        update_team_won_cards():
            Add to each team their respective players won cards.
        update_players_won_cards():
            Add to each player their respective team won cards.
        update_score():
            Update the score of the players in the game.
        player_set_initial_won_cards():
            Set the initial won cards for the players in the game.
        setup_deck():
            Setup the deck for the game.
        set_non_asking_players():
            Set the non-asking players in the game.
    """


    def __init__(self, players: List[Player]):
        num_players = len(players)
        if num_players < 3 or num_players > 5:
            raise ValueError("Number of players must be between 3 and 5")
        self.num_players = num_players
        self.players = players
        self.rounds: List[CardRound] = []
        self.teams: List[Team] = []
        self.cycle_player = players.copy()
        self.asking_player = players[0]
        self.dealer = players[-1]
        self.non_asking_players: list[Player] = []
        self.current_player = players[0]
        self.prize_claimed = False

    def __repr__(self):
        text = f"Players: {self.players}\n"
        text += f"Asking player = {self.asking_player}\n"
        text += f"Dealer = {self.dealer}\n"
        text += f"Teams: {self.teams}\n"
        text += f"Current Player: {self.current_player}\n"
        return text
    
    def shuffle_players(self) -> None:
        """
        Shuffle the players in the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.shuffle_players()
            >>> print(game.players)
            ['Bob', 'Alice', 'Charlie']
        """

        rnd.shuffle(self.players)

    def rotate_players(self) -> None:
        """
        Rotate the players in the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.rotate_players()
            >>> print(game.players)
            ['Bob', 'Charlie', 'Alice']
        """

        self.players.append(self.players.pop(0))

    def advance_cycle(self) -> None:
        next(self.cycle_player)

    def find_card_owner(self, card: Card) -> Player:
        """
        Find the player who has a specific card.
        Args:
            card (Card): The card to find the owner of.
        Returns:
            Player: The player who has the card.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1)
            >>> game.find_card_owner(card)
            'Alice'
        """

        for player in self.players:
            if player.has_card(card):
                return player

    def str_teams(self) -> str:
        """
        Print the teams in the game.
        Returns:
            str: A string representation of the teams in the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> game.add_team(team)
            >>> print(game.str_teams())
            'Team #1: the team is composed of:\nAlice\nBob\n'
        """

        text = ""
        for i, team in enumerate(self.teams):
            text += f"Team #{i+1}: {team}\n"

        return text
            
    def add_team(self, team: Team) -> None:
        """
        Add a team to the game.
        Args:
            team (Team): The team to add to the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> game.add_team(team)
            >>> print(game.str_teams())
            'Team #1: the team is composed of:\nAlice\nBob\n'
        """

        self.teams.append(team)
    
    def remove_team(self, team: Team) -> None:
        """
        Remove a team from the game.
        Args:
            team (Team): The team to remove from the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> game.add_team(team)
            >>> game.remove_team(team)
            >>> print(game.teams)
            []
        """

        self.teams.remove(team)
    
    def add_teams(self, teams: list[Team]) -> None:
        """
        Add multiple teams to the game.
        Args:
            teams (List[Team]): A list of teams to add to the game.
        """

        for team in teams:
            self.teams.append(team)
   
    def remove_teams(self, teams: list[Team]) -> None:
        for team in teams:
            self.teams.remove(team)

    def empty_teams(self) -> None:
        """
        Remove all the teams from the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> game.add_team(team)
            >>> game.empty_teams()
            >>> print(game.teams)
            []
        """
        self.teams: list[Team] = []

    def empty_rounds(self) -> None:
        """
        Remove all the rounds from the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card_round = CardRound([PlayedCard(Seed.spades, 1, 0, Player("Alice"))])
            >>> game.rounds.append(card_round)
            >>> game.empty_rounds()
            >>> print(game.rounds)
            []
        """
        self.rounds: list[CardRound] = []

    def asking_player_card_request(self) -> None:
        """
        Handle the card request of the asking player. 
        The asking player must choose a card to request, whose value is 13 and is not in their hand.
        If the number of players is 4, the asking player gets the prize. 
        
        If the prize has the card, the asking player just take the prize. 
        He forms an individual team and the other players form an opposing team.

        If the prize does not have the card, the asking player chooses a card from his hand and exchanges it with the player who has the requested card.

        If the number of players is 3 or 5, the asking player and the player who has the requested card form a team.
        If the number of players is 4, all the players form individual teams.

        Example:
            >>> game = Game([Player("Alice", asking=True), Player("Bob", asking=False), Player("Charlie", asking=False)])
            >>> game.setup_deck()
            >>> game.asking_player_card_request()
            >>> print(game.teams)
            'Team #1: the team is composed of:\nAlice\n'
            'Team #2: the team is composed of:\nBob\nCharlie\n'
        """

        self.empty_teams()

        player = self.asking_player  #get the current player
        requested_card = player.choose_card()   #choose a card
        while requested_card.value != 13 or requested_card in player.hand: 
            requested_card = player.choose_card()

        if self.prize.has_card(requested_card): #if the prize has the card
            self.assign_prize()
            self.add_team(Team([self.asking_player]))
            self.add_team(Team(self.non_asking_players))
            return None

        self.assign_prize()

        player_with_card = self.find_card_owner(requested_card) #find who has the requested card

        asking_team = Team([self.asking_player,player_with_card])

        if self.num_players == 4: #if there are 4 players
            opposing_teams: list[Team] = []
            for player_i in self.non_asking_players:
                opposing_teams.append(Team([player_i]))
        else:
            opposing_teams = Team([player_i for player_i in self.players if player_i not in asking_team])
        
        self.add_team(asking_team) #assign the teams
        self.add_teams(opposing_teams)

        card_to_exchange = player.choose_card() 
        while card_to_exchange not in player.hand:
            card_to_exchange = player.choose_card()


        Player.exchange_cards(player, player_with_card, card_to_exchange, requested_card)

        return None 

    def set_debts(self) -> None:
        for team in self.teams:
            team.set_debt()
        return None

    def update_team_won_cards(self) -> None:
        """
        Add to each team their respective players won cards
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1)
            >>> game.players[0].add_won_card(card)
            >>> game.update_team_won_cards()
            >>> print(game.teams[0].won_cards)
            '1 of spades'
        """
        for team in self.teams:
            team.update_team_won_cards()
        return None

    def update_players_won_cards(self) -> None:
        """
        Add to each player their respective team won cards
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1) 
            >>> game.players[0].add_won_card(card)
            >>> game.update_players_won_cards()
            >>> print(game.players[0].won_cards)
            '1 of spades'
        """

        for team in self.teams:
            team.update_players_won_cards()
        return None

    @property
    def non_asking_players_score(self) -> int:
        """
        Calculate the total score of the non-asking players
        Returns:
            int: The total score of the non-asking players
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.players[0].score = 1
            >>> game.players[1].score = 2
            >>> game.players[2].score = 3
            >>> game.non_asking_players_score
            5
        """
        return sum(player.score for player in self.non_asking_players)

    def update_score(self) -> None:
        """
        Update the score of the players in the game
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.players[0].score = 1
            >>> game.players[1].score = 2
            >>> game.players[2].score = 3
            >>> game.update_score()
            >>> print(game.players[0].score)
            1
            >>> print(game.players[1].score)
            2
            >>> print(game.players[2].score)
            3
        """

        for player in self.non_asking_players:
            player.update_score()
        self.asking_player.score -= self.non_asking_players_score

    def player_set_initial_won_cards(self) -> None:
        """
        Set the initial won cards for the asking player. 
        The amount of cards in the prize is 2 if there are 4 players, 3 otherwise.
        The asking player chooses a card from the prize and adds it to their won cards.
        Example:
            >>> game = Game([Player("Alice", asking=True), Player("Bob", asking=False), Player("Charlie", asking=False)])
            >>> game.setup_deck()
            >>> game.player_set_initial_won_cards()
            >>> print(game.asking_player.won_cards)
            '1 of spades'
        """

        prize_size = 2*(self.num_players == 4) + 3*(self.num_players != 4)

        player = self.asking_player

        for _ in range(prize_size):
            card = player.choose_card()
            while card not in player.hand:
                card = player.choose_card()
            player.remove_card(card)
            player.add_won_card(card)

        return None

    def setup_deck(self) -> None:
        """
        Setup the deck for the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_deck()
            >>> print(game.prize)
            '1 of spades...'
        """

        deck = Deck.standard()
        deck.shuffle()
        
        hands, prize = deck.deal(self.num_players)
        for hand,player in zip(hands, self.players):
            player.hand = hand

        self.prize = prize

        return None

    def set_non_asking_players(self) -> None:
        """
        Set the non-asking players in the game.
        Example:
            >>> game = Game([Player("Alice", asking=True), Player("Bob", asking=False), Player("Charlie", asking=False)])
            >>> game.set_non_asking_players()
            >>> print(game.non_asking_players)
            ['Bob', 'Charlie']
        """

        self.non_asking_players = self.players.copy()
        self.non_asking_players.remove(self.asking_player)
        for player in self.non_asking_players:
            player.asking = False

    def claim_prize(self) -> None:
        """
        Let the players claim the prize.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_deck()
            >>> game.claim_prize()
            >>> print(game.prize_claimed)
            True
        """

        for player in self.players:
            player_choice = player.choice_bool()
            if player_choice: #assign the prize to player
                self.asking_player = player
                player.asking = True
                self.set_non_asking_players()
                self.prize_claimed = player_choice

                return None

    def assign_prize(self) -> None:
        """
        Assign the prize to the asking player.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_deck()
            >>> game.asking_player = game.players[0]
            >>> game.assign_prize()
            >>> print(game.players[0].won_cards)
            '1 of spades...'
        """
        self.asking_player.hand += self.prize

    @property
    def scores(self) -> dict:
        """
        Get the scores of the players in the game
        Returns:
            dict: The scores of the players in the game
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.players[0].score = 1
            >>> game.players[1].score = 2
            >>> game.players[2].score = 3
            >>> game.scores
            {'Alice': 1, 'Bob': 2, 'Charlie': 3}
        """

        return {player.name:player.score for player in self.players}
    
    @property
    def debts(self) -> dict:
        """
        Get the debts of the players in the game
        Returns:
            dict: The debts of the players in the game
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.players[0].debt = 1
            >>> game.players[1].debt = 2
            >>> game.players[2].debt = 3
            >>> game.debts
            {'Alice': 1, 'Bob': 2, 'Charlie': 3}
        """

        return {player.name:player.debt for player in self.players}
    
    @property
    def won_cards(self) -> dict:
        """
        Get the won cards of the players in the game
        Returns:
            dict: The won cards of the players in the game
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.players[0].won_cards = Hand([Card(Seed.spades, 1)])
            >>> game.players[1].won_cards = Hand([Card(Seed.cups, 13)])
            >>> game.players[2].won_cards = Hand([Card(Seed.coins, 10)])
            >>> game.won_cards
            {'Alice': '1 of spades', 'Bob': '13 of cups', 'Charlie': '10 of coins'}
        """
        return {player.name:player.won_cards for player in self.players}
     
    def setup_game(self) -> None:
        """
        Setup the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_game()
        """
        
        while not self.prize_claimed: #while the prize is not empty
            self.setup_deck() #setup the deck
            self.claim_prize() #assign the prize

        self.asking_player_card_request() #request the player to choose a card    
        self.set_debts()

        return None

    @property
    def notation(self) -> str:
        """
        Return the notation of the game
        Returns:
            str: The notation of the game
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> print(game.notation)
            'Alice\nBob\nCharlie\n'
            'Dealer: Alice\n'
            'Asked: Bob\n'
            'Teams:\n'
            '#### Team #1\n'
            'Alice\nCharlie\n'
            '#### Team #2\n'
            'Bob\n'
            'prize: 1 of spades,...\n'
            'scores: {'Alice': 0, 'Bob': 0, 'Charlie': 0}\n'
            'debts: {'Alice': 57, 'Bob': 63, 'Charlie': 57}\n'
            'won cards: {'Alice': '', 'Bob': '', 'Charlie': ''}\n'
        """

        text = ""
        for player in self.players:
            text += f"{player.notation}\n"

        text += f"\nDealer: {self.dealer.name}\n"
        text += f"Asked: {self.asking_player.name}\n"

        text += f"\nTeams:\n"
        for i, team in enumerate(self.teams):
            text += f"#### Team #{i+1}\n"
            for player in team:
                text+= f"{player.name}\n"
            text += "\n"

        text += f"\nprize: {self.prize}\n"

        text += f"\nscores: {self.scores}\n"
        text += f"\ndebts: {self.debts}\n"
        text += f"\nwon cards: {self.won_cards}\n"
         
        return text

    def play_round(self) -> None:
        """
        Play a round of the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_game()
            >>> game.play_round()
        """

        round = CardRound.empty()

        for player in self.players: 
            played = False 
            while not played: #check if the player has played
                card = PlayedCard.from_card(player.choose_own_card(), player) #choose a card
                played = round.put_card_into_play(card) #put the card into play

        self.rounds.append(round)
        winner = round.winner_player
        winner.add_won_cards(round.cards)

        return None

    def play_game(self) -> None:
        """
        Play the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_game()
            >>> game.play_game() 
        """

        while not self.asking_player.is_hand_empty: 
            self.play_round()

        self.update_team_won_cards()
        self.update_players_won_cards()
        self.update_score()

        return None


    def winner(self) -> Player:
        """
        Find the winner of the game.
        Returns:
            Player: The winner of the game.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.setup_game()
            >>> game.play_game()
            >>> game.winner()
            'Alice'
        """

        return max(self.players, key=lambda x: x.won_cards.value)

    def reset_teams_won_cards(self) -> None:
        """
        Reset the teams' won cards
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1)
            >>> game.teams[0].add_card(card)
            >>> game.reset_teams_won_cards()
            >>> print(game.teams[0].won_cards)
            ''
        """

        for team in self.teams:
            team.reset_team_won_cards()
        return None
    
    def reset_players_won_cards(self) -> None:
        """
        Reset all the players' won cards
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1)
            >>> game.players[0].add_card(card)
            >>> game.reset_players_won_cards()
            >>> print(game.players[0].won_cards)
            ''
        """

        for player in self.players:
            player.reset_won_cards()
        return None
    
    def hand_to_won_cards(self) -> None:
        """
        Assign the hand of the players to their won cards
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> card = Card(Seed.spades, 1)
            >>> game.players[0].add_card(card)
            >>> game.hand_to_won_cards()
            >>> print(game.players[0].won_cards)
            '1 of spades'
        """

        self.reset_teams_won_cards()
        self.reset_players_won_cards()

        for player in self.players:
            player.won_cards = player.hand
            player.clear_hand()
        self.update_team_won_cards()
        self.update_players_won_cards()
        self.update_score()

        return None

    def find_team(self, player: Player) -> Team:
        """
        Find the team of a player.
        Args:
            player (Player): The player to find the team of.
        Returns:
            Team: The team of the player.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> team = Team([Player("Alice"), Player("Bob")])
            >>> game.add_team(team)
            >>> game.find_team(game.players[0])
            'Alice\nBob'
        """

        for team in self.teams:
            if team.has_player(player):
                return team

    @classmethod
    def placeholder(cls, num_players:int = 3) -> Game:
        """
        Create a placeholder game with a specified number of players.
        Args:
            num_players (int): The number of players in the game.
        Returns:
            Game: A placeholder game with the specified number of players.
        Example:
            >>> game = Game.placeholder(3)
            >>> print(game)
            'Players: [Alice, Bob, Charlie]\nAsking player = Alice\nDealer = Charlie\nTeams: []\nCurrent Player: Alice\n'
        """

        return Game(Player.placeholder(num_players))    

    def player_position(self, player: Player) -> int:
        """
        Find the position of a player in the cycle of players.
        Args:
            player (Player): The player to find the position of.
        Returns:
            int: The position of the player in the cycle of players.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.player_position(game.players[0])
            0
        """

        return self.players.index(player)

    def set_cycle_from_idx(self, idx: int) -> None:
        """
        Set the cycle of players from a specified index.
        Args:
            idx (int): The index to set the cycle from.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.set_cycle_from_idx(1)
            >>> print(game.cycle_player)
            ['Bob', 'Charlie', 'Alice']
        """

        new_cycle_players = self.players.copy() #copy the players

        for _ in range(idx): #rotate the players
            new_cycle_players.append(new_cycle_players.pop(0))

        return None

    def set_cycle_from_player(self, player: Player) -> None:
        """
        Set the cycle of players from a specified player.
        Args:
            player (Player): The player to set the cycle from.
        Example:
            >>> game = Game([Player("Alice"), Player("Bob"), Player("Charlie")])
            >>> game.set_cycle_from_player(game.players[1])
            >>> print(game.cycle_player)
            ['Bob', 'Charlie', 'Alice']
        """

        idx = self.player_position(player)

        self.set_cycle_from_idx(idx)

        return None  

class Match:
    """
    A class representing a match of Tarocchi.
    Attributes:
        players (List[Player]): The players in the match.
        games (List[Game]): The games played in the match.
        num_matches (int): The number of matches to play.
        num_players (int): The number of players in the match.
    Methods:
        __init__(players: List[Player], num_matches: int):
            Initializes the Match with a list of players and a number of matches.
        __repr__():
            Returns a string representation of the match.
        play_match():
            Play the match.
        scores():
            Get the scores of the players in the match.
    """


    def __init__(self, players: List[Player], num_matches: int):
        self.players = players
        self.games = []
        self.num_matches = num_matches
        self.num_players = len(players)

    def __repr__(self):
        text = f"Players: {self.players}\n"
        text += f"Number of matches: {self.num_matches}\n"
        text += f"Games: {self.games}\n"
        return text
    
    def play_match(self) -> None:
        """
        Play the match.
        Example:
            >>> match = Match([Player("Alice"), Player("Bob"), Player("Charlie")], 1)
            >>> match.play_match()
        """
        for _ in range(self.num_matches*self.num_players): #play the number of matches
            game = Game(self.players) #create a new game
            game.setup_game() #setup the game
            game.play_game() #play the game
            self.games.append(game) #add the game to the list of games
            self.players = self.players[1:] + self.players[:1] #rotate players
        return None
    
    @property
    def scores(self) -> dict:
        """
        Get the scores of the players in the match.
        Returns:
            dict: The scores of the players in the match.
        Example:
            >>> match = Match([Player("Alice"), Player("Bob"), Player("Charlie")], 1)
            >>> match.play_match()
            >>> match.scores
            {'Alice': 0, 'Bob': 0, 'Charlie': 0}
        """

        scores = {player.name:0 for player in self.players}
        for game in self.games:
            for player in game.players:
                scores[player.name] += player.score
        return scores
