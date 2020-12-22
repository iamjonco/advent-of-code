from aoc_2020.day_21 import part_1, part_2


def test_part_1():
    assert part_1("example.txt") == 5
    assert part_1("inputs.txt") == 2584


def test_part_2():
    assert part_2("example.txt") == "mxmxvkd,sqjhc,fvjkl"
    assert part_2("inputs.txt") == "fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb"
