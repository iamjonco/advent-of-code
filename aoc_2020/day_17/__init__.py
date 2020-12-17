import fileinput
import itertools

_ACTIVE = "#"
_INACTIVE = "."


def get_inputs(filename=None) -> list[list[str]]:
    return [[l.strip() for l in fileinput.input(filename or "inputs.txt")]]


def print_grid(grid):
    for z, cube in enumerate(grid):
        print(f"z={z}")
        for row in cube:
            print(row)
        print("\n")


def get_value(x, y, z, w, grid):
    if (
        x in range(0, len(grid[0][0][0]))
        and y in range(0, len(grid[0][0]))
        and z in range(0, len(grid[0]))
        and w in range(0, len(grid))
    ):
        return grid[w][z][y][x]
    return _INACTIVE


def count_active(grid):
    return "".join([y for w in grid for z in w for y in z]).count(_ACTIVE)


def count_active_neighbours(x, y, z, w, grid):
    neighbours = []

    for w0 in range(w - 1, w + 2):
        for z0 in range(z - 1, z + 2):
            for y0 in range(y - 1, y + 2):
                for x0 in range(x - 1, x + 2):
                    if x0 == x and y0 == y and z0 == z and w0 == w:
                        continue
                    neighbours.append(get_value(x0, y0, z0, w0, grid))
    return neighbours.count(_ACTIVE)


def cycle(grid, hypercube=False):
    grid0 = []
    dw = range(-1, len(grid) + 1) if hypercube else range(0, 1)
    for w in dw:
        w0 = []
        for z in range(-1, len(grid[0]) + 1):  # z
            z0 = []
            for y in range(-1, len(grid[0][0]) + 1):  # y
                y0 = ""
                for x in range(-1, len(grid[0][0][0]) + 1):  # x
                    active = count_active_neighbours(x, y, z, w, grid)
                    current = get_value(x, y, z, w, grid)
                    if current == _ACTIVE and active in range(2, 4):
                        y0 += _ACTIVE
                    elif current == _INACTIVE and active == 3:
                        y0 += _ACTIVE
                    else:
                        y0 += _INACTIVE
                z0.append(y0)
            w0.append(z0)
        grid0.append(w0)
    return grid0


def part_1(filename=None) -> int:
    grid = get_inputs(filename)
    for i in range(0, 6):
        grid = cycle(grid)
    return count_active(grid)


def part_2(filename=None) -> int:
    grid = get_inputs(filename)
    for i in range(0, 6):
        grid = cycle(grid, hypercube=True)
    return count_active(grid)


if __name__ == "__main__":
    print("Day 17")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
