def get_inputs(filename=None):
    with open(filename or "inputs.txt") as f:
        parts = [l.strip().split("\n") for l in f.read().split("\n\n")]

    return [int(p) for p in parts[0][1:]], [int(p) for p in parts[1][1:]]


def is_finished(a, b):
    return len(a) * len(b) == 0


def calc_score(deck: list[int]):
    return sum((i + 1) * v for i, v in enumerate(reversed(deck)))


def play_recursive_round(a_deck, b_deck):
    prev = set()
    while not is_finished(a_deck, b_deck):
        scores = (calc_score(a_deck), calc_score(b_deck))
        if scores in prev:
            return [1], []
        prev.add(scores)

        a = a_deck.pop(0)
        b = b_deck.pop(0)

        if len(a_deck) >= a and len(b_deck) >= b:
            sub_a = a_deck[:a]
            sub_b = b_deck[:b]
            res_a, res_b = play_recursive_round(sub_a, sub_b)
            a_wins = len(res_a) > len(res_b)
        else:
            a_wins = a > b

        if a_wins:
            a_deck.append(a)
            a_deck.append(b)
        else:
            b_deck.append(b)
            b_deck.append(a)

    return a_deck, b_deck


def part_1(filename=None):
    a_deck, b_deck = get_inputs(filename)
    while not is_finished(a_deck, b_deck):
        a = a_deck.pop(0)
        b = b_deck.pop(0)
        if a > b:
            a_deck.append(a)
            a_deck.append(b)
        else:
            b_deck.append(b)
            b_deck.append(a)
    return calc_score(a_deck if len(a_deck) > 0 else b_deck)


def part_2(filename=None):
    a_deck, b_deck = get_inputs(filename)
    play_recursive_round(a_deck, b_deck)
    return calc_score(a_deck if len(a_deck) > 0 else b_deck)


if __name__ == "__main__":
    print("Day 22")
    print(f"Part 1 Example: {part_1('example.txt')}")
    print(f"Part 1: {part_1('inputs.txt')}")
    print(f"Part 2 Example: {part_2('example.txt')}")
    print(f"Part 2: {part_2('inputs.txt')}")
