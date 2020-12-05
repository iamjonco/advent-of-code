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


def part_1(inputs: List[BoardingPass]):
    max_seat_id = 0
    for bp in inputs:
        seat_id = bp.seat_id
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    assert max_seat_id == 878


def part_2(inputs: List[BoardingPass]):
    # Get all the passes possible for the plane
    all_passes = [
        BoardingPass("".join([*row, *column]))
        for row in itertools.product("FB", repeat=7)
        for column in itertools.product("LR", repeat=3)
    ]
    assert len(all_passes) == 128 * 8

    # Removing those that are not available
    for row in ["FFFFFFF", "BBBBBBB"]:
        for column in itertools.product("LR", repeat=3):
            all_passes.remove(BoardingPass("".join([row, *column])))
    assert len(all_passes) == (128 * 8) - 16

    empty = set(all_passes) - set(inputs)
    empty_ids = [bp.seat_id for bp in empty]
    input_ids = [bp.seat_id for bp in inputs]

    result = []
    for i in empty_ids:
        if i + 1 in input_ids and i - 1 in input_ids:
            result.append(i)

    assert len(result) == 1
    assert result[0] == 504


if __name__ == "__main__":
    with open(util.get_input_path("day5_1.txt")) as f:
        passes = [BoardingPass(line.strip()) for line in f.readlines()]
    part_1(inputs)
    part_2(passes)
