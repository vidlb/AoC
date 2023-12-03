import re
import math
from itertools import chain
from typing import Generator


def check_match(number: re.Match, line: str, span_check: bool) -> bool:
    expr = re.compile(r"\d|\.")

    def check_char(char: str) -> bool:
        return expr.match(char)

    start, end = number.span()
    if span_check and any(check_char(c) for c in line[start:end]):
        return True
    if start > 0 and check_char(line[start - 1]):
        return True
    if end < len(line) - 1 and check_char(line[end]):
        return True
    return False


def iter_parts(text: list[str], yield_values: bool = False) -> Generator:
    expr = re.compile(r"\d+")
    for i, line in enumerate(text):
        parts = []
        for num in expr.finditer(line):
            if check_match(num, line, False):
                parts.append(num)
            elif i > 0 and check_match(num, text[i - 1], True):
                parts.append(num)
            elif i < len(text) - 1 and check_match(num, text[i + 1], True):
                parts.append(num)
        if yield_values:
            yield [int(p.group()) for p in parts]
        else:  # yield matches, for part 2
            yield parts


def part_1(text: list[str]) -> int:
    return sum(chain.from_iterable(iter_parts(text, yield_values=True)))


def collect_parts(gear: re.Match, parts: list[re.Match]) -> list[int]:
    adj_numbers = []
    for part in parts:
        pos_range = range(part.start(), part.end() + 1)
        if gear.start() in pos_range or gear.end() in pos_range:
            adj_numbers.append(int(part.group()))
    return adj_numbers


def part_2(text: list[str]) -> int:
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
