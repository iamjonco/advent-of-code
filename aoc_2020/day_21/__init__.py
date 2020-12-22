import fileinput
from collections import namedtuple

Food = namedtuple("Food", ["ingredients", "allergens"])


def get_inputs(filename: str = None):
    fi = fileinput.input(filename or "inputs.txt")

    foods = []
    for line in fi:
        parts = line.split(" (contains ")
        ingredients = parts[0].strip().split()
        allergens = parts[1].replace(")", "").strip().split(", ")
        foods.append(Food(ingredients, allergens))

    fi.close()
    return foods


def map_allergens(foods: list[Food]):
    # Map allergens to ingredients
    # If allergen already in map then only keep ingredients that appear in both
    allergen_map = {}
    for f in foods:
        for a in f.allergens:
            if a in allergen_map:
                allergen_map[a] = allergen_map[a] & set(f.ingredients)
            else:
                allergen_map[a] = set(f.ingredients)

    # Reduce
    while not all(len(v) == 1 for v in allergen_map.values()):
        for a in allergen_map:
            if len(allergen_map[a]) == 1:
                i = allergen_map[a]
                for o in (k for k in allergen_map.keys() if k != a):
                    allergen_map[o].difference_update(i)

    # Flatten
    for a in allergen_map:
        allergen_map[a] = allergen_map[a].pop()

    return allergen_map


def part_1(filename=None):
    foods = get_inputs(filename)
    all_i = [i for f in foods for i in f.ingredients]
    i2a = {v: k for k, v in map_allergens(foods).items()}
    good_i = {i for i in set(all_i) if i not in i2a}
    counts = {i: all_i.count(i) for i in good_i}
    return sum(counts.values())


def part_2(filename=None):
    foods = get_inputs(filename)
    a2i = map_allergens(foods)
    sorted_a = sorted(a2i.keys())
    return ",".join([a2i[a] for a in sorted_a])


if __name__ == "__main__":
    print("Day 21")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
