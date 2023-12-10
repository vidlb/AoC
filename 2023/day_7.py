from collections import Counter

CARDS = list("AKQJT98765432")


def hand_type(hand: Counter) -> int:
    mx, le = max(hand.values()), len(hand.values())
    if mx == 5:
        return 0  # five of a kind
    if mx == 4:
        return 1  # four of a kind
    if mx == 3 and le == 2:
        return 2  # full house
    if mx == 3:
        return 3  # thee of a kind
    if mx == 2 and le == 3:
        return 4  # two pair
    if mx == 2:
        return 5  # one pair
    return 6  # high_card


def cards_score(hand: str):
    return tuple(CARDS.index(c) for c in hand)


def parse_games(text: str):
    hands = []
    for game in text.splitlines():
        hand, bid = game.split()
        counter = Counter(hand)
        hands.append((hand, int(bid), hand_type(counter), cards_score(hand)))
    return hands


def part_1(text: str):
    games = sorted(parse_games(text), key=lambda g: (g[2], g[3]), reverse=True)
    return sum(i * g[1] for i, g in enumerate(games, 1))


def part_2(text: str):
    ...


if __name__ == "__main__":
    with open("data_7.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
