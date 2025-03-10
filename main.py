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

def has_full_house(cards):
    rank_counts = Counter(card.split('-')[0] for card in cards)
    has_three = any(count == 3 for count in rank_counts.values())
    has_pair = any(count == 2 for count in rank_counts.values())
    return has_three and has_pair


def has_pairs(cards):
    ranks_only = [card.split('-')[0] for card in cards]
    rank_counts = Counter(ranks_only)

    pairs = [rank for rank, count in rank_counts.items() if count == 2]
    three_of_a_kind = [rank for rank, count in rank_counts.items() if count == 3]
    four_of_a_kind = [rank for rank, count in rank_counts.items() if count == 4]

    if four_of_a_kind:
        return ("Four of a Kind", max(four_of_a_kind, key=rank_to_value), 8)
    elif three_of_a_kind:
        return ("Three of a Kind", max(three_of_a_kind, key=rank_to_value), 4)
    elif len(pairs) == 2:
        return ("Two Pair", pairs, 3)
    elif len(pairs) == 1:
        return ("Pair", pairs[0], 2)
    return (None, None, 0)  # No pair

def compare_players(players):
    players.sort(key=lambda p: p.point, reverse=True)
    highest_score = players[0].point
    winners = [players[0]]

    for player in players[1:]:
        if player.point == highest_score:
            winners.append(player)
        else:
            break

    if len(winners) > 1:
        print("It's a tie between:")
        for winner in winners:
            print(f"{winner.username} with {winner.point} points")
        return winners

    print(f"The winner is {winners[0].username} with {winners[0].point} points!")
    return winners[0]

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
    print(f"{player.username} cards:", player.cards, '\n')
    merge_cards = player.cards + game.board
    print(f"{player.username} combined: ", merge_cards, '\n')

    hand, rank, points = has_pairs(merge_cards)
    if hand:
        print(f"{player.username} has {hand} ({rank})", '\n')
        player.point = points
    elif has_flush(merge_cards):
        print(f'{player.username} has a Flush', '\n')
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

winner = compare_players(game.players)