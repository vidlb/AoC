from collections import OrderedDict
from time import perf_counter


def parse_map(block: str) -> tuple[tuple[int]]:
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


def part_1(text: str) -> int:
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


def part_2(text: str) -> int:
    sd, map_ranges = parse_data(text, sort_by_src=False)
    seed_ranges = [(sd[i], sd[i] + sd[i + 1]) for i in range(0, len(sd), 2)]
    seed_ranges = sorted(seed_ranges, key=lambda r: r[0])
    min_seed, max_seed = seed_ranges[0][0], seed_ranges[-1][1]
    map_ranges = list(reversed(map_ranges.values()))
    max_loc = max(loc[0] + loc[2] for loc in map_ranges[0])

    def check_seed_ranges(seed: int):
        if not min_seed <= seed < max_seed:
            return False
        return any((start <= seed < end) for (start, end) in seed_ranges)

    search = range(0, max_loc)
    print(f"Starting process with {search=}")
    for loc in search:
        seed = get_seed(loc, map_ranges)
        if check_seed_ranges(seed):
            print(f"Found {seed=}")
            return loc


if __name__ == "__main__":
    with open("data_5.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    st = perf_counter()
    print(f"Part 2 answer is {part_2(data)}")
    sp = perf_counter()
    print(f"Elpased time: {sp - st}s")
