from collections import Counter

CARDS = list("AKQJT98765432")


def cards_score(hand: str):
    return tuple(CARDS.index(c) for c in hand)


def hand_type(hand: Counter) -> int:
    mx, le = max(hand.values()), len(hand.values())
    if mx == 5:
        htype = 0  # five of a kind
    elif mx == 4:
        htype = 1  # four of a kind
    elif mx == 3 and le == 2:
        htype = 2  # full house
    elif mx == 3:
        htype = 3  # thee of a kind
    elif mx == 2 and le == 3:
        htype = 4  # two pair
    elif mx == 2:
        htype = 5  # one pair
    else:
        htype = 6  # high_card
    return htype


def part_1(text: str):
    games = []
    for game in text.splitlines():
        hand, bid = game.split()
        counter = Counter(hand)
        games.append((hand, int(bid), hand_type(counter), cards_score(hand)))

    games = sorted(games, key=lambda g: (g[2], g[3]), reverse=True)
    return sum(i * g[1] for i, g in enumerate(games, 1))


def joker_hand_type(hand: Counter) -> int:
    mx, le = max(hand.values()), len(hand.values())
    jk = hand.get("J") or 0
    if (
        mx == 5
        or jk == 4
        or (mx == 4 and jk == 1)
        or (mx == 3 and jk == 2)
        or (jk == 3 and le == 2)
    ):
        htype = 0  # five of a kind
    elif mx == 4 or (mx == 3 and jk == 1) or (jk >= 2 and le == 3):
        htype = 1  # four of a kind
    elif mx == 3 and le == 2 or jk == 1 and le == 3:
        htype = 2  # full house
    elif mx == 3 or jk == 2 or mx == 2 and jk == 1:
        htype = 3  # thee of a kind
    elif mx == 2 and le == 3:
        htype = 4  # two pair
    elif mx == 2 or mx == 1 and jk == 1:
        htype = 5  # one pair
    else:
        htype = 6  # high_card
    return htype


CARDS_WITH_JOKER = list("AKQT98765432J")


def joker_cards_score(hand: str):
    return tuple(CARDS_WITH_JOKER.index(c) for c in hand)


def part_2(text: str):
    games = []
    for game in text.splitlines():
        hand, bid = game.split()
        counter = Counter(hand)
        htype = joker_hand_type(counter)
        score = joker_cards_score(hand)
        games.append((hand, int(bid), htype, score))

    games = sorted(games, key=lambda g: (g[2], g[3]), reverse=True)
    for i, g in enumerate(games, 1):
        print(i, g)
    return sum(i * g[1] for i, g in enumerate(games, 1))


if __name__ == "__main__":
    with open("data_7.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
