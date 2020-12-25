import pytest

from aoc_2020.day_11 import part_1, part_2


@pytest.mark.parametrize("file,expected", [("example.txt", 37), ("inputs.txt", 2277)])
def test_part_1(file, expected):
    assert part_1(file) == expected


@pytest.mark.parametrize("file,expected", [("example.txt", 26), ("inputs.txt", 2066)])
def test_part_2(file, expected):
    assert part_2(file) == expected
