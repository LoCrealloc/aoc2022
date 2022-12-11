import aoc
from utils import find_ints, find_ints_strings
from copy import deepcopy

year, day = 2022, 11

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").split("\n\n")

factor = 1
initials = {}

for monkey_input in puzzle:
    m = monkey_input.splitlines()

    key = find_ints_strings(m[0])[0]

    initials[key] = {"count": 0}

    initials[key]["items"] = find_ints(m[1])

    initials[key]["op"] = m[2].split("new = ")[1]

    initials[key]["test"] = find_ints(m[3])[0]
    factor *= initials[key]["test"]

    initials[key]["true"] = find_ints_strings(m[4])[0]

    initials[key]["false"] = find_ints_strings(m[5])[0]


def part_1(monkeys):
    for i in range(20):
        for monkey_key in monkeys.keys():
            monkey = monkeys[monkey_key]

            for item in monkey["items"]:
                monkey["count"] += 1

                level = eval(monkey["op"], {"old": item})

                level //= 3

                if level % monkey["test"] == 0:
                    a_monkey = monkeys[monkey["true"]]
                else:
                    a_monkey = monkeys[monkey["false"]]

                a_monkey["items"].append(level)

            monkey["items"] = []

    counts = sorted([monkey["count"] for monkey in monkeys.values()])
    return counts[-1] * counts[-2]


def part_2(monkeys):
    for i in range(10000):
        for monkey_key in monkeys.keys():
            monkey = monkeys[monkey_key]

            for item in monkey["items"]:
                monkey["count"] += 1

                level = int(eval(monkey["op"], {"old": item}))

                if level % monkey["test"] == 0:
                    a_monkey = monkeys[monkey["true"]]
                else:
                    a_monkey = monkeys[monkey["false"]]

                level %= factor

                a_monkey["items"].append(level)

            monkey["items"] = []

    counts = sorted([monkey["count"] for monkey in monkeys.values()])
    return counts[-1] * counts[-2]


if __name__ == '__main__':
    print(part_1(deepcopy(initials)))
    print(part_2(initials))
