import pytest

from aoc_2020.day_25 import part_1


@pytest.mark.parametrize("file,expected", [("inputs.txt", 16902792)])
def test_part_1(file, expected):
    assert part_1(file) == expected
