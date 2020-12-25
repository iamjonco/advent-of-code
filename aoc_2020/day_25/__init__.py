import fileinput


def get_inputs(filename=None):
    return [int(l.strip()) for l in fileinput.input(filename or "inputs.txt")]


def transform(subject: int, loop: int):
    value = 1
    for x in range(loop):
        value = value * subject
        value = value % 20201227
    return value


def do_transform(subject, value=1):
    return (value * subject) % 20201227


def calc_loop_size(key: int):
    value = 1
    loops = 0
    while value != key:
        value = do_transform(7, value)
        loops += 1
    return loops


def part_1(filename=None):
    key_a, key_b = get_inputs(filename)
    loop_a = calc_loop_size(key_a)
    enc_key = 1
    for _ in range(loop_a):
        enc_key = do_transform(key_b, enc_key)
    return enc_key


if __name__ == "__main__":
    print("Day 25")
    print(f"Part 1: {part_1()}")
