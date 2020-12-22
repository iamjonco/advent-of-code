import fileinput


def get_inputs(filename=None):
    bags: dict[str, dict[str, int]] = {}
    for l in fileinput.input(filename or "inputs.txt"):
        parts = l.split(" bags contain ")
        children = (
            parts[1]
            .strip()
            .replace(" bags", "")
            .replace(" bag", "")
            .replace(".", "")
            .split(", ")
        )
        if children[0].startswith("no"):
            bags[parts[0]] = {}
            continue
        bags[parts[0]] = {
            c[c.index(" ") + 1 :]: int(c[: c.index(" ")]) for c in children
        }
    return bags


def contains_bag(parent, child, all_bags):
    if child in all_bags[parent]:
        return True
    for k in all_bags[parent].keys():
        if contains_bag(k, child, all_bags):
            return True
    return False


def count_children(parent, all_bags):
    if not len(all_bags[parent]):
        return 0
    count = 0
    for k, v in all_bags[parent].items():
        count += v
        count += v * count_children(k, all_bags)
    return count


def part_1(filename=None):
    bags = get_inputs(filename)
    return sum(1 for b in bags.keys() if contains_bag(b, "shiny gold", bags))


def part_2(filename=None):
    bags = get_inputs(filename)
    return count_children("shiny gold", bags)


if __name__ == "__main__":
    print("Day 07")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
