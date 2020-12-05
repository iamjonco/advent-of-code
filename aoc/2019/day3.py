import itertools
import re

import numpy as np

import util

INSTRUCTION_PATTERN = re.compile(r"^([UDRL])(\d+)$")


def manhattan_distance(x, y) -> int:
    return abs(x) + abs(y)


class Wire:
    def __init__(self):
        self.grid = [(0, 0)]
        self.x = 0
        self.y = 0

    @property
    def end_coord(self):
        return self.x, self.y

    def get_intersections(self, other: "Wire"):
        intersect = set(self.grid).intersection(set(other.grid))
        intersect.remove((0, 0))
        return intersect

    def steps_to_coord(self, x, y):
        return self.grid.index((x, y))

    def add(self, i: str):
        match = INSTRUCTION_PATTERN.match(i)
        if not match:
            raise ValueError(f"Could not match instruction {i}")

        direction, step = match.groups()
        step = int(step)

        if direction in "RL":
            x_inc = 1 if direction == "R" else -1
        else:
            x_inc = 0

        if direction in "UD":
            y_inc = 1 if direction == "U" else -1
        else:
            y_inc = 0

        for i in range(0, step):
            self.x += x_inc
            self.y += y_inc
            self.grid.append((self.x, self.y))

    def __repr__(self):
        x_max = max(self.grid, key=lambda c: c[0])[0]
        y_max = max(self.grid, key=lambda c: c[1])[1]
        buf = []
        for y in range(0, y_max + 1):
            buf.insert(
                0,
                "".join(
                    ["X" if (x, y) in self.grid else "." for x in range(0, x_max + 1)]
                ),
            )
        return "\n".join(buf)

    @staticmethod
    def from_str(s: str):
        w = Wire()
        for i in s.strip().split(","):
            w.add(i)
        return w


def part_1():
    with open(util.get_input_path("day3_1.txt")) as f:
        wires = [Wire.from_str(line) for line in f.readlines()]
    common_coords = wires[0].get_intersections(wires[1])
    manhattan = {manhattan_distance(*c): c for c in common_coords}
    assert min(manhattan.keys()) == 1431


def part_2():
    with open(util.get_input_path("day3_1.txt")) as f:
        lines = f.readlines()
        wire_a = Wire.from_str(lines[0])
        wire_b = Wire.from_str(lines[1])
    common_coords = wire_a.get_intersections(wire_b)
    steps = [
        wire_a.steps_to_coord(*c) + wire_b.steps_to_coord(*c) for c in common_coords
    ]
    assert min(steps) == 48012


if __name__ == "__main__":
    part_1()
    part_2()
