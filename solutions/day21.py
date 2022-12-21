import aoc
import re

year, day = 2022, 21

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()

monkeys = {}

for m in puzzle:
    p1, p2 = m.split(": ")

    monkeys[p1] = p2


def part_1():
    def evaluate(monkey):

        value = monkeys[monkey]

        if value.isdigit():
            return int(value)

        n_monkeys = re.findall(r"(\w+) [+\-*/] (\w+)", value)

        n_monkeys = n_monkeys[0]

        return int(eval(
            value, {
                n_monkeys[0]: evaluate(n_monkeys[0]),
                n_monkeys[1]: evaluate(n_monkeys[1])
            }))

    return evaluate("root")


def part_2():
    opposites = {
        "+": "-",
        "-": "+",
        "*": "//",
        "/": "*"
    }

    monkeys["humn"] = "99999"

    def evaluate(monkey, path):

        value = monkeys[monkey]

        path[monkey] = str(value)

        if re.match(r"\d", value):
            return int(value), path

        n_monkeys = re.findall(r"(\w+) [+\-*/] (\w+)", value)

        n_monkeys = n_monkeys[0]

        return int(eval(
            value, {
                n_monkeys[0]: evaluate(n_monkeys[0], path)[0],
                n_monkeys[1]: evaluate(n_monkeys[1], path)[0]
            })), path

    def evaluate_path(key):
        parts = path[key].split(" ")

        if len(parts) == 1:
            if parts[0] == "X":
                return parts[0]
            return int(parts[0])

        l = evaluate_path(parts[0])
        r = evaluate_path(parts[2])

        if type(l) == int and type(r) == int:
            return int(eval(f"{l}{parts[1]}{r}"))

        return [l, parts[1], r]

    left_monkey, right_monkey = re.findall(r"(\w+) [+\-*/] (\w+)", monkeys["root"])[0]
    right, r_path = evaluate(right_monkey, {})
    left, l_path = evaluate(left_monkey, {})

    if "99999" in [q[1] for q in r_path]:
        path = r_path
        relevant_monkey = right_monkey
        relevant_number = -left
    else:
        path = l_path
        relevant_monkey = left_monkey
        relevant_number = -right

    path["humn"] = "X"

    x = evaluate_path(relevant_monkey)

    def do(l, s, r, number):

        if type(l) == int:
            num = l
            n = r
        else:
            num = r
            n = l

        s = opposites[s]

        number = int(eval(f"{number}{s}{num}"))

        if n == "X":
            return number

        return do(*n, number)

    return do(*x, relevant_number)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
