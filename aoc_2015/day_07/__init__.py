import fileinput


class cached(object):
    def __init__(self, arg, cache=None):
        self._arg = arg
        self.cache = cache or {}

    def __call__(self, graph, k):
        if k not in self.cache:
            self.cache[k] = self._arg(graph, k)
        return self.cache[k]


def get_inputs(filename=None):
    graph = {}
    for l in fileinput.input(filename or "inputs.txt"):
        parts = l.strip().split()
        if len(parts) == 3:
            graph[parts[-1]] = ("EQ", parts[0])
        elif len(parts) == 4:
            graph[parts[-1]] = (parts[0], parts[1])
        else:
            graph[parts[-1]] = (parts[1], parts[0], parts[2])
    return graph


def find_key(graph, k, cache):
    if k in cache:
        return cache[k]

    if k.isdigit():
        return int(k)

    instruction = graph[k]
    op = instruction[0]

    if op == "AND":
        value = find_key(graph, instruction[1], cache) & find_key(
            graph, instruction[2], cache
        )
    elif op == "OR":
        value = find_key(graph, instruction[1], cache) | find_key(
            graph, instruction[2], cache
        )
    elif op == "LSHIFT":
        value = find_key(graph, instruction[1], cache) << find_key(
            graph, instruction[2], cache
        )
    elif op == "RSHIFT":
        value = find_key(graph, instruction[1], cache) >> find_key(
            graph, instruction[2], cache
        )
    elif op == "NOT":
        value = ~find_key(graph, instruction[1], cache) & 0xFFFF
    else:
        value = find_key(graph, instruction[1], cache)

    cache[k] = value
    return value


def part_1(filename=None):
    graph = get_inputs(filename)
    return find_key(graph, "a", {})


def part_2(filename=None):
    b = part_1(filename)
    graph = get_inputs(filename)
    return find_key(graph, "a", {"b": b})


if __name__ == "__main__":
    print("Day 07")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
