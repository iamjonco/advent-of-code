import itertools
from enum import Enum

import util


class OpCode(Enum):
    ADDITION = (1, "+")
    MULTIPLY = (2, "*")
    EOF = (99, None)

    def __new__(cls, code, op):
        entry = object.__new__(cls)
        entry.code = entry._value_ = code
        entry.op = op
        return entry

    def __repr__(self):
        return f"<{type(self).__name__}.{self.name}: ({self.code!r}, {self.op!r})>"


class Computer:
    def __init__(self, memory):
        if not memory:
            raise AttributeError("Initial memory is empty")
        self.memory = memory

    def evaluate(self, inputs: dict):
        mem = self.memory.copy()

        if inputs:
            for k, v in inputs.items():
                mem[k] = v

        cursor = 0
        while OpCode(mem[cursor]) != OpCode.EOF:
            operator = OpCode(mem[cursor])
            x = mem[cursor + 1]
            y = mem[cursor + 2]
            store = mem[cursor + 3]
            mem[store] = eval(f"{mem[x]}{operator.op}{mem[y]}")
            cursor += 4
        return mem[0]

    @staticmethod
    def from_file(filename):
        with open(util.get_input_path(filename)) as f:
            return Computer(
                [int(x) for line in f.readlines() for x in line.strip().split(",")]
            )


def part_1():
    computer = Computer.from_file("day2_1.txt")
    assert computer.evaluate({1: 12, 2: 2}) == 3101844


def part_2():
    computer = Computer.from_file("day2_1.txt")
    for noun, verb in itertools.product(*[range(0, 100), range(0, 100)]):
        if computer.evaluate({1: noun, 2: verb}) == 19690720:
            assert 100 * noun + verb == 8478


if __name__ == "__main__":
    part_1()
    part_2()
