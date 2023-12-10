from math import prod


def n_times(time, dist) -> tuple[int]:
    return tuple(i for i in range(time) if i * (time - i) > dist)


def part_1(text: str) -> int:
    time, dist, _ = text.split("\n")
    time = tuple(int(t) for t in time.split(":")[1].split())
    dist = tuple(int(d) for d in dist.split(":")[1].split())
    return prod(len(n_times(t, d)) for t, d in zip(time, dist))


def part_2(text: str) -> int:
    time, dist, _ = text.split("\n")
    time = time.split(":")[1].replace(" ", "")
    dist = dist.split(":")[1].replace(" ", "")
    return len(n_times(int(time), int(dist)))


if __name__ == "__main__":
    with open("data_6.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
