import fileinput


def get_inputs(filename=None):
    with fileinput.input(filename or "inputs.txt") as fi:
        return next(fi).strip()


def move(x: int, y: int, d: str):
    if d == "^":
        y += 1
    elif d == "v":
        y -= 1
    elif d == ">":
        x += 1
    elif d == "<":
        x -= 1
    return x, y


def part_1(filename=None):
    dirs = get_inputs(filename)
    x = 0
    y = 0
    visited = {(x, y)}
    for d in dirs:
        x, y = move(x, y, d)
        visited.add((x, y))
    return len(visited)


def part_2(filename=None):
    dirs = get_inputs(filename)
    sx, sy = 0, 0
    rx, ry = 0, 0
    visited = {(0, 0)}
    santa = True
    for d in dirs:
        if santa:
            sx, sy = move(sx, sy, d)
            visited.add((sx, sy))
        else:
            rx, ry = move(rx, ry, d)
            visited.add((rx, ry))
        santa = not santa
    return len(visited)


if __name__ == "__main__":
    print("Day 03")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
