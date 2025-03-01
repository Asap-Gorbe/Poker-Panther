import random

from Bastion import account


class Deck:
    def __init__(self):
        self.Deck = []

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for rank in ranks:
            for suit in suits:
                self.Deck.append(f"{rank}-{suit}")

    def deal(self):
        random.shuffle(self.Deck)
        card_1_2 = self.Deck[-2:]
        del self.Deck[-2:]
        return card_1_2


class Player:
    def __init__(self, username,Deck,Chip=1000):
        self.username = username
        self.Deck = Deck
        self.Chip = Chip
    def action (self):
        action = False
    def bet (self,amount):
        action = True
        self.Chip -= amount
        if amount > self.Chip :
            print('you cant bet more than your balance ')






cards = Deck()
p1 = Player('A$AP Gorbe',Deck.deal())
p2 = Player("shayanstx", Deck.deal())
