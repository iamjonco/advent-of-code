import re

start = "1113122113"


def calculate(r: int, sequence: str = None):
    n = str(sequence) if sequence else start

    def replace(m):
        s = m.group(1)
        return f"{len(s)}{s[0]}"

    regex = re.compile(r"((\d)\2*)")
    for _ in range(r):
        n = regex.sub(replace, n)

    return len(n)


def part_1(sequence=None):
    return calculate(40, sequence)


def part_2(sequence=None):
    return calculate(50, sequence)


if __name__ == "__main__":
    print("Day 10")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
