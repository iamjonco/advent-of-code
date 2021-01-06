import fileinput
import itertools
import re

_mask_pattern = re.compile(r"mask = ([01X]+)")
_mem_pattern = re.compile(r"mem\[([0-9]+)] = ([0-9]+)")


def get_inputs(filename=None):
    program = {}
    current = None
    for l in fileinput.input(filename or "inputs.txt"):
        if l.startswith("mask"):
            m = _mask_pattern.match(l)
            current = m.group(1)
            program[current] = []
        else:
            m = _mem_pattern.match(l)
            val = (int(m.group(1)), int(m.group(2)))
            program[current].append(val)

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


def part_1(filename=None):
    program = get_inputs(filename)
    memory = {}
    for mask, instructions in program.items():
        for i in instructions:
            memory[i[0]] = mask_value(i[1], mask)
    return sum(memory.values())


def part_2(filename=None):
    program = get_inputs(filename)
    memory = {}
    for mask, instructions in program.items():
        for i in instructions:
            to_write = floating_mask(i[0], mask)
            for addr in to_write:
                memory[addr] = i[1]
    return sum(memory.values())


if __name__ == "__main__":
    print("Day 14")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
