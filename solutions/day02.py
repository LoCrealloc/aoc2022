import aoc

year, day = 2022, 2

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")
puzzle = puzzle.splitlines()


elfValues = ["A", "B", "C"]
myValues = ["X", "Y", "Z"]


def part_1():
    res = 0

    for line in puzzle:
        elf, me = line.split(" ")
        elf = myValues[elfValues.index(elf)]

        res += myValues.index(me) + 1

        if me == elf:
            res += 3  # Draw

        elif elf == myValues[myValues.index(me)-1]:
            res += 6  # Win

    return res


def part_2():
    res = 0

    for line in puzzle:
        elf, me = line.split(" ")
        elf = myValues[elfValues.index(elf)]

        if me == "X":
            me = myValues[myValues.index(elf)-1]
        elif me == "Y":
            me = elf
        else:
            me = myValues[myValues.index(elf)+1 if myValues.index(elf) != 2 else 0]

        res += myValues.index(me) + 1

        if me == elf:
            res += 3  # Draw

        elif elf == myValues[myValues.index(me) - 1]:
            res += 6  # Win

    return res


if __name__ == '__main__':
    print(part_1())
    print(part_2())






