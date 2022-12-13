import aoc
from functools import cmp_to_key


year, day = 2022, 13

input_puzzle = aoc.setup(year, day, show_title=False, f="input.txt")


def evaluate(left, right) -> int:
    if type(left) == int and type(right) == int:
        if left < right:
            return -1

    elif type(left) == list and type(right) == list:
        for x, value in enumerate(left):
            try:
                if value == right[x]:
                    continue

                return evaluate(value, right[x])
            except IndexError:
                return 1

        return -1

    elif type(left) == int:
        left = [left]

        return evaluate(left, right)

    elif type(right) == int:
        right = [right]

        return evaluate(left, right)

    return 1


def part_1():
    puzzle = input_puzzle.split("\n\n")

    for i, pair in enumerate(puzzle):
        pair = pair.splitlines()
        for j, line in enumerate(pair):
            if line == "":
                continue

            pair[j] = eval(line)

        puzzle[i] = pair

    res = 0

    for index, values in enumerate(puzzle):
        if evaluate(*values) == -1:
            res += index + 1

    return res


def part_2():
    puzzle = []

    for j, line in enumerate(input_puzzle.splitlines()):
        if line == "":
            continue

        puzzle.append(eval(line))

    puzzle.append([[2]])
    puzzle.append([[6]])

    puzzle = sorted(puzzle, key=cmp_to_key(evaluate))

    return (puzzle.index([[2]]) + 1) * (puzzle.index([[6]]) + 1)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
