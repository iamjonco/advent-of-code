import math
from collections import namedtuple

import util

Schedule = namedtuple("Schedule", ["start", "buses"])
Bus = namedtuple("Bus", ["b_id", "offset"])


def get_inputs(filepath=None):
    if filepath:
        with open(util.get_input_path(filepath)) as f:
            lines = [s.strip() for s in f.readlines()]
    # Example input
    else:
        lines = ["939", "7,13,x,x,59,x,31,19"]

    start = int(lines[0])
    buses = []
    for idx, val in enumerate(lines[1].split(",")):
        if val != "x":
            buses.append(Bus(int(val), idx))

    return Schedule(start, buses)


def calc_nearest(target, b_id):
    q, r = divmod(target, b_id)
    t = q * b_id
    if t < target:
        t += b_id
    return t


def calc_times(target: int, buses: list[Bus]):
    return {calc_nearest(target, bus.b_id): bus for bus in buses}


def part_1(schedule):
    times = calc_times(schedule.start, schedule.buses)
    earliest = min(times.keys())
    return times[earliest].b_id * (earliest - schedule.start)


def inverse_mod(a, b):
    if b == 1:
        return 1

    x = b  # save for later
    # Recursive Extended Euclid algorithm to find coefficient of a
    a0, a1, b0, b1 = 1, 0, 0, 1
    while b > 0:
        q, a, b = math.floor(a / b), b, a % b
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    # q = GCD, a0 = coefficient of a, b0 = coefficient of b
    return a0 % x


def part_2(schedule):
    time = 0
    product = math.prod([b.b_id for b in schedule.buses])

    # Use gauss chinese remainder theorem
    for bus in schedule.buses:
        p = product // bus.b_id
        time += (bus.b_id - bus.offset) * inverse_mod(p, bus.b_id) * p
    return time % product


if __name__ == "__main__":
    example_input = get_inputs()
    real_input = get_inputs("day13_1.txt")
    assert part_1(example_input) == 295
    assert part_1(real_input) == 261
    assert part_2(example_input) == 1068781
    assert part_2(real_input) == 807435693182510
