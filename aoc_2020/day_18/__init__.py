import fileinput
import token
import tokenize
from io import StringIO
import ast

import typing


def get_inputs(filepath=None):
    return [l.strip() for l in fileinput.input(filepath or "inputs.txt")]


def to_tokens(s: str):
    return tokenize.generate_tokens(StringIO(s).readline)


def evaluate(s):
    tokens = to_tokens(s) if isinstance(s, str) else s
    stack = []
    ops = []

    for t in tokens:
        if t.type == token.NUMBER:
            stack.insert(0, t.string)

        elif t.type == token.OP:
            if t.string in "+*":
                ops.insert(0, t.string)
            elif t.string == "(":
                stack.insert(0, evaluate(tokens))
            else:
                break

    while len(ops) > 0:
        stack.append(eval(f"{stack.pop()}{ops.pop()}{stack.pop()}"))

    return stack[0]


class PrecedenceMod(ast.NodeTransformer):
    def visit_Add(self, node: ast.Add) -> typing.Any:
        return ast.Mult()

    def visit_Mult(self, node: ast.Mult) -> typing.Any:
        return ast.Add()


def evaluate_2(exp):
    exp = exp.replace("+", "t").replace("*", "+").replace("t", "*")
    tree = ast.parse(exp, mode="eval")
    mod_tree = PrecedenceMod().visit(tree)
    return eval(compile(mod_tree, "", mode="eval"))


def part_1(filepath=None):
    inputs = get_inputs(filepath)
    return sum(evaluate(i) for i in inputs)


def part_2(filepath=None):
    return sum(evaluate_2(i) for i in get_inputs(filepath))


if __name__ == "__main__":
    print("Day 18")
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
