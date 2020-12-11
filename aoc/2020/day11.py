import util


def get_inputs(filepath):
    with open(util.get_input_path(filepath)) as f:
        return [s.strip() for s in f.readlines()]


def in_range(r, c, grid: list[str]):
    return r not in range(0, len(grid)) or c not in range(0, len(grid[0]))


def value_at(r, c, grid: list[str]):
    if r not in range(0, len(grid)) or c not in range(0, len(grid[0])):
        return None
    return grid[r][c]


def value_in_dir(r, c, r_inc, c_inc, grid: list[str]):
    val = value_at(r + r_inc, c + c_inc, grid)
    while val == ".":
        val = value_at(r + r_inc, c + c_inc, grid)
        r += r_inc
        c += c_inc
    return val


def count_adj_in_dir(r, c, grid: list[str]):
    a = [
        value_in_dir(r, c, -1, 0, grid),
        value_in_dir(r, c, -1, 1, grid),
        value_in_dir(r, c, 0, 1, grid),
        value_in_dir(r, c, 1, 1, grid),
        value_in_dir(r, c, 1, 0, grid),
        value_in_dir(r, c, 1, -1, grid),
        value_in_dir(r, c, 0, -1, grid),
        value_in_dir(r, c, -1, -1, grid),
    ]
    return a.count("#")


def count_adj(r, c, grid: list[str]):
    if grid[r][c] == ".":
        return None

    # start at N and go clockwise
    return [
        value_at(r - 1, c, grid),
        value_at(r - 1, c + 1, grid),
        value_at(r, c + 1, grid),
        value_at(r + 1, c + 1, grid),
        value_at(r + 1, c, grid),
        value_at(r + 1, c - 1, grid),
        value_at(r, c - 1, grid),
        value_at(r - 1, c - 1, grid),
    ].count("#")


def next_value(val, adj, adj_limit):
    if val == ".":
        return "."
    if val == "L" and adj == 0:
        return "#"
    if val == "#" and adj > adj_limit:
        return "L"
    return val


def next_grid(grid: list[str], long_dir=False, adj_limit=3):
    new_grid = []
    for r in range(0, len(grid)):
        row = []
        for c in range(0, len(grid[0])):
            val = value_at(r, c, grid) or "."
            adj = count_adj_in_dir(r, c, grid) if long_dir else count_adj(r, c, grid)
            row.append(next_value(val, adj, adj_limit))
        new_grid.append("".join(row))
    return new_grid


def occupied_seats(grid: list[str]):
    return "".join(grid).count("#")


def part_1():
    start = get_inputs("day11_1.txt")
    grids = [start, next_grid(start)]

    while grids[-2] != grids[-1]:
        grids.append(next_grid(grids[-1]))

    assert occupied_seats(grids[-1]) == 2277


def part_2():
    start = get_inputs("day11_1.txt")
    grids = [start, next_grid(start, long_dir=True, adj_limit=4)]

    while grids[-2] != grids[-1]:
        grids.append(next_grid(grids[-1], long_dir=True, adj_limit=4))

    assert occupied_seats(grids[-1]) == 2066


if __name__ == "__main__":
    part_1()
    part_2()
