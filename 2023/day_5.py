from collections import OrderedDict


def parse_map(block: str):
    _, *numbers = block.split("\n")
    return tuple(tuple(map(int, n.split())) for n in numbers if n)


def parse_data(text: str, sort_by_src: bool = True) -> OrderedDict:
    seeds, *blocks = text.split("\n\n")
    seeds = tuple(int(s) for s in seeds.split(": ")[1].split())
    map_ranges = OrderedDict()
    for b in blocks:
        name, *lines = b.split("\n")
        maps = tuple(tuple(map(int, l.split())) for l in lines if l)
        map_ranges[name] = tuple(sorted(maps, key=lambda m: m[1 if sort_by_src else 0]))
    return seeds, map_ranges


def get_location(seed: int, map_ranges: list) -> int:
    key = seed
    for m in map_ranges:
        if key > m[-1][1] + m[-1][2]:
            continue
        for dst, src, rng in m:
            if src <= key < src + rng:
                key = dst + (key - src)
                break
    return key


def part_1(text: str):
    seeds, map_ranges = parse_data(text)
    map_ranges = list(map_ranges.values())
    return min(get_location(s, map_ranges) for s in seeds)


def get_seed(location: int, map_ranges: list) -> int:
    key = location
    for m in map_ranges:
        if key > m[-1][0] + m[-1][2]:
            continue
        for src, dst, rng in m:
            if src <= key < src + rng:
                key = dst + (key - src)
                break
    return key


def part_2(text: str):
    sd, map_ranges = parse_data(text, sort_by_src=False)
    map_ranges = list(reversed(map_ranges.values()))
    seed_ranges = [(sd[i], sd[i + 1]) for i in range(0, len(sd), 2)]

    def check_seed_ranges(seed: int):
        return any((start <= seed < start + rng) for (start, rng) in seed_ranges)

    max_loc = max(loc[0] + loc[2] for loc in map_ranges[0])
    for loc in range(0, max_loc):
        if check_seed_ranges(get_seed(loc, map_ranges)):
            return loc


if __name__ == "__main__":
    with open("data_5.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
