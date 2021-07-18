#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    SUITES = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    def __init__(self):
        print("A deck was created")
        self.full_deck = [f'{rank} of {suite}' for rank in Deck.RANKS for suite in Deck.SUITES]

    def __len__(self):
        return len(self.full_deck)

    def shuffle_deck(self):
        shuffle(self.full_deck)

    def split_deck(self):
        return self.full_deck[:26], self.full_deck[-26:]

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def add(self,cards):
        self.cards.extend(cards)
    
    def remove(self,card):
        self.cards.remove(card)

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self,name):
        self.name = name

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
game = Deck()
print(f'Total cards: {len(game)}')
game.shuffle_deck()
pone, ptwo = game.split_deck()
print(f'First 5 shuffled cards of player one: {pone[:5]}')