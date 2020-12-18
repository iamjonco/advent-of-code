import fileinput
import math


def get_inputs(filepath=None) -> list[str]:
    return [x.strip() for x in fileinput.input(filepath or "inputs.txt")]


def tree_count(grid: list[str], dx: int, dy: int):
    x_max = len(grid[0])
    x = dx
    y = dy
    trees = 0

    while y < len(grid):
        if grid[y][x % x_max] == "#":
            trees += 1
        x += dx
        y += dy

    return trees


def part_1(filepath=None):
    return tree_count(get_inputs(filepath), 3, 1)


def part_2(filepath=None):
    grid = get_inputs(filepath)
    return math.prod(
        [
            tree_count(grid, 1, 1),
            tree_count(grid, 3, 1),
            tree_count(grid, 5, 1),
            tree_count(grid, 7, 1),
            tree_count(grid, 1, 2),
        ]
    )


if __name__ == "__main__":
    print("Day 3")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
