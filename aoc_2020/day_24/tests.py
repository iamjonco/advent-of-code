from aoc_2020.day_24 import part_1, part_2


def test_part_1():
    assert part_1("example.txt") == 10
    assert part_1("inputs.txt") == 351


def test_part_2():
    assert part_2("example.txt") == 2208
    assert part_2("inputs.txt") == 3869
