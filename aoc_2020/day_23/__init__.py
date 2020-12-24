def play(start: int, cups: dict[int, int], moves):
    lowest = min(cups.keys())
    highest = max(cups.keys())
    current = start

    for _ in range(moves):
        picked = [cups[current]]
        picked.append(cups[picked[-1]])
        picked.append(cups[picked[-1]])
        cups[current] = cups[picked[-1]]

        destination = current - 1 if current - 1 in cups else highest
        while destination in picked:
            destination -= 1
            if destination < lowest:
                destination = highest
        prev_destination = cups[destination]
        cups[destination] = picked[0]
        cups[picked[-1]] = prev_destination

        current = cups[current]

    return cups


def part_1(cups_str: str, moves=100):
    cups = {int(a): int(b) for a, b in zip(cups_str, cups_str[1:] + cups_str[0])}
    cups = play(int(cups_str[0]), cups, moves)
    next = cups[1]
    result = []
    while next != 1:
        result.append(str(next))
        next = cups[next]

    return int("".join(result))


def part_2(cups_str: str, moves=10000000):
    cups = {int(a): int(b) for a, b in zip(cups_str, cups_str[1:] + cups_str[0])}

    # Add cups until 1 million
    start = int(cups_str[0])
    largest = int(max(cups_str))
    prev = int(cups_str[-1])
    for i in range(largest + 1, 1000001):
        cups[prev] = i
        prev = i
    cups[prev] = start
    assert len(cups) == 1000000

    # Play
    cups = play(start, cups, moves)

    # Result
    a = cups[1]
    b = cups[a]
    return a * b


if __name__ == "__main__":
    print("Day 23")
    print(f"Part 1 Example: {part_1('389125467')}")
    print(f"Part 1: {part_1('487912365')}")
    print(f"Part 2 Example: {part_2('389125467')}")
    print(f"Part 2: {part_2('487912365')}")
