import fileinput
from functools import reduce


def get_inputs(filename=None):
    fi = fileinput.input(filename or "inputs.txt")

    rules = {}
    line: str = fi.readline().strip()
    while len(line) > 0:
        parts = line.split(":")
        rules[parts[0].strip()] = [
            int(i) for i in parts[1].strip().replace(" or ", "-").split("-")
        ]
        line = fi.readline().strip()

    assert fi.readline().strip() == "your ticket:"
    tickets = [[int(i) for i in fi.readline().strip().split(",")]]

    assert fi.readline().strip() == ""
    assert fi.readline().strip() == "nearby tickets:"
    tickets.extend([[int(i) for i in t.strip().split(",")] for t in fi])

    return rules, tickets


def get_invalid_field(rules: dict[str, list[int]], ticket: list[int]):
    for i in ticket:
        conditions = [
            i in range(r[0], r[1] + 1) or i in range(r[2], r[3] + 1)
            for r in rules.values()
        ]
        if not any(conditions):
            return i
    return 0


def get_field_map(rules: dict[str, list[int]], ticket: list[int]):
    fields = []
    for i in ticket:
        field_set = set()
        for k, v in rules.items():
            if i in range(v[0], v[1] + 1) or i in range(v[2], v[3] + 1):
                field_set.add(k)
        if len(field_set) > 0:
            fields.append(field_set)
        else:
            return None
    return fields


def part_1(filename=None):
    rules, tickets = get_inputs(filename)
    invalid = (get_invalid_field(rules, t) for t in tickets)
    return sum(invalid)


def part_2(filename=None):
    rules, tickets = get_inputs(filename)
    # Get potential fields for valid tickets
    field_maps = []
    for t in tickets:
        fm = get_field_map(rules, t)
        if fm:
            field_maps.append(fm)

    resolved = []
    for pos in range(len(field_maps[0])):
        resolved.append(set.intersection(*[t[pos] for t in field_maps]))

    # loop through and remove already assigned until all sets are len 1
    locked = [False] * len(resolved)
    while False in locked:
        singles = {f for r in resolved if len(r) == 1 for f in r}
        for i, v in enumerate(locked):
            if not v:
                locked[i] = len(resolved[i]) == 1

        for i, v in enumerate(resolved):
            if not locked[i]:
                resolved[i] = v.difference(singles)

    # flatten
    resolved = [k for s in resolved for k in s]
    departure_value = [
        tickets[0][i] for i, k in enumerate(resolved) if "departure" in k
    ]
    return reduce(lambda x, y: x * y, departure_value, 1)


if __name__ == "__main__":
    print("Day 16")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
