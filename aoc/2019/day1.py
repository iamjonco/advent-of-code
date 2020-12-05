from typing import List

import util


def fuel_for_mass(mass):
    return (mass // 3) - 2


class Module:
    def __init__(self, mass: int):
        self.mass = mass

    def fuel_required(self):
        total_fuel = [fuel_for_mass(self.mass)]
        add_fuel = fuel_for_mass(total_fuel[-1])
        while add_fuel > 0:
            total_fuel.append(add_fuel)
            add_fuel = fuel_for_mass(add_fuel)
        return sum(total_fuel)


def read_inputs(fp: str) -> List[Module]:
    with open(fp) as f:
        return [Module(int(line.strip())) for line in f.readlines()]


if __name__ == "__main__":
    modules: List[Module] = read_inputs(util.get_input_path("day1_1.txt"))
    result = sum([m.fuel_required() for m in modules])
    print(result)
