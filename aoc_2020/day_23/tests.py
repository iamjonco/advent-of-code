import pytest

from aoc_2020.day_23 import part_1, part_2


@pytest.mark.parametrize(
    "file,expected", [("389125467", 67384529), ("487912365", 89573246)]
)
def test_part_1(file, expected):
    assert part_1(file) == expected


@pytest.mark.parametrize(
    "file,expected", [("389125467", 149245887792), ("487912365", 2029056128)]
)
def test_part_2(file, expected):
    assert part_2(file) == expected
