def parse_data(text: str) -> list[tuple[int]]:
    return [tuple(map(int, line.split())) for line in text.splitlines()]


def get_diffs(numbers: list[int]):
    steps = []
    while not all(n == 0 for n in numbers):
        numbers = tuple(numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1))
        steps.append(numbers)
    return steps


def extrapolate(report: list[int]) -> list[list[int]]:
    diffs = get_diffs(report)
    new_data = 0
    for d in reversed(diffs):
        new_data = new_data + d[-1]
    return report[-1] + new_data


def part_1(text: str) -> int:
    return sum(extrapolate(r) for r in parse_data(text))


def extrapolate_backward(report: list[int]) -> list[list[int]]:
    diffs = get_diffs(report)
    new_data = 0
    for d in reversed(diffs):
        new_data = d[0] - new_data
    return report[0] - new_data


def part_2(text: str) -> int:
    return sum(extrapolate_backward(r) for r in parse_data(text))


if __name__ == "__main__":
    with open("data_9.txt", encoding="utf-8") as io:
        data = io.read()
    print(f"Part 1 answer is {part_1(data)}")
    print(f"Part 2 answer is {part_2(data)}")
