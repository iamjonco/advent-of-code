def get_nth(numbers, nth):
    if nth - 1 < len(numbers):
        return numbers[nth - 1]

    prev = numbers[-1]
    last_spoken = {n: i + 1 for i, n in enumerate(numbers)}
    for t in range(len(numbers), nth):
        next = t - last_spoken.get(prev, t)
        last_spoken[prev] = t
        prev = next

    return prev


if __name__ == "__main__":
    real_input = [0, 6, 1, 7, 2, 19, 20]
    assert get_nth(real_input, 2020) == 706
    assert get_nth(real_input, 30000000) == 19331
