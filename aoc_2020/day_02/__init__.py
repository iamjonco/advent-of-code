import fileinput
import re
from collections import namedtuple

Password = namedtuple("Password", ["min", "max", "char", "value"])

_PW_PATTERN = re.compile("^([0-9]+)-([0-9]+) ([a-z]): (.*)$")


def get_inputs(filepath=None) -> list:
    return [
        Password(int(v[0]), int(v[1]), v[2], v[3])
        for l in fileinput.input(filepath or "inputs.txt")
        for v in _PW_PATTERN.findall(l)
    ]


def part_1(filepath=None):
    return sum(
        1
        for pw in get_inputs(filepath)
        if pw.value.count(pw.char) in range(pw.min, pw.max + 1)
    )


def part_2(filepath):
    return sum(
        1
        for pw in get_inputs(filepath)
        if (pw.char == pw.value[pw.min - 1]) != (pw.char == pw.value[pw.max - 1])
    )


def is_valid(pw: tuple) -> bool:
    return (pw[2] == pw[3][int(pw[0]) - 1]) != (pw[2] == pw[3][int(pw[1]) - 1])


if __name__ == "__main__":
    print("Day 1")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
