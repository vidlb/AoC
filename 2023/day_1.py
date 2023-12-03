import re

DIGITS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
}


def part_1(text: list[str]) -> int:
    tot = 0
    for string in text:
        numbers = list(filter(lambda s: s.isdigit(), string))
        tot += int(numbers[0] + numbers[-1])
    return tot


def part_2(text: list[str]) -> int:
    tot = 0
    for string in text:
        expr = "(?=(" + "|".join(list(DIGITS.keys()) + [r"\d"]) + "))"
        numbers = re.findall(expr, string)
        first, last = numbers[0], numbers[-1]
        tot += int(DIGITS.get(first, first) + DIGITS.get(last, last))
    return tot


if __name__ == "__main__":
    with open("data_1.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
