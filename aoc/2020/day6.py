import util


def get_groups():
    with open(util.get_input_path("day6_1.txt")) as f:
        lines = [line.strip() for line in f.readlines()]

    # Split input into groups
    groups = [[]]
    current = groups[-1]
    for line in lines:
        if not line:
            groups.append([])
            current = groups[-1]
            continue

        current.append({s for s in line})

    return groups


def part_1():
    groups = get_groups()
    counts = [len(set.union(*g)) for g in groups]
    assert sum(counts) == 6683


def part_2():
    groups = get_groups()
    counts = [len(set.intersection(*g)) for g in groups]
    assert sum(counts) == 3122


if __name__ == "__main__":
    part_1()
    part_2()
