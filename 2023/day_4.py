def parse_line(line: str) -> set:
    values = line.split(": ")[1]
    win, card = values.split(" | ")
    win = set(int(w.strip()) for w in win.split())
    card = set(int(c.strip()) for c in card.split())
    return tuple(win & card)


def compute_score(win_numbers):
    n = 0
    for i in range(len(win_numbers)):
        if i == 0:
            n = 1
        else:
            n *= 2
    return n


def part_1(text: str):
    return sum(compute_score(parse_line(t)) for t in text)


def recursive_score(line_num, win_numbers: list[set]):
    score = 1
    line_end = line_num + 1 + len(win_numbers[line_num])
    for i in range(line_num + 1, line_end):
        score += recursive_score(i, win_numbers)
    return score


def part_2(text: str):
    win_sets = [parse_line(l) for l in text]
    return sum(recursive_score(i, win_sets) for i in range(len(win_sets)))


if __name__ == "__main__":
    with open("data_4.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
