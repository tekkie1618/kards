import data


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_suit_letter(self, suits, char):
        for k, v in suits.items():
            if char == v:
                return k
        return 0

    def __repr__(self):
        return f"{self.value}{self.get_suit_letter(data.SUITS, self.suit)}"

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
        return rows[line]
