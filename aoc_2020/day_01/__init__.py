import fileinput
import itertools
import math


def get_inputs(filepath=None) -> list[int]:
    return [int(l.strip()) for l in fileinput.input(filepath or "inputs.txt")]


def find_2020(x, length):
    for i in itertools.permutations(x, length):
        if sum(i) == 2020:
            return i


def part_1(filepath=None):
    return math.prod(find_2020(get_inputs(filepath), 2))


def part_2(filepath=None):
    return math.prod(find_2020(get_inputs(filepath), 3))


if __name__ == "__main__":
    print("Day 1")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
