import itertools
from collections import namedtuple
from typing import Union

import util


def get_inputs(file=None):
    if isinstance(file, str):
        with open(util.get_input_path(file)) as f:
            lines = [s.strip() for s in f.readlines()]
    else:
        lines = file

    program = {}
    mask = None
    for l in lines:
        # Mask
        if l.startswith("mask"):
            mask = l.split("=")[1].strip()
            program[mask] = []
        # Memory
        else:
            value = int(l[4 : l.index("]")]), int(l[l.index("=") + 2 :])
            program[mask].append(value)

    return program


def mask_value(v: int, m: str):
    return int(
        "".join([i if j == "X" or i == j else j for i, j in zip(format(v, "036b"), m)]),
        2,
    )


def floating_mask(v: int, m: str):
    masked = "".join([i if j == "0" else j for i, j in zip(format(v, "036b"), m)])
    masked = masked.replace("X", "{}")

    floating = m.count("X")
    if floating > 0:
        resolved = []
        for bits in itertools.product(["0", "1"], repeat=floating):
            resolved.append(masked.format(*bits))
        return [int(r, 2) for r in resolved]

    return [v]


def part_1(program):
    memory = {}
    for mask, instructions in program.items():
        for i in instructions:
            memory[i[0]] = mask_value(i[1], mask)
    return sum(memory.values())


def part_2(program):
    memory = {}
    for mask, instructions in program.items():
        for i in instructions:
            to_write = floating_mask(i[0], mask)
            for addr in to_write:
                memory[addr] = i[1]
    return sum(memory.values())


if __name__ == "__main__":
    real_input = get_inputs("day14_1.txt")

    # Part 1
    example_1 = get_inputs(
        [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0",
        ]
    )
    assert part_1(example_1) == 165
    assert part_1(real_input) == 7611244640053

    # Part 2
    example_2 = get_inputs(
        [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1",
        ]
    )
    assert part_2(example_2) == 208
    print(part_2(real_input))
