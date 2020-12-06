import itertools

PW_MIN = 254032
PW_MAX = 789860


class Password:
    def __init__(self, contents):
        self.contents = (
            [int(i) for i in str(contents)] if isinstance(contents, int) else contents
        )

    def is_valid(self, adj_doubles=True):
        doubles = set()
        for i in range(0, len(self.contents) - 1):
            a = self.contents[i]
            b = self.contents[i + 1]
            if a > b:
                return False
            if a == b:
                doubles.add((i, i + 1))

        bad_doubles = set()
        if adj_doubles:
            for i, j in doubles:
                value = self.contents[i]
                if (i - 1) in range(0, len(self.contents)) and value == self.contents[
                    i - 1
                ]:
                    bad_doubles.add((i, j))
                elif (j + 1) in range(0, len(self.contents)) and value == self.contents[
                    j + 1
                ]:
                    bad_doubles.add((i, j))

        return len(doubles - bad_doubles) > 0


def part_1():
    count = 0
    for pw in range(PW_MIN, PW_MAX):
        if Password(pw).is_valid(False):
            count += 1
    assert count == 1033


def part_2():
    count = 0
    for pw in range(PW_MIN, PW_MAX):
        if Password(pw).is_valid():
            count += 1
    print(count)
    # assert count == 1033


if __name__ == "__main__":
    part_1()
    part_2()
    # print(Password(788866).is_valid)
