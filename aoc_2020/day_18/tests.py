from aoc_2020.day_18 import part_1, part_2, evaluate, evaluate_2


def test_evaluate():
    assert evaluate("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert evaluate("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert evaluate("2 * 3 + (4 * 5)") == 26
    assert evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632


def test_evaluate_2():
    assert evaluate_2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert evaluate_2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert evaluate_2("2 * 3 + (4 * 5)") == 46
    assert evaluate_2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert evaluate_2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert evaluate_2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def test_part_1():
    assert part_1() == 654686398176


def test_part_2():
    assert part_2() == 8952864356993
