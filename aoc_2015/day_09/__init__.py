import fileinput
import itertools


def get_inputs(filename=None):
    distances = {}
    for l in fileinput.input(filename or "inputs.txt"):
        parts = l.strip().replace(" to ", " ").replace(" = ", " ").split()
        distances[(parts[0], parts[1])] = int(parts[2])
        distances[(parts[1], parts[0])] = int(parts[2])
    return distances


def get_paths(distances):
    towns = {k[0] for k in distances}
    paths = []
    for path in itertools.permutations(towns):
        d = 0
        it = iter(path)
        b = next(it)
        for i in it:
            a = b
            b = i
            d += distances[(a, b)]
        paths.append(d)
    return paths


def part_1(filename=None):
    distances = get_inputs(filename)
    paths = get_paths(distances)
    return min(paths)


def part_2(filename=None):
    distances = get_inputs(filename)
    paths = get_paths(distances)
    return max(paths)


if __name__ == "__main__":
    print("Day 09")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
