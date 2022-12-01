import aoc

year, day = 2022, 1

puzzle = aoc.setup(year, day, show_title=False, f="../input.txt")
puzzle = puzzle.split("\n\n")

elves = [sum([int(x) for x in elf.splitlines()]) for elf in puzzle]


def part_1():
    return max(elves)


def part_2():
    return sum(sorted(elves, reverse=True)[:3])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
