import fileinput
import math
from collections import namedtuple

Schedule = namedtuple("Schedule", ["start", "buses"])
Bus = namedtuple("Bus", ["b_id", "offset"])


def get_inputs(filename=None):
    fi = fileinput.input(filename or "inputs.txt")
    target = int(next(fi))
    buses = {int(val): idx for idx, val in enumerate(next(fi).split(",")) if val != "x"}
    fi.close()
    return target, buses


def part_1(filename=None):
    target, buses = get_inputs(filename)
    times = {}
    for k in buses.keys():
        q, r = divmod(target, k)
        t = q * k
        if t < target:
            t += k
        times[t] = k
    earliest = min(times.keys())
    return times[earliest] * (earliest - target)


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


def part_2(filename=None):
    target, buses = get_inputs(filename)
    time = 0
    product = math.prod(buses.keys())

    # Use gauss chinese remainder theorem
    for k, v in buses.items():
        p = product // k
        time += (k - v) * inverse_mod(p, k) * p
    return time % product


if __name__ == "__main__":
    print("Day 13")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
