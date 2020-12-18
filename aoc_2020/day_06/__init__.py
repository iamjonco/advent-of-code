import fileinput


def get_inputs(filepath=None):
    groups = "".join([l for l in fileinput.input(filepath or "inputs.txt")]).split(
        "\n\n"
    )
    groups = [g.split("\n") for g in groups]
    return [[{c for c in l} for l in g] for g in groups]


def part_1(filepath=None):
    return sum(len(set.union(*g)) for g in get_inputs(filepath))


def part_2(filepath=None):
    return sum(len(set.intersection(*g)) for g in get_inputs(filepath))


if __name__ == "__main__":
    print("Day 6")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
