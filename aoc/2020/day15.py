def get_nth(numbers, nth):
    if nth - 1 < len(numbers):
        return numbers[nth - 1]

    turn = len(numbers) + 1
    prev = numbers[-1]
    tracker = {n: [i + 1] for i, n in enumerate(numbers)}

    for i in range(turn, nth + 1):
        spoken = tracker.get(prev)
        if len(spoken) < 2:
            prev = 0
        else:
            prev = spoken[-1] - spoken[-2]

        spoken = tracker.get(prev)
        if spoken is None:
            tracker[prev] = [turn]
        else:
            spoken.append(turn)

        turn += 1

    return prev


if __name__ == "__main__":
    real_input = [0, 6, 1, 7, 2, 19, 20]
    assert get_nth(real_input, 2020) == 706
    assert get_nth(real_input, 30000000) == 19331
