import fileinput


def get_inputs(filename=None):
    adapters = sorted(int(l.strip()) for l in fileinput.input(filename or "inputs.txt"))
    adapters.append(max(adapters) + 3)
    adapters.insert(0, 0)
    return adapters


def part_1(filename=None):
    adapters = set(get_inputs(filename))
    adapters.remove(0)
    chain = [0]
    while len(adapters):
        n = next(a for a in adapters if a in range(chain[-1], chain[-1] + 4))
        chain.append(n)
        adapters.remove(n)

    diffs = {}
    for x in range(len(chain) - 1):
        d = chain[x + 1] - chain[x]
        diffs[d] = diffs.get(d, 0) + 1

    return diffs.get(1, 0) * diffs.get(3, 0)


def part_2(filename=None):
    adapters = get_inputs(filename)
    arrangements = {0: 1}
    for a in adapters:
        count = arrangements.get(a)
        for x in range(1, 4):
            ax = a + x
            if ax in adapters:
                arrangements[ax] = arrangements.get(ax, 0) + count
    return arrangements[max(adapters)]


if __name__ == "__main__":
    print("Day 10")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
