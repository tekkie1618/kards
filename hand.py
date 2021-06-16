import settings


class Hand:
    cards = []

    def discard(self, discarded_cards):
        return [self.cards.pop(self.cards.index(card)) for card in discarded_cards]

    def print(self, player_number):
        print(f"Player {player_number + 1}")
        for height in range(7):
            if settings.DRAW_CARDS:
                for card in self.cards:
                    print(card.build(height, card.suit, card.value), end="")
                print()
