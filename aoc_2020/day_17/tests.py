from aoc_2020.day_17 import part_1, part_2


def test_part_1_example():
    assert part_1("example.txt") == 112


def test_part_2_example():
    assert part_2("example.txt") == 848


def test_part_1():
    assert part_1("inputs.txt") == 202


def test_part_2():
    assert part_2("inputs.txt") == 2028
