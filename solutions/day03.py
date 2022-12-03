import aoc

from string import ascii_letters

year, day = 2022, 3

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")
puzzle = puzzle.splitlines()


def part_1():
    res = 0

    for line in puzzle:
        half = int(len(line) / 2)
        h1, h2 = line[:half], line[half:]

        for c in h1:
            if c in h2:
                res += ascii_letters.index(c) + 1
                break

    return res


def part_2():
    res = 0

    new = [puzzle[n:n + 3] for n in range(0, len(puzzle), 3)]

    for b in new:
        for c in b[0]:
            if c in b[1] and c in b[2]:
                res += ascii_letters.index(c) + 1
                break

    return res


if __name__ == '__main__':
    print(part_1())
    print(part_2())
