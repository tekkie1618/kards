from collections import defaultdict

from deck import Deck
from hand import Hand
from check_score import check_score
import settings


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
    if (
        settings.NUMBER_OF_PLAYERS > 0
        and settings.STARTING_CARDS > 0
        and settings.NUMBER_OF_DECKS > 0
    ):
        play(
            settings.NUMBER_OF_PLAYERS,
            settings.STARTING_CARDS,
            settings.NUMBER_OF_DECKS,
        )
    else:
        print(
            "Check your settings!\nMust have at least 1 player, 1 starting card, and 1 deck."
        )


if __name__ == "__main__":
    main()
