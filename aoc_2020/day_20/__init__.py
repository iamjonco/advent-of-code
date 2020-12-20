import itertools
import math
import re
from typing import List

import numpy as np


class Tile:
    def __init__(self, tid: int, contents: List[str]):
        self.tid = tid

        # meta with original data
        self.original = contents
        binary = [
            contents[0],
            contents[-1],
            "".join(c[0] for c in contents),
            "".join(c[-1] for c in contents),
        ]
        binary.extend([b[::-1] for b in binary])
        self.all_borders = {b: int(b, 2) for b in binary}
        self.unique_borders = set()

        # contents
        self.contents = np.array([[c for c in l] for l in contents])

        # orientation tracker
        self._ori_tracker = itertools.cycle(list(range(12)))
        self.ori = next(self._ori_tracker)

    @property
    def image(self):
        return ["".join(c for c in r) for r in self.contents]

    @property
    def borders(self):
        return [
            "".join(self.contents[0, :]),
            "".join(self.contents[:, -1]),
            "".join(self.contents[-1, :]),
            "".join(self.contents[:, 0]),
        ]

    def flip_x(self):
        self.contents = np.fliplr(self.contents)

    def flip_y(self):
        self.contents = np.flipud(self.contents)

    def rotate_acw(self):
        self.contents = np.rot90(self.contents)

    def cycle(self):
        self.ori = next(self._ori_tracker)
        self.rotate_acw()

        if self.ori == 0:
            self.flip_x()

        elif self.ori == 4:
            self.flip_y()

        elif self.ori == 8:
            self.flip_y()
            self.flip_x()

    def __str__(self):
        return f"{self.tid!r}"

    def __repr__(self):
        return f"{self.tid!r}"


_BINARY_TRANS = str.maketrans(".#", "01")  # convert to binary


def get_inputs(filepath=None) -> dict[int, Tile]:
    with open(filepath or "inputs.txt") as f:
        parts = [l.strip().split("\n") for l in f.read().split("\n\n")]

    tiles = {}
    for p in parts:
        tid = int(p[0][5:-1])
        contents = [l.translate(_BINARY_TRANS) for l in p[1:]]
        tiles[tid] = Tile(tid, contents)

    return tiles


def verify_gird(grid):
    return math.prod(
        t.tid for t in [grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]]
    )


def get_groups(tiles):
    border_freqs: dict[str, list[Tile]] = {}
    for t in tiles.values():
        for b in t.all_borders:
            border_freqs[b] = border_freqs.get(b, []) + [t]

    corners = set()
    edges = set()
    inner = set()

    unique_borders = {k for k, v in border_freqs.items() if len(v) == 1}
    for t in tiles.values():
        t.unique_borders = {b for b in t.all_borders if b in unique_borders}
        if len(t.unique_borders) == 4:
            corners.add(t)
        elif len(t.unique_borders) == 2:
            edges.add(t)
        else:
            inner.add(t)

    assert len(set.intersection(corners, edges, inner)) == 0
    assert len(corners) == 4
    assert len(edges) == (int(math.sqrt(len(tiles))) - 2) * 4
    assert len(inner) == len(tiles) - len(corners) - len(edges)

    return border_freqs, corners, edges, inner


def fit(tile: Tile, sides: list[set]):
    original = tile.ori
    for i in range(0, 12):
        if all(b in sides[s] for s, b in enumerate(tile.borders) if len(sides[s]) > 0):
            return True
        tile.cycle()
    assert tile.ori == original
    return False


def build_grid(tiles):
    grid_size = int(math.sqrt(len(tiles)))
    max_idx = grid_size - 1
    border_freqs, corners, edges, inner = get_groups(tiles)
    grid = np.empty((grid_size, grid_size), np.object)

    for i in range(0, grid.shape[0]):
        for j in range(0, grid.shape[1]):
            tile = None
            unique_sides = [i == 0, j == max_idx, i == max_idx, j == 0]

            if unique_sides.count(True) == 2:
                pieces = corners
            elif unique_sides.count(True) == 1:
                pieces = edges
            else:
                pieces = inner

            for t in pieces:
                if any(unique_sides):
                    sides = [t.unique_borders if x else [] for x in unique_sides]
                else:
                    sides = [[], [], [], []]

                if i - 1 >= 0:
                    sides[0] = {grid[i - 1][j].borders[2]}
                if j - 1 >= 0:
                    sides[3] = {grid[i][j - 1].borders[1]}

                result = fit(t, sides)
                if result:
                    tile = t
                    break

            # Add to grid
            grid[i][j] = tile
            pieces.remove(tile)

    assert len(corners) == 0
    assert len(edges) == 0
    assert len(inner) == 0

    return grid


def make_regex(s):
    chars = [s[0]]
    counts = [0]
    for c in s:
        if c != chars[-1]:
            chars.append(c)
            counts.append(0)
        counts[-1] += 1
    return "".join(f"{a}{{{b}}}" for a, b in zip(chars, counts)).replace(" ", "[01]")


def part_1(filename=None):
    tiles = get_inputs(filename)
    grid = build_grid(tiles)
    return verify_gird(grid)


def part_2(filename=None):
    tiles = get_inputs(filename)
    grid = build_grid(tiles)

    # Monster
    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    monster = [l.replace("#", "1") for l in monster]

    # Build the image
    t_shape = grid[0][0].contents.shape
    g_shape = grid.shape

    image_contents = []
    for gi in range(0, g_shape[0]):
        for ti in range(1, t_shape[0] - 1):
            s = ""
            for gj in range(0, g_shape[1]):
                s += "".join(grid[gi][gj].contents[ti, 1 : t_shape[1] - 1])
            image_contents.append(s)
    image_tile = Tile(0, image_contents)

    # Look for the monster - rotate if not found
    m0 = re.compile(make_regex(monster[0]))
    m1 = re.compile(make_regex(monster[1]))
    m2 = re.compile(make_regex(monster[2]))

    found = 0
    image = image_tile.image
    for _ in range(12):
        for r in range(len(image) - 2):
            for i in range(len(image[r])):
                a = m0.match(image[r], i)
                b = m1.match(image[r + 1], i)
                c = m2.match(image[r + 2], i)
                if a and b and c:
                    found += 1
        if found > 0:
            break
        image_tile.cycle()
        image = image_tile.image

    monster_filled = "".join(monster).count("1")
    image_filled = "".join(image).count("1")

    return image_filled - (found * monster_filled)


if __name__ == "__main__":
    print("Day 20")
    print(f"Part 1: {part_1('example.txt')}")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2('example.txt')}")
    print(f"Part 2: {part_2()}")
