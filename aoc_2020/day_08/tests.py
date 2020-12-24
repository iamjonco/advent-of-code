import pytest

from aoc_2020.day_08 import part_1, part_2


@pytest.mark.parametrize("file,expected", [("inputs.txt", 1782), ["example.txt", 5]])
def test_part_1(file, expected):
    assert part_1(file) == expected


@pytest.mark.parametrize("file,expected", [("inputs.txt", 797), ["example.txt", 8]])
def test_part_2(file, expected):
    assert part_2(file) == expected
