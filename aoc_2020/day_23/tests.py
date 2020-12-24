from aoc_2020.day_23 import part_1, part_2


def test_part_1():
    assert part_1("389125467") == 67384529
    assert part_1("487912365") == 89573246


def test_part_2():
    assert part_2("389125467") == 149245887792
    assert part_2("487912365") == 2029056128
