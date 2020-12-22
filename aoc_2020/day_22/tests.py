from aoc_2020.day_22 import part_1, part_2


def test_part_1():
    assert part_1("example.txt") == 306
    assert part_1("inputs.txt") == 33694


def test_part_2():
    assert part_2("example.txt") == 291
    assert part_2("inputs.txt") == 31835
