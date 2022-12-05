import aoc
from utils import find_ints
from copy import deepcopy

year, day = 2022, 5

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()

# Input parsing
parsed = []

stacks = puzzle[:8]
ins = puzzle[10:]

for stack in stacks:
    stack = stack.replace("[", " ").replace("]", " ").replace("   ", " ")

    crate_line = []

    for count, c in enumerate(stack):
        if (count+1) % 2 == 0:
            crate_line.append(c)

    parsed.append(crate_line)

for s in parsed:
    s += [" "] * (len(max(parsed)) - len(s))

parsed.reverse()


def find_index(index, crates):
    r = 0

    for crateIndex, crate in enumerate(crates):
        if crate[index] != " ":
            r = crateIndex

    return r


def evaluate(crates: list[list[str]]) -> str:
    res = ""
    for index, _ in enumerate(crates[0]):
        res += crates[find_index(index, crates)][index]

    return res


def part_1(crates):
    for i in ins:
        nums = find_ints(i)

        many = nums[0]

        f = nums[1] - 1
        to = nums[2] - 1

        where = find_index(f, crates)
        to_h = (find_index(to, crates) + 1) if crates[0][to] != " " else 0

        for _ in range(many):
            crate = crates[where][f]
            crates[where][f] = " "

            where -= 1

            try:
                crates[to_h][to] = crate
            except IndexError:
                crates.append([" " for _ in range(len(crates[0]))])
                crates[to_h][to] = crate

            to_h += 1

    return evaluate(crates)


def part_2(crates):
    for i in ins:
        nums = find_ints(i)

        many = nums[0]

        f = nums[1] - 1
        to = nums[2] - 1

        where = find_index(f, crates)
        to_h = (find_index(to, crates) + 1) if crates[0][to] != " " else 0

        to_move = []

        for _ in range(many):
            to_move.append(crates[where][f])
            crates[where][f] = " "

            where -= 1

        to_move.reverse()

        for crate in to_move:
            try:
                crates[to_h][to] = crate
            except IndexError:
                crates.append([" " for _ in range(len(crates[0]))])
                crates[to_h][to] = crate

            to_h += 1

    return evaluate(crates)


if __name__ == '__main__':
    print(part_1(deepcopy(parsed)))
    print(part_2(deepcopy(parsed)))
