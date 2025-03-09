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
        self.point = 0
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

def rank_to_value (rank):
    rank_values = {
        '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14
        }
    return rank_values.get(rank.strip(), None)

def get_sorted_ranks(cards):
    ranks = [card.split('-')[0] for card in cards]
    rank_values = [rank_to_value(rank) for rank in ranks]
    rank_values = list(set(rank_values))
    rank_values.sort()
    return rank_values

def is_straight(rank_values):
    count = 1
    for i in range(len(rank_values) - 1):
        if rank_values[i] + 1 == rank_values[i + 1]:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

def is_ace_low_straight(rank_values):
    return set([14, 2, 3, 4, 5]).issubset(rank_values)

def has_straight(cards):
    rank_values = get_sorted_ranks(cards)
    return is_straight(rank_values) or is_ace_low_straight(rank_values)

def has_flush(cards):
    suits = [card.split('-')[1] for card in cards]
    suit_counts = Counter(suits)
    return any(count >= 5 for count in suit_counts.values())

def has_straight_flush(cards):
    suits = [card.split('-')[1] for card in cards]
    suit_counts = Counter(suits)
    for suit, count in suit_counts.items():
        if count >= 5:
            suited_cards = [card for card in cards if card.endswith(suit)]
            if has_straight(suited_cards):
                return True
    return False

def has_royal_flush(cards):
    suits = [card.split('-')[1] for card in cards]
    suit_counts = Counter(suits)
    for suit, count in suit_counts.items():
        if count >= 5:
            suited_cards = [card for card in cards if card.endswith(suit)]
            rank_values = get_sorted_ranks(suited_cards)
            if set([10, 11, 12, 13, 14]).issubset(rank_values):
                return True
    return False

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
        if count_rank == 2:
            if len([r for r in rank_counts.values() if r == 2]) == 2:
                print(f'{player.username} has Two Pair', '\n')
                player.point = 3
            else:
                print(f'{player.username} has a Pair of {most_common_rank}', '\n')
                player.point = 2
        elif count_rank == 3:
            print(f'{player.username} has Three of a Kind of {most_common_rank}', '\n')
            player.point = 4
        elif count_rank == 4:
            print(f'{player.username} has Four of a Kind of {most_common_rank}', '\n')
            player.point = 8
        elif has_flush(merge_cards):
            print(f'{player.username} has a Flush of {most_common_house}', '\n')
            player.point = 6
        elif has_straight(merge_cards):
            print(f'{player.username} has a Straight', '\n')
            player.point = 5
        elif has_straight_flush(merge_cards):
            print(f'{player.username} has a Straight Flush!', '\n')
            player.point = 9
        elif has_royal_flush(merge_cards):
            print(f'{player.username} has a Royal Flush!!!', '\n')
            player.point = 10
