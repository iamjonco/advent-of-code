import pytest

from aoc_2020.day_10 import part_1, part_2


@pytest.mark.parametrize("file,expected", [("inputs.txt", 1885), ["example.txt", 220]])
def test_part_1(file, expected):
    assert part_1(file) == expected


@pytest.mark.parametrize(
    "file,expected", [("inputs.txt", 2024782584832), ["example.txt", 19208]]
)
def test_part_2(file, expected):
    assert part_2(file) == expected
