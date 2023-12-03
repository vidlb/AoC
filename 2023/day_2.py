import math

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


def check_draw(draw: list[str]) -> bool:
    counter = color_count(draw)
    for color, count in counter.items():
        if count > CUBES_MAX[color]:
            return False
    return True


def part_1(text: list[str]) -> int:
    tot = 0
    for string in text:
        game_id, draws = parse_game(string)
        if all(map(check_draw, draws)):
            tot += game_id
    return tot


def part_2(text: list[str]) -> int:
    tot = 0
    for string in text:
        _, draws = parse_game(string)
        used_cubes = {"red": 0, "green": 0, "blue": 0}
        for counter in (color_count(d) for d in draws):
            for color, count in counter.items():
                if count > used_cubes[color]:
                    used_cubes[color] = count
        tot += math.prod(used_cubes.values())
    return tot


if __name__ == "__main__":
    with open("data_2.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
