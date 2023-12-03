import re
import math
from itertools import chain
from typing import Generator


def check_char(char: str) -> bool:
    if char.isdigit() or char == ".":
        return False
    return True


def collect_matches(num: re.Match, line: str, check_pos: bool):
    matches = []
    start, end = num.span()
    if check_pos and any(check_char(c) for c in line[start:end]):
        matches.append(num)
    elif start > 0 and check_char(line[start - 1]):
        matches.append(num)
    elif end < len(line) - 1 and check_char(line[end]):
        matches.append(num)
    return matches


def iter_parts(text: list[str], yield_values: bool = False) -> Generator:
    exp = re.compile(r"\d+")
    for i, line in enumerate(text):
        parts = []
        for num in exp.finditer(line):
            parts.extend(collect_matches(num, line, False))
            if i > 0:
                parts.extend(collect_matches(num, text[i - 1], True))
            if i < len(text) - 1:
                parts.extend(collect_matches(num, text[i + 1], True))
        if yield_values:
            yield [int(p.group()) for p in parts]
        else:  # yield matches
            yield parts


def part_1(text: list[str]) -> int:
    return sum(chain.from_iterable(iter_parts(text, yield_values=True)))


def collect_parts(gear: re.Match, parts: list[re.Match]):
    adj_numbers = []
    for part in parts:
        pos_range = range(part.start(), part.end() + 1)
        if gear.start() in pos_range or gear.end() in pos_range:
            adj_numbers.append(int(part.group()))
    return adj_numbers


def part_2(text: list[str]) -> Generator:
    parts = list(iter_parts(text))
    gears = [list(re.finditer(r"\*", line)) for line in text]
    tot = 0
    for i, gears in enumerate(gears):
        for gear in gears:
            adj_numbers = collect_parts(gear, parts[i])
            if i > 0:
                adj_numbers.extend(collect_parts(gear, parts[i - 1]))
            if i < len(text) - 1:
                adj_numbers.extend(collect_parts(gear, parts[i + 1]))
            if len(adj_numbers) == 2:
                tot += math.prod(adj_numbers)
    return tot


if __name__ == "__main__":
    with open("data_3.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
