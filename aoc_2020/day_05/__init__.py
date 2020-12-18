import fileinput
import itertools
from typing import List

import util


class BoardingPass:
    def __init__(self, code):
        assert len(code) == 10
        self.code = code

    def __eq__(self, other):
        if isinstance(other, BoardingPass):
            return self.code == other.code
        return False

    def __hash__(self):
        return hash(self.code)

    def __repr__(self):
        return f"<{type(self).__name__}: {self.code!r}>"

    @property
    def column(self):
        i = 0
        j = 7

        for c in self.code[7:]:
            diff = (j - i) // 2
            if c == "L":
                j = j - diff - 1
            else:
                i = i + diff + 1

        return min([i, j])

    @property
    def row(self):
        i = 0
        j = 127

        for c in self.code[0:7]:
            diff = (j - i) // 2
            if c == "F":
                j = j - diff - 1
            else:
                i = i + diff + 1

        return min([i, j])

    @property
    def seat_id(self):
        return (self.row * 8) + self.column


def get_inputs(filepath=None) -> set[int]:
    return {calc_seat_id(l.strip()) for l in fileinput.input(filepath or "inputs.txt")}


def calc_seat_id(code):
    def bsp(part, upper, i, j):
        for p in part:
            diff = (j - i) // 2
            if p == upper:
                j = j - diff - 1
            else:
                i = i + diff + 1
        return min([i, j])

    return (bsp(code[:7], "F", 0, 127) * 8) + bsp(code[7:], "L", 0, 7)


def part_1(filepath=None):
    return max(get_inputs(filepath))


def part_2(filepath=None):
    # Get all the passes possible for the plane
    all_passes = {
        calc_seat_id("".join([*row, *column]))
        for row in itertools.product("FB", repeat=7)
        for column in itertools.product("LR", repeat=3)
        if "".join(row) not in ["FFFFFFF", "BBBBBBB"]  # ignore the front and back rows
    }
    actual = get_inputs(filepath)
    return next(
        filter(lambda i: i + 1 in actual and i - 1 in actual, all_passes - actual)
    )


if __name__ == "__main__":
    print("Day 5")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
