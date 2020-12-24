import fileinput


def get_inputs(filename=None):
    return [
        (x[0], int(x[1]))
        for x in (l.split() for l in fileinput.input(filename or "inputs.txt"))
    ]


def execute(instructions: list[tuple[str, int]]):
    visited = set()
    idx = 0
    value = 0
    try:
        while idx not in visited:
            visited.add(idx)
            op = instructions[idx][0]
            if op == "jmp":
                idx += instructions[idx][1]
            elif op == "acc":
                value += instructions[idx][1]
                idx += 1
            else:
                idx += 1
        return idx, value
    except IndexError:
        return -1, value


def part_1(filename=None):
    instructions = get_inputs(filename)
    idx, value = execute(instructions)
    return value


def part_2(filename=None):
    instructions = get_inputs(filename)
    to_replace = [
        (idx, i) for idx, i in enumerate(instructions) if i[0] in ["nop", "jmp"]
    ]
    for r in to_replace:
        modified = instructions.copy()
        modified[r[0]] = ("nop" if r[1][0] == "jmp" else "jmp", r[1][1])
        end_idx, value = execute(modified)
        if end_idx == -1:
            return value

    raise RuntimeError("Could not find bad instruction")


if __name__ == "__main__":
    print("Day 08")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
