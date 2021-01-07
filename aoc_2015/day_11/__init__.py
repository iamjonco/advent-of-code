import fileinput


def get_inputs(filename=None):
    return fileinput.input(filename or "inputs.txt")


def part_1(filename=None):
    pass


def part_2(filename=None):
    pass


if __name__ == "__main__":
    print("Day 11")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
