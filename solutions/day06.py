import aoc
from collections import Counter


year, day = 2022, 6

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")


def part_1():
    for i, x in enumerate(puzzle):
        if not i < 4 and Counter(puzzle[i-4:i]).most_common(1)[0][1] == 1:
            return i


def part_2():
    for i, x in enumerate(puzzle):
        if not i < 14 and Counter(puzzle[i-14:i]).most_common(1)[0][1] == 1:
            return i


if __name__ == '__main__':
    print(part_1())
    print(part_2())
