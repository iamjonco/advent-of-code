from aoc_2020.day_20 import part_1, part_2


def test_part_1():
    assert part_1("example.txt") == 20899048083289
    assert part_1("inputs.txt") == 14129524957217


def test_part_2():
    assert part_2("example.txt") == 273
    assert part_2("inputs.txt") == 1649
