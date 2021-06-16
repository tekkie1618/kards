from check_hands import check_hand
import data


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
        scores["players"][player]["hand_name"] = data.HANDS[checked_hand]
        for card in hand:
            if data.VALUES[card.value] > scores["players"][player]["highest_card"]:
                scores["players"][player]["highest_card"] = data.VALUES[card.value]
        if checked_hand > scores["winning_hand_value"]:
            scores["winning_players"].clear()
            scores["winning_hand_value"] = checked_hand
            scores["winning_hand_name"] = data.HANDS[checked_hand]
            scores["winning_hand"] = hand
            scores["winning_players"].append(player)
        elif checked_hand == scores["winning_hand_value"]:
            scores["winning_players"].append(player)
        player += 1
    check_tie(scores)
    return scores
