import fileinput


def get_inputs(filename=None):
    return (l.strip() for l in fileinput.input(filename or "inputs.txt"))


def sanitise(s):
    _s = []
    it = iter(s[1:-1])
    for c in it:
        if c == "\\":
            n = next(it)
            if n == "\\":
                _s.append("\\")
            elif n == '"':
                _s.append('"')
            else:
                _s.append(chr(int(next(it) + next(it), 16)))
        else:
            _s.append(c)
    return "".join(_s)


def part_1(filename=None):
    strings = get_inputs(filename)
    memory = 0
    actual = 0
    for s in strings:
        memory += 2
        it = iter(s[1:-1])
        for c in it:
            if c == "\\":
                n = next(it)
                memory += 1
                if n == "x":
                    next(it)
                    next(it)
                    memory += 2
            memory += 1
            actual += 1
    return memory - actual


def part_2(filename=None):
    strings = get_inputs(filename)
    count = 0
    for s in strings:
        n = s.replace("\\", "\\\\").replace('"', '\\"')
        count += len(n) - len(s) + 2
    return count


if __name__ == "__main__":
    print("Day 08")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
