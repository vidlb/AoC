from functools import lru_cache


def count_wins(line: str) -> int:
    win, own = line.split(": ")[1].split(" | ")
    return len({*win.split()} & {*own.split()})


def part_1(cards: list[str]):
    return sum(2 ** count_wins(c) // 2 for c in cards)


def part_2(cards: list[str]):
    win_len = tuple(count_wins(c) for c in cards)

    @lru_cache(maxsize=20)
    def recursive_score(line: int) -> int:
        score = 1
        for i in range(line + 1, line + 1 + win_len[line]):
            score += recursive_score(i)
        return score

    return sum(recursive_score(i) for i in range(len(win_len)))


if __name__ == "__main__":
    with open("data_4.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
