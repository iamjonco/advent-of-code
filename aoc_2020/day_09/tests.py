import pytest

from aoc_2020.day_09 import part_1, part_2


@pytest.mark.parametrize(
    "file,window,expected", [("inputs.txt", 25, 26134589), ["example.txt", 5, 127]]
)
def test_part_1(file, window, expected):
    assert part_1(file, window) == expected


@pytest.mark.parametrize(
    "file,window,expected", [("inputs.txt", 25, 3535124), ["example.txt", 5, 62]]
)
def test_part_2(file, window, expected):
    assert part_2(file, window) == expected
