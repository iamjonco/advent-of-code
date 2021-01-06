import fileinput
from collections import namedtuple

dirs = ["E", "S", "W", "N"]

Instruction = namedtuple("Instruction", ["op", "value"])


def get_inputs(filename=None):
    return (
        Instruction(l[0], int(l[1:])) for l in fileinput.input(filename or "inputs.txt")
    )


def part_1(filename=None):
    instructions = get_inputs(filename)

    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    d = 0
    x = 0
    y = 0

    for i in instructions:
        # Direct actions
        if i.op == "N":
            y += i.value
        elif i.op == "S":
            y -= i.value
        elif i.op == "E":
            x += i.value
        elif i.op == "W":
            x -= i.value

        # Directional actions
        elif i.op == "L":
            for _ in range(i.value // 90):
                d = (d + 3) % 4
        elif i.op == "R":
            for _ in range(i.value // 90):
                d = (d + 1) % 4
        elif i.op == "F":
            x += dxy[d][0] * i.value
            y += dxy[d][1] * i.value

        # Fall through
        else:
            raise AttributeError("Bad instruction")

    return abs(x) + abs(y)


def part_2(filename=None):
    instructions = get_inputs(filename)

    wx = 10
    wy = 1
    x = 0
    y = 0

    for i in instructions:
        # Move waypoint
        if i.op == "N":
            wy += i.value
        elif i.op == "S":
            wy -= i.value
        elif i.op == "E":
            wx += i.value
        elif i.op == "W":
            wx -= i.value

        # Rotate waypoint
        elif i.op == "L":
            for _ in range(i.value // 90):
                wx, wy = -wy, wx
        elif i.op == "R":
            for _ in range(i.value // 90):
                wx, wy = wy, -wx

        # Move ship
        elif i.op == "F":
            x += wx * i.value
            y += wy * i.value

        # Fall through
        else:
            raise AttributeError("Bad instruction")

    return abs(x) + abs(y)


if __name__ == "__main__":
    print("Day 12")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
