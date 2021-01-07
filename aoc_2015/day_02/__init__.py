import fileinput


def get_inputs(filename=None):
    return (
        [int(i) for i in x]
        for x in (
            l.strip().split("x") for l in fileinput.input(filename or "inputs.txt")
        )
    )


def part_1(filename=None):
    presents = get_inputs(filename)
    sides = map(lambda p: [p[0] * p[1], p[1] * p[2], p[2] * p[0]], presents)
    return sum(min(s) + 2 * s[0] + 2 * s[1] + 2 * s[2] for s in sides)


def part_2(filename=None):
    presents = get_inputs(filename)
    return sum(
        p[0] * p[1] * p[2]  # volume
        + min(
            [(2 * p[0] + 2 * p[1]), (2 * p[1] + 2 * p[2]), (2 * p[2] + 2 * p[0])]
        )  # calc all distances
        for p in presents
    )


if __name__ == "__main__":
    print("Day 02")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
