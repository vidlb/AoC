import math
from typing import Generator

CUBES_MAX = {"red": 12, "green": 13, "blue": 14}


def parse_game(string: str) -> tuple[int, list[list[str]]]:
    game_id, draws = string.split(": ")
    draws = [d.split(", ") for d in draws.split("; ")]
    return int(game_id.split()[1]), draws


def color_count(draw: list[str]) -> dict:
    counter = {"red": 0, "green": 0, "blue": 0}
    for color in draw:
        count, color_name = color.split()
        counter[color_name] += int(count)
    return counter


def part_1(text: list[str]) -> Generator:
    for string in text:
        game_id, draws = parse_game(string)
        maxed_out = False
        for draw in draws:
            counter = color_count(draw)
            for color, count in counter.items():
                if count > CUBES_MAX[color]:
                    maxed_out = True
        if not maxed_out:
            yield game_id


def part_2(text: list[str]) -> Generator:
    for string in text:
        _, draws = parse_game(string)
        counters = [color_count(d) for d in draws]
        cubes = {"red": 0, "green": 0, "blue": 0}
        for counter in counters:
            for color, count in counter.items():
                if count > cubes[color]:
                    cubes[color] = count
        yield math.prod(cubes.values())


if __name__ == "__main__":
    with open("data_2.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {sum(part_1(data))}")
    print(f"Part 2 answer is {sum(part_2(data))}")
