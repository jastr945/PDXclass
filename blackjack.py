'''

Let's start modeling a game of blackjack.

Card class with a suit and a rank Deck class with a collection of cards Hand class with a collection of cards from a deck.

Use multiple modules.

In the deck module, implement methods that:

    Return a shuffled deck
    Cut the deck
    Draw a card off the top of a deck

In the hand module, implement methods that:

    Add a card to a hand
    Allow a user to type in a hand and have it be converted into a Hand object

In the game module, implement top-level functions that:

    Start a new game of Blackjack, or Quit
    Score a hand
    Bust if the score is over 21


'''



import random


suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen']


class Card:
    """
    This class creates a card.
    """


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __repr__(self):
        return '{} of {}'. format(self.rank, self.suit)


class Deck:
    """
    This class creates an entire deck.
    """


    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))


    def __repr__(self):
        """
        Returns a string containing a printable representation of an object.
        """
        return '{}'.format(self.rank, self.suit)


    def cut_and_shuffle(self):
        """
        Cuts the deck in a random manner and shuffles it.
        """
        cutting_point = random.randrange(len(self.cards))
        bottom = self.cards[cutting_point:]
        top = self.cards[:cutting_point]
        cutdeck = bottom + top
        random.shuffle(cutdeck)
        return cutdeck


d = Deck()
print(d.cards)
print(d.cut_and_shuffle())
