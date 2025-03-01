import random

cards = []
suits = ["Heart", "Diamond", "Club", "Spade"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for suit in suits:
    for rank in ranks:
        cards.append(f"{rank}-{suit}")

class Player:
    def __init__(self, username):
        self.username = username
        self.chips = 1000
        self.isFold = False
        self.cards = []
    
    def check(self):
        pass
    
    def bet(self, chip_count):
        pass

    def fold(self):
        self.isFold = True


class PokerGame:
    def __init__(self):
        self.players = []
        self.board = []
        self.min_bet = 10
    
    def start(self):
        self.deal()
        self.board.append(cards[-3:])
        del cards[-3:]
    
    def deal(self):
        random.shuffle(cards)
        for player in self.players:
            player.cards = cards[-2:]
            del cards[-2:]
    
    def add_player(self, player):
        self.players.append(player)


# --- Main App ---

if __name__ == "__main__":
    game = PokerGame()
    game.add_player(Player("shayan"))
    game.add_player(Player("mamad"))
    game.start()
    
    for player in game.players:
        print(player.cards)