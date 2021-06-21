import settings

SUITS = {
    "S": "\u2660" if not settings.USE_CLEAR_SUIT_CHAR else "\u2664",
    "D": "\u2666" if not settings.USE_CLEAR_SUIT_CHAR else "\u2662",
    "C": "\u2663" if not settings.USE_CLEAR_SUIT_CHAR else "\u2667",
    "H": "\u2665" if not settings.USE_CLEAR_SUIT_CHAR else "\u2661",
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
    if settings.ACES_HIGH
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
