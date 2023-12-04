from day_4 import part_1, part_2


def test_part_1():
    with open("test_data_4.txt", encoding="utf-8") as io:
        data = io.read().splitlines()

    res = part_1(data)
    assert res == 13


def test_part_2():
    with open("test_data_4.txt", encoding="utf-8") as io:
        data = io.read().splitlines()

    res = part_2(data)
    assert res == 30


if __name__ == "__main__":
    test_part_1()
    test_part_2()
