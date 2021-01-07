import fileinput


def get_inputs(filename=None):
    fi = fileinput.input(filename or "inputs.txt")
    s = next(fi).strip()
    fi.close()
    return s


def part_1(filename=None):
    instructions = get_inputs(filename)
    ups = instructions.count("(")
    downs = len(instructions) - ups
    return ups - downs


def part_2(filename=None):
    instructions = get_inputs(filename)
    f = 0
    for idx, op in enumerate(instructions):
        if op == "(":
            f += 1
        else:
            f -= 1
        if f < 0:
            return idx + 1


if __name__ == "__main__":
    print("Day 01")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
