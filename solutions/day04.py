import aoc

year, day = 2022, 4

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")

puzzle = [[list(map(int, nums.split("-"))) for nums in line.split(",")] for line in puzzle.splitlines()]


def part_1():
    res = 0

    for left, right in puzzle:
        if (left[0] <= right[0] and right[1] <= left[1]) or (right[0] <= left[0] and left[1] <= right[1]):
            res += 1

    return res


def part_2():
    res = 0

    for left, right in puzzle:
        if left[0] <= right[0] <= left[1] or right[0] <= left[0] <= right[1]:
            res += 1

    return res


if __name__ == '__main__':
    print(part_1())
    print(part_2())
