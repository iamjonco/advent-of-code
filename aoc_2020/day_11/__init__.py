import fileinput
import operator

_dirs = {
    "n": [0, 1],
    "ne": [1, 1],
    "e": [1, 0],
    "se": [1, -1],
    "s": [0, -1],
    "sw": [-1, -1],
    "w": [-1, 0],
    "nw": [-1, 1],
}


def get_inputs(filepath=None):
    grid = {}
    for y, l in enumerate(fileinput.input(filepath or "inputs.txt")):
        for x, c in enumerate(l.strip()):
            if c != ".":
                grid[(x, y)] = c
    return grid


def immediate_adj(
    coord: tuple[int, int], grid: dict[tuple[int, int], str], xm=None, ym=None
):
    adj = 0
    for c in ((coord[0] + d[0], coord[1] + d[1]) for d in _dirs.values()):
        adj += 1 if grid.get(c) == "#" else 0
    return adj


def infinite_adj(coord: tuple[int, int], grid: dict[tuple[int, int], str], xm, ym):
    adj = 0
    for d in _dirs.values():
        x, y = coord
        while x in range(xm) and y in range(ym):
            x += d[0]
            y += d[1]
            if (x, y) in grid:
                adj += 1 if grid.get((x, y)) == "#" else 0
                break
    return adj


def count_occupied(grid: dict[tuple[int, int], str]):
    return "".join(r for r in grid.values()).count("#")


def calc_final_grid(grid: dict[tuple[int, int], str], adj_limit, adj_func):
    xm = max(grid.keys(), key=operator.itemgetter(0))[0] + 1
    ym = max(grid.keys(), key=operator.itemgetter(1))[1] + 1
    prev_grid = None
    while grid != prev_grid:
        prev_grid = grid
        grid = {}
        for coord, v in prev_grid.items():
            adj = adj_func(coord, prev_grid, xm, ym)
            if v == "L" and adj == 0:
                grid[coord] = "#"
            elif v == "#" and adj >= adj_limit:
                grid[coord] = "L"
            else:
                grid[coord] = v
    return prev_grid


def part_1(filename=None):
    grid = get_inputs(filename)
    final_grid = calc_final_grid(grid, 4, immediate_adj)
    return count_occupied(final_grid)


def part_2(filename=None):
    grid = get_inputs(filename)
    final_grid = calc_final_grid(grid, 5, infinite_adj)
    return count_occupied(final_grid)


if __name__ == "__main__":
    print("Day 11")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
