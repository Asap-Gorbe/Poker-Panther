import random
from collections import Counter

cards = []
suits = ["Heart", "Diamond", "Club", "Spade"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for suit in suits:
    for rank in ranks:
        cards.append(f"{rank}-{suit}")


class Player:
    def __init__(self, username,chip = 1000):
        self.username = username
        self.chip = chip
        self.isFold = False
        self.cards = []
    def bet (self,amount):
        self.chip -= amount
    def check(self):
        pass

    def fold(self):
        self.isFold = True

class PokerGame:
    def __init__(self):
        self.players = []
        self.board = []
        self.min_bet = 10

    def Flop(self):
        self.deal()
        del cards[-1]
        self.board.extend(cards[-3:])
        del cards[-3:]

    def Turn(self):
        del cards[-1]
        self.board.append(cards[-1])
        del cards[-1]

    def River (self):
        del cards[-1]
        self.board.append(cards[-1])
        del cards[-1]

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
    game.add_player(Player("Gorbe"))
    game.add_player(Player("awful master"))
    game.Flop()
    game.Turn()
    game.River()
    for player in game.players:
        print(f"{player.username} cards:", player.cards,'\n')
        merge_cards = player.cards + game.board
        print(f"{player.username} combined: ", merge_cards ,'\n' )
        ranks_only = [card.split('-')[0] for card in merge_cards]
        houses_only = [card.split('-')[1] for card in merge_cards]
        rank_counts = Counter(ranks_only)
        house_counts = Counter(houses_only)

        most_common_rank, count_rank = rank_counts.most_common(1)[0]
        most_common_house, count_house = house_counts.most_common(1)[0]

        #print(f"Most repeated rank: {most_common_rank} (appears {count_rank} times)")
        #print(f"Most repeated house: {most_common_house} (appears {count_house} times)")

        # Check for hand rankings
        if count_house >= 5:
            print(f'{player.username} has a flush of {most_common_house}','\n')

        if count_rank == 2:
            print(f'{player.username} has a pair of {most_common_rank}','\n')
        elif count_rank == 3:
            print(f'{player.username} has a Three of a kind of {most_common_rank}','\n')
        elif count_rank == 4:
            print(f'{player.username} has a for of a kind {most_common_rank}','\n')