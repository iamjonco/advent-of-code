import fileinput
import re

_REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
_HGT_PATTERN = re.compile(r"^([\d]+)(cm|in)$")
_HCL_PATTERN = re.compile(r"^#[0-9a-f]{6}$")
_PID_PATTERN = re.compile(r"^[0-9]{9}$")
_ECL_VALID = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def get_inputs(filepath=None) -> list[dict[str, str]]:
    lines = (l.strip() for l in fileinput.input(filepath or "inputs.txt"))
    buffer = [""]
    for l in lines:
        if len(l):
            buffer[-1] += l + " "
        else:
            buffer.append("")

    return [
        {k: v for k, v in [x.split(":") for x in s.strip().split(" ")]} for s in buffer
    ]


def get_complete(passport: dict[str, str]):
    return all(k in passport for k in _REQUIRED_KEYS)


def is_valid(passport: dict[str, str]):
    if not get_complete(passport):
        return False

    def is_hgt_valid():
        match = _HGT_PATTERN.match(passport["hgt"])
        if not match:
            return False

        value, units = match.groups()
        value = int(value)

        if units == "cm":
            return value in range(150, 194)
        elif units == "in":
            return value in range(59, 77)

    return (
        int(passport["byr"]) in range(1920, 2003)  # byr
        and int(passport["iyr"]) in range(2010, 2021)  # iyr
        and int(passport["eyr"]) in range(2020, 2031)  # eyr
        and is_hgt_valid()  # hgt
        and _HCL_PATTERN.match(passport["hcl"])  # hcl
        and passport["ecl"] in _ECL_VALID  # ecl
        and _PID_PATTERN.match(passport["pid"])  # pid
    )


def part_1(filepath=None):
    return len([p for p in get_inputs(filepath) if get_complete(p)])


def part_2(filepath=None):
    return len([p for p in get_inputs(filepath) if is_valid(p)])


if __name__ == "__main__":
    print("Day 4")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
