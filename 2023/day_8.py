from itertools import cycle
from math import lcm


def parse_data(text: str) -> tuple[str, dict]:
    instr, *lines = text.splitlines()
    instr = tuple(0 if i == "L" else 1 for i in instr)
    nodes_map = {}
    for n in lines[1:]:
        node, targets = n[:-1].split(" = (")
        nodes_map[node] = tuple(targets.split(", "))
    return instr, nodes_map


def part_1(text: str) -> int:
    instructions, nodes = parse_data(text)
    key = "AAA"
    for i, lr in enumerate(cycle(instructions), 1):
        key = nodes[key][lr]
        if key == "ZZZ":
            return i
    return 0


def part_2(text: str) -> int:
    instructions, nodes = parse_data(text)

    def steps_to_z(key: str) -> int:
        for i, lr in enumerate(cycle(instructions), 1):
            key = nodes[key][lr]
            if key[2] == "Z":
                return i
        return 0

    keys = tuple(k for k in nodes if k.endswith("A"))
    steps = tuple(steps_to_z(k) for k in keys)
    return lcm(*steps)


if __name__ == "__main__":
    with open("data_8.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
