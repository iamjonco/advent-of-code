import functools
from collections import namedtuple
from enum import Enum, auto

import util


class Op(Enum):
    ACC = auto()
    JMP = auto()
    NOP = auto()


Result = namedtuple("Result", ["acc", "pos", "has_error"])
Instruction = namedtuple("Instruction", ["op", "value"])


def i(*args):
    print(*args)
    return []


class Console:
    def __init__(self, instructions):
        self.instructions = instructions

    @staticmethod
    def from_file(fp: str):
        with open(fp) as f:
            instructions = []
            for line in f.readlines():
                parts = line.strip().split()
                instructions.append(Instruction(parts[0], int(parts[1])))
            return Console(instructions)

    def execute(self, correct_error=False):
        if correct_error:
            for pos, ins in enumerate(self.instructions):
                if ins.op == "acc":
                    continue

                copy = self.instructions.copy()
                copy[pos] = Instruction("nop" if ins.op == "jmp" else "jmp", ins.value)
                result = self._execute(copy)
                if not result.has_error:
                    return result
        else:
            return self._execute(self.instructions)

    def _execute(self, instructions):
        has_error = False
        acc = 0
        pos = 0
        visited = set()
        instructions = instructions or self.instructions

        while pos < len(instructions):
            has_error = pos in visited
            if has_error:
                break

            visited.add(pos)
            current = instructions[pos]

            # ACC
            if current.op == "acc":
                acc += current.value
                pos += 1

            # JMP
            elif current.op == "jmp":
                pos += current.value

            # NOP
            else:
                pos += 1

        return Result(acc, pos, has_error)


def example_1():
    console = Console.from_file(util.get_input_path("day8_2.txt"))
    result = console.execute()
    assert result.has_error
    assert result.acc == 5
    assert result.pos == 1


def part_1():
    console = Console.from_file(util.get_input_path("day8_1.txt"))
    result = console.execute()
    assert result.has_error
    assert result.acc == 1782
    assert result.pos == 306


def part_2():
    console = Console.from_file(util.get_input_path("day8_1.txt"))
    result = console.execute(correct_error=True)
    print(result)


if __name__ == "__main__":
    example_1()
    part_1()
    part_2()
