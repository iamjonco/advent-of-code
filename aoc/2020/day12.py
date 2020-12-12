import numpy as np

import util

_DIR_MAP = {"N": ("E", "W"), "E": ("S", "N"), "S": ("W", "E"), "W": ("N", "S")}


class Instruction:
    def __init__(self, op: str, value: int):
        self.op = op
        self.value = value

    def __str__(self):
        return f"{self.op}{self.value}"


class Ship:
    def __init__(self, x=0, y=0, face="E"):
        self.x = x
        self.y = y
        self.face = face

    def process(self, i: Instruction):
        if i.op == "N":
            return self.north(i)
        if i.op == "S":
            return self.south(i)
        if i.op == "E":
            return self.east(i)
        if i.op == "W":
            return self.west(i)

        if i.op == "F":
            return self.forward(i)

        if i.op == "R":
            return self.right(i)

        if i.op == "L":
            return self.left(i)

        raise ValueError(f"Unrecognised instruction {i}")

    def north(self, i: Instruction):
        self.y += i.value

    def south(self, i: Instruction):
        self.y -= i.value

    def east(self, i: Instruction):
        self.x += i.value

    def west(self, i: Instruction):
        self.x -= i.value

    def forward(self, i: Instruction):
        self.process(Instruction(self.face, i.value))

    def _rotate(self, degrees, index):
        for i in range(0, int(degrees / 90)):
            self.face = _DIR_MAP[self.face][index]

    def left(self, i: Instruction):
        self._rotate(i.value, 1)

    def right(self, i: Instruction):
        self._rotate(i.value, 0)

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f"ship: ({self.x},{self.y}),{self.face}"


class WaypointShip(Ship):
    def __init__(self, x=0, y=0, face="E", waypoint_x=10, waypoint_y=1):
        self.ship_x = x
        self.ship_y = y
        super(WaypointShip, self).__init__(waypoint_x, waypoint_y, face)

    def _rotate_waypoint(self, degrees):
        angle = np.deg2rad(degrees)
        r = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        o = np.atleast_2d((0, 0))
        p = np.atleast_2d((self.x, self.y))
        self.x, self.y = np.squeeze((r @ (p.T - o.T) + o.T).T).round().astype(int)

    def left(self, i: Instruction):
        self._rotate_waypoint(i.value)

    def right(self, i: Instruction):
        self._rotate_waypoint(-i.value)

    def forward(self, i: Instruction):
        self.ship_x += self.x * i.value
        self.ship_y += self.y * i.value

    @property
    def manhattan(self):
        return abs(self.ship_x) + abs(self.ship_y)

    def __str__(self):
        return f"ship: ({self.ship_x},{self.ship_y}), wp: ({self.x},{self.y})"


def get_inputs(filepath):
    with open(util.get_input_path(filepath)) as f:
        return [
            Instruction(i[0], int(i[1:])) for i in [l.strip() for l in f.readlines()]
        ]


def part_1(instructions: list[Instruction]):
    ship = Ship()
    for i in instructions:
        ship.process(i)
    assert ship.manhattan == 562


def part_2(instructions: list[Instruction]):
    ship = WaypointShip()
    for i in instructions:
        ship.process(i)
    assert ship.manhattan == 101860


if __name__ == "__main__":
    # inputs = [Instruction(s[0], int(s[1:])) for s in "F10,N3,F7,R90,F11".split(",")]
    inputs = get_inputs("day12_1.txt")
    part_1(inputs)
    part_2(inputs)
