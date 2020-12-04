import re
from typing import List

import util

_HGT_PATTERN = re.compile(r"^([\d]+)(cm|in)$")
_HCL_PATTERN = re.compile(r"^#[0-9a-f]{6}$")
_PID_PATTERN = re.compile(r"^[0-9]{9}$")
_ECL_VALID = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class Passport:
    def __init__(
        self,
        byr=None,
        iyr=None,
        eyr=None,
        hgt=None,
        hcl=None,
        ecl=None,
        pid=None,
        cid=None,
    ):
        self.byr = byr
        """Birth Year"""
        self.iyr = iyr
        """Issue Year"""
        self.eyr = eyr
        """Expiry Year"""
        self.hgt = hgt
        """Height in cm or in"""
        self.hcl = hcl
        """Hair Color - hex code"""
        self.ecl = ecl
        """Eye color"""
        self.pid = pid
        """Passport ID"""
        self.cid = cid
        """Country ID - optional"""

    def __str__(self):
        return str(self.__dict__)

    def is_byr_valid(self):
        """
        :return: birth year is between 1920-2002 inclusive
        """
        if self.byr is None:
            return False
        return int(self.byr) in range(1920, 2003)

    def is_iyr_valid(self):
        """
        :return: issue year is between 2010-2020 inclusive
        """
        if self.iyr is None:
            return False
        return int(self.iyr) in range(2010, 2021)

    def is_eyr_valid(self):
        """
        :return: expiry year is between 2020-2030 inclusive
        """
        if self.eyr is None:
            return False
        return int(self.eyr) in range(2020, 2031)

    def is_hgt_valid(self):
        """
        :return: height is between 150-193cm or 59-76in inclusive
        """
        if self.hgt is None:
            return False

        match = _HGT_PATTERN.match(self.hgt)
        if not match:
            return False

        value, units = match.groups()
        value = int(value)

        if units == "cm":
            return value in range(150, 194)
        elif units == "in":
            return value in range(59, 77)

        print("Here")
        return False

    def is_hcl_valid(self):
        """
        :return: hair color is a valid hex code
        """
        if self.hcl is None:
            return False
        return _HCL_PATTERN.match(self.hcl)

    def is_ecl_valid(self):
        """
        :return: eye color is exactly one of: amb blu brn gry grn hzl oth
        """
        if self.ecl is None:
            return False
        return self.ecl in _ECL_VALID

    def is_pid_valid(self):
        """
        :return: password ID is a 9 digit number including leading zero
        """
        if self.pid is None:
            return False
        if self.pid == "7243957480":
            print(self.pid)
        return _PID_PATTERN.match(self.pid)

    def is_cid_valid(self):
        return True

    def is_valid(self) -> bool:
        return (
            self.is_byr_valid()
            and self.is_iyr_valid()
            and self.is_eyr_valid()
            and self.is_hgt_valid()
            and self.is_hcl_valid()
            and self.is_ecl_valid()
            and self.is_pid_valid()
            and self.is_cid_valid()
        )


def read_inputs(fp: str) -> List[Passport]:
    with open(fp) as f:
        lines = f.readlines()

    dicts = [{}]
    current = dicts[0]
    for line in lines:
        line = line.strip()
        # New passport started
        if len(line) == 0:
            current = {}
            dicts.append(current)
            continue

        parts = line.split()
        for part in parts:
            p = part.split(":")
            current[p[0]] = p[1]

    return [Passport(**kwargs) for kwargs in dicts]


if __name__ == "__main__":
    inputs: List[Passport] = read_inputs(util.get_input_path("day4_1.txt"))
    valid = list(filter(lambda p: p.is_valid(), inputs))
    print(len(valid))
