# https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html/
import random
from collections import defaultdict


# settings below this line
USE_SUIT_CHAR = True
USE_CLEAR_SUIT_CHAR = False
NUMBER_OF_PLAYERS = 2
STARTING_CARDS = 5
NUMBER_OF_DECKS = 2
ACES_HIGH = False
DRAW_CARDS = False
# settings above this line

SUITS = {
    "S": "\u2660" if not USE_CLEAR_SUIT_CHAR else "\u2664",
    "D": "\u2666" if not USE_CLEAR_SUIT_CHAR else "\u2662",
    "C": "\u2663" if not USE_CLEAR_SUIT_CHAR else "\u2667",
    "H": "\u2665" if not USE_CLEAR_SUIT_CHAR else "\u2661",
}

VALUES = (
    {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    if ACES_HIGH
    else {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }
)

HANDS = {
    9: "straight-flush",
    8: "four-of-a-kind",
    7: "full-house",
    6: "flush",
    5: "straight",
    4: "three-of-a-kind",
    3: "two-pairs",
    2: "one-pair",
    1: "highest-card",
}

# HANDS
# Royal Flush - 10, J, Q, K, A same suit
# Straight Flush - 5 cards in order (a is 1 or 14)
# Four of a Kind - 4 cards same value
# Full House - three of a kind, and two of a kind
# Flush - 5 cards same suit, no order
# Straight - 5 cards in order, not same suit
# Three of a Kind - 3 cards same value
# Two Pair - 2 pairs
# Pair - 2 cards same value
# High Card - highest card


def check_flush(hand):
    suits = [card.suit for card in hand]
    return True if len(set(suits)) == 1 else False


def check_straight(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [VALUES[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    else:
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False


def check_straight_flush(hand):
    return True if check_flush(hand) and check_straight(hand) else False


def check_four_of_a_kind(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    return True if sorted(value_counts.values()) == [1, 4] else False


def check_full_house(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    return True if sorted(value_counts.values()) == [2, 3] else False


def check_three_of_a_kind(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    return True if set(value_counts.values()) == set([3, 1]) else False


def check_two_pair(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    return True if sorted(value_counts.values()) == [1, 2, 2] else False


def check_one_pair(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    return True if 2 in value_counts.values() else False


def check_hand(hand):
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pair(hand):
        return 3
    if check_one_pair(hand):
        return 2
    return 1


def check_tie(scores):
    return scores


def check_score(hands):
    scores = {}
    scores["players"] = {}
    player = 0
    scores["winning_players"] = []
    # TODO make list to dictionary and apply player: score
    scores["winning_hand"] = []
    scores["winning_hand_name"] = ""
    scores["winning_hand_value"] = 0

    for hand in hands:
        checked_hand = check_hand(hand)
        scores["players"][player] = {}
        scores["players"][player]["hand"] = hand
        scores["players"][player]["highest_card"] = 0
        scores["players"][player]["hand_name"] = HANDS[checked_hand]
        for card in hand:
            if VALUES[card.value] > scores["players"][player]["highest_card"]:
                scores["players"][player]["highest_card"] = VALUES[card.value]
        if checked_hand > scores["winning_hand_value"]:
            scores["winning_players"].clear()
            scores["winning_hand_value"] = checked_hand
            scores["winning_hand_name"] = HANDS[checked_hand]
            scores["winning_hand"] = hand
            scores["winning_players"].append(player)
        elif checked_hand == scores["winning_hand_value"]:
            scores["winning_players"].append(player)
        player += 1
    check_tie(scores)
    return scores
    # TODO add tie logic


def get_suit_letter(suits, char):
    for k, v in suits.items():
        if char == v:
            return k
    return 0


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value}{get_suit_letter(SUITS, self.suit)}"

    def print(self, card):
        for height in range(7):
            print(self.build(height, card.suit, card.value))

    def build(self, line: int, suit: str, value: str):
        rows = [
            "┌─────────┐",
            "│      {:>2} │".format(value),
            "│         │",
            "│    {}    │".format(suit),
            "│         │",
            "│ {:<2}      │".format(value),
            "└─────────┘",
        ]

        # "┌─────────┐"
        # "│      || │"
        # "│         │"
        # "│    |    │"
        # "│         │"
        # "│ ||      │"
        # "└─────────┘"
        # ♥ ♠ ♣ ♦
        # u2660 u2666 u2663 u2665
        # u2664 u2662 u2667 u2661

        return rows[line]


class Deck:
    cards = []

    def __init__(self, number_of_decks):
        cards = []
        for _ in range(number_of_decks):
            cards += [
                Card(value, suit if not USE_SUIT_CHAR else SUITS[suit])
                for suit in SUITS
                for value in VALUES
            ]
        random.shuffle(cards)
        self.cards = cards

    def deal(self, number_of_cards):
        dealt = []
        for _ in range(number_of_cards):
            if len(self.cards) != 0:
                dealt.append(self.cards.pop())
            else:
                print("No more cards!")
        return dealt

    def shuffle(self):
        random.shuffle(self.cards)


class Hand:
    cards = []

    def discard(self, discarded_cards):
        return [self.cards.pop(self.cards.index(card)) for card in discarded_cards]

    def print(self, player_number):
        print(f"Player {player_number + 1}")
        for height in range(7):
            if DRAW_CARDS:
                for card in self.cards:
                    print(card.build(height, card.suit, card.value), end="")
                print()


def play(num_players: int, starting_cards: int, number_of_decks: int = 1):
    hands = []
    deck = Deck(number_of_decks)
    hand = Hand()
    for player in range(num_players):
        hand.cards = deck.deal(starting_cards)
        hand.print(player)
        hands.append(hand.cards)
        print(f"{hand.cards}\n")
    score = check_score(hands)
    # print(f"Results\nWinner: Player(s) {score['winning_players']}\nScore: {score['winning_hand_name']}\nHand: {score['winning_hand']}\n")
    print(
        f"Results\nWinner: Player(s) {[x + 1 for x in score['winning_players']]}\nScore: {score['winning_hand_name']}\nHand: {score['winning_hand']}\n"
    )
    print(f"Scores\n{score}\n")


def main():
    if NUMBER_OF_PLAYERS > 0 and STARTING_CARDS > 0 and NUMBER_OF_DECKS > 0:
        play(NUMBER_OF_PLAYERS, STARTING_CARDS, NUMBER_OF_DECKS)
    else:
        print(
            "Check your settings!\nMust have at least 1 player, 1 starting card, and 1 deck."
        )


if __name__ == "__main__":
    main()
