import random

import card
import settings
import data


class Deck:
    cards = []

    def __init__(self, number_of_decks):
        cards = []
        for _ in range(number_of_decks):
            cards += [
                card.Card(
                    value, suit if not settings.USE_SUIT_CHAR else data.SUITS[suit]
                )
                for suit in data.SUITS
                for value in data.VALUES
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
