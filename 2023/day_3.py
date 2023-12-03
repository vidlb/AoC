import re
import math
from typing import Generator


def check_char(char: str) -> bool:
    if char.isdigit() or char == ".":
        return False
    return True


def collect_matches(matches: list[re.Match], num: re.Match, line: str, check_pos: bool):
    start, end = num.span()
    if check_pos and any(check_char(c) for c in line[start:end]):
        return matches.append(num)
    if start > 0 and check_char(line[start - 1]):
        return matches.append(num)
    if end < len(line) - 1 and check_char(line[end]):
        return matches.append(num)
    return None


def find_parts(text: list[str]) -> Generator:
    exp = re.compile(r"\d+")
    for i, line in enumerate(text):
        parts = []
        for num in exp.finditer(line):
            collect_matches(parts, num, line, False)
            if i > 0:
                collect_matches(parts, num, text[i - 1], True)
            if i < len(text) - 1:
                collect_matches(parts, num, text[i + 1], True)
        yield parts


def part_1(text: list[str]) -> int:
    return sum(int(num.group()) for lines in find_parts(text) for num in lines)


def check_positions(part: re.Match, gear: re.Match) -> bool:
    pos_range = range(part.start(), part.end() + 1)
    if gear.start() in pos_range or gear.end() in pos_range:
        return True
    return False


def collect_parts(adj_numbers: list[int], gear: re.Match, parts: list[re.Match]):
    for part in parts:
        if check_positions(part, gear):
            adj_numbers.append(int(part.group()))


def find_adj_numbers(text: list[str]) -> Generator:
    parts = list(find_parts(text))
    gears_list = [list(re.finditer(r"\*", line)) for line in text]
    for i, gears in enumerate(gears_list):
        for gear in gears:
            adj_numbers = []
            collect_parts(adj_numbers, gear, parts[i])
            if i > 0:
                collect_parts(adj_numbers, gear, parts[i - 1])
            if i < len(text) - 1:
                collect_parts(adj_numbers, gear, parts[i + 1])
            if len(adj_numbers) == 2:
                yield adj_numbers


def part_2(text: list[str]) -> int:
    return sum(math.prod(parts) for parts in find_adj_numbers(text))


if __name__ == "__main__":
    with open("data.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
