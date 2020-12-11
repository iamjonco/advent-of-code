import util


def detect_error(numbers, window: int):
    if isinstance(numbers, str):
        with open(util.get_input_path(numbers)) as f:
            numbers = [int(f.strip()) for f in f.readlines()]

    for idx, n in enumerate(numbers[window:]):
        preamble = set(numbers[idx : idx + window])
        if not any(n - i in preamble for i in preamble):
            return n, idx + window
    return None, None


def calc_weakness(numbers, error_pos):
    if isinstance(numbers, str):
        with open(util.get_input_path(numbers)) as f:
            numbers = [int(f.strip()) for f in f.readlines()]

    error_value = numbers[error_pos]
    head = 0
    tail = 0
    while sum(numbers[head : head + tail + 2]) != error_value:
        if sum(numbers[head : head + tail + 2]) <= error_value:
            tail += 1
        else:
            head += 1
            tail = 0

    window = numbers[head : head + tail + 2]
    return min(window) + max(window)


def example_1():
    error_value, error_pos = detect_error("day9_2.txt", 5)
    assert error_value == 127


def part_1():
    error_value, error_pos = detect_error("day9_1.txt", 26)
    assert error_value == 26134589


def part_2():
    error_value, error_pos = detect_error("day9_1.txt", 26)
    weakness = calc_weakness("day9_1.txt", error_pos)
    assert 3535124 == weakness


if __name__ == "__main__":
    example_1()
    part_1()
    part_2()
