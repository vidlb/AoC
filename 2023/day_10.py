# North, east, south, west
POS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INVERT_POS = {0: 2, 1: 3, 2: 0, 3: 1, -1: -1}
LUT = {
    "|": [("7", "F", "|"), (), ("J", "L", "|"), ()],
    "-": [(), ("7", "J", "-"), (), ("L", "F", "-")],
    "L": [("7", "F", "|"), ("7", "J", "-"), (), ()],
    "J": [("7", "F", "|"), (), (), ("F", "L", "-")],
    "7": [(), (), ("L", "J", "|"), ("F", "L", "-")],
    "F": [(), ("7", "J", "-"), ("L", "J", "|"), ()],
}


def find_start(data: list):
    for n, line in enumerate(data):
        if "S" in line:
            return n, line.index("S")


def guess_symbol(data: list, y: int, x: int):
    count = {}
    for symbol in LUT:
        pipes = 0
        for i, pos in enumerate(POS):
            next_y, next_x = y + pos[0], x + pos[1]
            if not 0 <= next_y < len(data) or not 0 <= next_x < len(data[next_y]):
                continue
            if data[next_y][next_x] in LUT[symbol][i]:
                pipes += 1
        count[symbol] = pipes
    return max(count, key=count.get)


def next_pipe_idx(data: list, orig: int, char: str, y: int, x: int) -> tuple[int]:
    for i, pos in enumerate(POS):
        if i == orig:
            continue
        next_y, next_x = y + pos[0], x + pos[1]
        if not 0 <= next_y < len(data) or not 0 <= next_x < len(data[next_y]):
            continue
        next_char = data[next_y][next_x]
        if next_char in LUT[char][i]:
            return INVERT_POS[i], next_y, next_x
    return -1, -1, -1  # found "S": loop is complete


def part_1(data: list) -> int:
    y, x = find_start(data)
    char = guess_symbol(data, y, x)
    origin = -1
    i = 0
    while y >= 0 and x >= 0:
        origin, y, x = next_pipe_idx(data, origin, char, y, x)
        char = data[y][x]
        i += 1
    return i // 2


def part_2() -> int:
    return 0


if __name__ == "__main__":
    with open("data_10.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    # print(f"Part 2 answer is {part_2(data)}")
