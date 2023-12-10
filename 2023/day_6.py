from math import prod


def parse_races(text: str) -> tuple[tuple[int]]:
    time, dist, _ = text.split("\n")
    time, dist = time.split(":")[1].split(), dist.split(":")[1].split()
    return tuple(int(t) for t in time), tuple(int(d) for d in dist)


def button_times(total_time, dist) -> tuple[int]:
    times = []
    for i in range(total_time):
        run_time = total_time - i
        if i * run_time > dist:
            times.append(i)
    return tuple(times)


def part_1(text: str) -> int:
    time, dist = parse_races(text)
    runs = []
    for t, d in zip(time, dist):
        runs.append(len(button_times(t, d)))
    return prod(runs)


def parse_single_race(text: str) -> tuple[int]:
    time, dist, _ = text.split("\n")
    time, dist = time.split(":")[1].replace(" ", ""), dist.split(":")[1].replace(" ", "")
    return int(time), int(dist)


def part_2(text: str) -> int:
    return len(button_times(*parse_single_race(text)))


if __name__ == "__main__":
    with open("data_6.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
