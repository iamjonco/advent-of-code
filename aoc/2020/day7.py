import re
from typing import Dict

import util

BAG_PATTERN = re.compile(
    r"(?P<count>[\d]*)(?:[\s]?)(?P<color>[\D]+\s[\D]+) (?:bags|bag)"
)
SHINY_GOLD = "shiny gold"


class Bag:
    def __init__(self, color: str):
        self.color = color
        self.parents = {}
        self.children = {}

    @property
    def all_parents(self) -> set:
        bags = set(self.parents.values())
        for p in self.parents.values():
            bags.update(p.all_parents)
        return bags

    @property
    def all_children_count(self):
        return sum(
            [
                count + (bag.all_children_count * count)
                for bag, count in self.children.values()
            ]
        )

    def __hash__(self):
        return hash(self.color)

    def __repr__(self):
        return f"{type(self).__name__}(color={self.color!r})>"


def get_bag_attrs(s):
    groups = BAG_PATTERN.match(s).groupdict()
    return groups["color"], None if groups["count"] == "" else int(groups["count"])


def create_bags(filepath) -> Dict[str, Bag]:
    with open(filepath) as f:
        bags = {}
        for line in f.readlines():
            color, children = line.strip().strip(".").split("contain")

            # Process main bag
            parent_color, _ = get_bag_attrs(color)
            parent_bag = bags.get(parent_color, Bag(parent_color))
            if parent_color not in bags:
                bags[parent_color] = parent_bag

            # Process children
            if "no other bags" == children.strip():
                continue

            children = map(lambda s: s.strip(), children.split(","))
            for child in children:
                child_color, count = get_bag_attrs(child)
                child_bag = bags.get(child_color, Bag(child_color))
                if child_color not in bags:
                    bags[child_color] = child_bag
                child_bag.parents[parent_color] = parent_bag
                parent_bag.children[child_color] = (child_bag, count)

        return bags


def example_1():
    all_bags = create_bags(util.get_input_path("day7_2.txt"))
    my_bag = all_bags.get(SHINY_GOLD)
    assert len(my_bag.all_parents) == 4


def example_2():
    all_bags = create_bags(util.get_input_path("day7_2.txt"))
    my_bag = all_bags.get(SHINY_GOLD)
    assert my_bag.all_children_count == 32


def part_1():
    all_bags = create_bags(util.get_input_path("day7_1.txt"))
    my_bag = all_bags.get(SHINY_GOLD)
    assert len(my_bag.all_parents) == 278


def part_2():
    all_bags = create_bags(util.get_input_path("day7_1.txt"))
    my_bag = all_bags.get(SHINY_GOLD)
    assert my_bag.all_children_count == 45157


if __name__ == "__main__":
    part_1()
    part_2()
