import util


def get_inputs(filepath):
    with open(util.get_input_path(filepath)) as f:
        return sorted([int(line.strip()) for line in f.readlines()])


def find_chain(adapters: list[int]):
    jolts = 0
    chain = []

    while len(chain) < len(adapters):
        for a in adapters:
            if a in chain:
                continue
            if a in range(jolts, jolts + 4):
                chain.append(a)
                break
        jolts = chain[-1]

    return chain


def get_differences(chain):
    full_chain = [0, *chain, max(chain) + 3]
    diffs = {}

    for x in range(0, len(full_chain) - 1):
        d = full_chain[x + 1] - full_chain[x]
        if d in diffs:
            diffs[d] += 1
        else:
            diffs[d] = 1

    return diffs


def find_arrangements(adapters: list[int], cache=None):
    adapters = [0, *adapters, max(adapters) + 3]
    cache = cache or {adapters[0]: 1}

    for i in adapters:
        paths = cache.get(i)
        for j in range(1, 4):
            if i + j in adapters:
                to_cache = cache.get(i + j, 0) + paths
                cache[i + j] = to_cache

    return cache[max(adapters)]


def part_1():
    adapters = get_inputs("day10_1.txt")
    chain = find_chain(adapters)
    differences = get_differences(chain)
    assert differences[1] * differences[3] == 1885


def part_2():
    adapters = get_inputs("day10_1.txt")
    arrangements = find_arrangements(adapters)
    assert 2024782584832 == arrangements


if __name__ == "__main__":
    part_1()
    part_2()
