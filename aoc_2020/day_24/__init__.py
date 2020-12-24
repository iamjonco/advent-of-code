import fileinput

moves = {
    "e": [1, -1, 0],
    "ne": [1, 0, -1],
    "nw": [0, 1, -1],
    "w": [-1, 1, 0],
    "sw": [-1, 0, 1],
    "se": [0, -1, 1],
}


def get_inputs(filename=None):
    instructions = []
    for l in fileinput.input(filename or "inputs.txt"):
        current = []
        it = iter(l.strip())
        for c in it:
            if c in "ns":
                current.append(c + next(it))
            else:
                current.append(c)
        instructions.append(current)
    return instructions


def process_instructions(instructions: list[list[str]]):
    tiles = set()
    for i in instructions:
        coord = [0, 0, 0]
        for op in i:
            coord = [a + b for a, b in zip(coord, moves[op])]
        coord = tuple(coord)
        if coord in tiles:
            tiles.remove(coord)
        else:
            tiles.add(coord)
    return tiles


def get_neighbours(tile: tuple[int, int, int]):
    return {(tile[0] + v[0], tile[1] + v[1], tile[2] + v[2]) for v in moves.values()}


def part_1(filename=None):
    instructions = get_inputs(filename)
    tiles = process_instructions(instructions)
    return len(tiles)


def part_2(filename=None):
    instructions = get_inputs(filename)
    tiles = process_instructions(instructions)

    for day in range(100):
        new_tiles = {
            t
            for t in tiles
            if len(get_neighbours(t).intersection(tiles)) in range(1, 3)
        }
        to_check = (n for t in tiles for n in get_neighbours(t) if n not in tiles)
        for t in to_check:
            if len(get_neighbours(t).intersection(tiles)) == 2:
                new_tiles.add(t)
        tiles = new_tiles

    return len(tiles)


if __name__ == "__main__":
    print("Day 24")
    print(f"Part 1 Example: {part_1('example.txt')}")
    print(f"Part 1: {part_1('inputs.txt')}")
    print(f"Part 2 Example: {part_2('example.txt')}")
    print(f"Part 2: {part_2('inputs.txt')}")
