def get_inputs(numbers=None):
    return numbers or [0, 6, 1, 7, 2, 19, 20]


def get_nth(numbers, nth):
    if nth - 1 < len(numbers):
        return numbers[nth - 1]

    prev = numbers[-1]
    last_spoken = {n: i + 1 for i, n in enumerate(numbers)}
    for t in range(len(numbers), nth):
        next = t - last_spoken.get(prev, t)
        last_spoken[prev] = t
        prev = next

    return prev


def part_1(numbers=None):
    return get_nth(get_inputs(numbers), 2020)


def part_2(numbers=None):
    return get_nth(get_inputs(numbers), 30000000)


if __name__ == "__main__":
    print("Day 15")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
