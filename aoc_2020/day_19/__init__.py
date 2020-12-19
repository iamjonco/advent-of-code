import fileinput
import lark

_INTS = "".join(str(i) for i in range(0, 10))
_CHARS = "".join(chr(i + 97) for i in range(0, 10))


def get_inputs(filepath=None):
    parts = "".join([s for s in fileinput.input(filepath or "inputs.txt")]).split(
        "\n\n"
    )

    # Leave BNF rules as single string
    # Lark parser doesn't like numbers as rule names, convert to text
    rules = fix_production_rule(parts[0])
    return rules, [l.strip() for l in parts[1].split("\n")]


def fix_production_rule(rule: str):
    return rule.translate(str.maketrans(_INTS, _CHARS))


def part_1(filepath=None):
    rules, messages = get_inputs(filepath)
    count = 0
    parser = lark.Lark(rules, start="a")
    for m in messages:
        try:
            parser.parse(m)
            count += 1
        except lark.LarkError:
            pass
    return count


def part_2(filepath=None):
    rules, messages = get_inputs(filepath)
    rules = rules.replace(
        fix_production_rule("8: 42"), fix_production_rule("8: 42 | 42 8")
    )
    rules = rules.replace(
        fix_production_rule("11: 42 31"), fix_production_rule("11: 42 31 | 42 11 31")
    )
    count = 0
    parser = lark.Lark(rules, start="a")
    for m in messages:
        try:
            parser.parse(m)
            count += 1
        except lark.LarkError:
            pass
    return count


if __name__ == "__main__":
    print("Day 19")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
