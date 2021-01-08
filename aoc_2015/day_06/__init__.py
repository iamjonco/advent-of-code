import fileinput
import itertools
import re
from collections import namedtuple

Instruction = namedtuple("Instruction", ["op", "start", "end"])


def get_inputs(filename=None):
    regex = re.compile(
        r"^(toggle|turn off|turn on) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$"
    )
    return (
        Instruction(
            m.group(1),
            (int(m.group(2)), int(m.group(3))),
            (int(m.group(4)), int(m.group(5))),
        )
        for l in fileinput.input(filename or "inputs.txt")
        for m in [regex.match(l)]
        if m
    )


def part_1(filename=None):
    instructions = get_inputs(filename)
    grid = {(x, y): False for x in range(1000) for y in range(1000)}

    for i in instructions:
        coords = itertools.product(
            range(i.start[0], i.end[0] + 1), range(i.start[1], i.end[1] + 1)
        )
        if i.op == "toggle":
            for c in coords:
                grid[c] = not grid[c]
        elif i.op == "turn on":
            for c in coords:
                grid[c] = True
        else:
            for c in coords:
                grid[c] = False

    return list(grid.values()).count(True)


def part_2(filename=None):
    instructions = get_inputs(filename)
    grid = {(x, y): 0 for x in range(1000) for y in range(1000)}

    for i in instructions:
        coords = itertools.product(
            range(i.start[0], i.end[0] + 1), range(i.start[1], i.end[1] + 1)
        )
        if i.op == "toggle":
            for c in coords:
                grid[c] += 2
        elif i.op == "turn on":
            for c in coords:
                grid[c] += 1
        else:
            for c in coords:
                grid[c] -= 1 if grid[c] > 0 else 0

    return sum(grid.values())


if __name__ == "__main__":
    print("Day 06")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
