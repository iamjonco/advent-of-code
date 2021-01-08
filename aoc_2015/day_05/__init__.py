import fileinput
import re


def get_inputs(filename=None):
    return (l.strip() for l in fileinput.input(filename or "inputs.txt"))


def part_1(filename=None):
    vowels = re.compile(r"([aeiou].*){3,}")
    double = re.compile(r"(.)\1")
    illegal = re.compile(r"ab|cd|pq|xy")
    return sum(
        1
        for s in get_inputs(filename)
        if vowels.search(s) and double.search(s) and not illegal.search(s)
    )


def part_2(filename=None):
    double = re.compile(
        r"(..).*\1"
    )  # match any two chars then find the same capture group anywhere after
    sandwich = re.compile(r"(.).\1")  # match repeated char with one char in between
    return sum(
        1 for s in get_inputs(filename) if double.search(s) and sandwich.search(s)
    )


if __name__ == "__main__":
    print("Day 05")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
