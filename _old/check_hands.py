from collections import defaultdict

import data


def check_flush(hand):
    suits = [card.suit for card in hand]
    return True if len(set(suits)) == 1 else False


def check_straight(hand):
    values = [card.value for card in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [data.VALUES[i] for i in values]
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
