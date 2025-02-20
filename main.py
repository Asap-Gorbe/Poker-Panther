import random


class Deck:
    def __init__(self):
        self.suits = ['Hearts♥️', 'Diamonds♦️', 'Clubs♣️', 'Spades♠️']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def reset_deck(self):
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):

        return f"Deck of {len(self.cards)} cards"


# Example usage:
deck = Deck()
print(deck)
card = deck.deal()
print(f"Dealt: {card}")
print(deck)