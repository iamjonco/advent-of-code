import re

_INPUT = re.compile("([0-9]+)-([0-9]+) ([a-z]): (.*)")


def read_inputs(fp: str) -> list:
    with open(fp) as f:
        return [tuple(_INPUT.match(x).groups()) for x in f.readlines()]


def old_is_valid(pw: tuple) -> bool:
    return pw[3].count(pw[2]) in range(int(pw[0]), int(pw[1]) + 1)


def is_valid(pw: tuple) -> bool:
    return (pw[2] == pw[3][int(pw[0]) - 1]) != (pw[2] == pw[3][int(pw[1]) - 1])


if __name__ == '__main__':
    filepath = "inputs/day2_1.txt"
    inputs = read_inputs(filepath)
    results = list(filter(is_valid, inputs))
    print(len(results))
