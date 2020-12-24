import fileinput


def get_inputs(filename=None):
    return [int(l.strip()) for l in fileinput.input(filename or "inputs.txt")]


def calc_weakness(numbers, error_pos):
    error_value = numbers[error_pos]


def part_1(filename=None, window=25):
    numbers = get_inputs(filename)
    for i, n in enumerate(numbers[window:]):
        preamble = set(numbers[i : i + window])
        if not any(n - p in preamble for p in preamble):
            return n
    return None


def part_2(filename=None, window=25):
    numbers = get_inputs(filename)
    error = part_1(filename, window)
    head = 0
    tail = 0
    while sum(numbers[head : head + tail + 2]) != error:
        if sum(numbers[head : head + tail + 2]) <= error:
            tail += 1
        else:
            head += 1
            tail = 0
    sum_set = numbers[head : head + tail + 2]
    return min(sum_set) + max(sum_set)


if __name__ == "__main__":
    print("Day 09")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
