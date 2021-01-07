import hashlib

secret_key = "bgvyzdsv"


def calc_number(hash_start):
    i = 0
    md5_hash = ""
    while not md5_hash.startswith(hash_start):
        i += 1
        md5_hash = hashlib.md5(f"{secret_key}{i}".encode("utf-8")).hexdigest()
    return i


def part_1(filename=None):
    return calc_number("00000")


def part_2(filename=None):
    return calc_number("000000")


if __name__ == "__main__":
    print("Day 04")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
