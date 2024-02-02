# Clockwise : north, east, south, west
POS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INV_POS = {0: 2, 1: 3, 2: 0, 3: 1, -1: -1}
CONNECTIBLE_PIPES = {
    "-": [(), ("7", "J", "-"), (), ("L", "F", "-")],
    "|": [("7", "F", "|"), (), ("J", "L", "|"), ()],
    "7": [(), (), ("L", "J", "|"), ("F", "L", "-")],
    "J": [("7", "F", "|"), (), (), ("F", "L", "-")],
    "F": [(), ("7", "J", "-"), ("L", "J", "|"), ()],
    "L": [("7", "F", "|"), ("7", "J", "-"), (), ()],
}


def guess_symbol(data: list, y: int, x: int):
    count = {}
    for symbol in CONNECTIBLE_PIPES:
        pipes = 0
        for i, pos in enumerate(POS):
            next_y, next_x = y + pos[0], x + pos[1]
            if not 0 <= next_y < len(data) or not 0 <= next_x < len(data[next_y]):
                continue
            if data[next_y][next_x] in CONNECTIBLE_PIPES[symbol][i]:
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
        if next_char in CONNECTIBLE_PIPES[char][i]:
            return i, next_y, next_x
    return -1, -1, -1  # found "S": loop is complete


def find_start(data: list):
    for n, line in enumerate(data):
        if "S" in line:
            return n, line.index("S")


def pipe_coords(data: list) -> list[tuple]:
    y, x = find_start(data)
    char = guess_symbol(data, y, x)
    coords = [(y, x)]
    direction = -1
    while y >= 0 and x >= 0:
        direction, y, x = next_pipe_idx(data, INV_POS[direction], char, y, x)
        char = data[y][x]
        if x >= 0 and y >= 0:
            coords.append((y, x))
    return coords


def part_1(data: list) -> int:
    return len(pipe_coords(data)) // 2


def part_2(data: list) -> int:
    coords = pipe_coords(data)
    padded_coords = [*coords, coords[0]]
    pairs = zip(padded_coords, padded_coords[1:])
    # Shoelace area
    area = (
        abs(sum(row1 * col2 - row2 * col1 for (row1, col1), (row2, col2) in pairs)) / 2
    )
    # Pick's theorem
    return int(area - 0.5 * len(coords) + 1)


if __name__ == "__main__":
    with open("data_10.txt", encoding="utf-8") as io:
        data = io.read().splitlines()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
