import aoc
from copy import deepcopy


year, day = 2022, 17

puzzle = aoc.setup(year, day, show_title=False, f="input.txt")

jet = puzzle

rocks = [
    [
        ["@", "@", "@", "@"]
    ],
    [
        [".", "@", "."],
        ["@", "@", "@"],
        [".", "@", "."]
    ],
    [
        ["@", "@", "@"],
        [".", ".", "@"],
        [".", ".", "@"],
    ],
    [
        ["@"],
        ["@"],
        ["@"],
        ["@"]
    ],
    [
        ["@", "@"],
        ["@", "@"]
    ],
]


def part_1():
    def calc_height():
        out = 0

        for c, l in enumerate(chamber):
            if "#" in l:
                out = c + 1
            else:
                break

        return out

    rock = 0
    count = 0

    move = 0

    chamber = []
    chamber_height = ["."] * 7
    for _ in range(5000):
        chamber.append(deepcopy(chamber_height))

    while count != 2022:

        spawn = calc_height() + 3

        current_rock = rocks[rock]

        rock_height = len(current_rock)
        rock_width = len(current_rock[0])

        for i, line in enumerate(current_rock):
            for j, part in enumerate(line):
                chamber[spawn + i][j + 2] = part

        pos = [2, spawn]

        while True:
            ins = jet[move]
            if move == len(jet) - 1:
                move = 0
            else:
                move += 1

            if ins == ">":
                add = 1
            else:
                add = -1

            ok = False

            for i in range(pos[1], pos[1] + rock_height):

                line = chamber[i]
                indices = [x for x in range(len(line)) if line[x] == "@"]

                if ins == ">":
                    if indices[-1] <= 5 and chamber[i][indices[-1] + add] == ".":
                        ok = True
                    else:
                        ok = False
                else:
                    if 1 <= indices[0] and chamber[i][indices[0] + add] == ".":
                        ok = True
                    else:
                        ok = False

                if not ok:
                    break

            if ok:
                for i in range(pos[1], pos[1] + rock_height):

                    line = chamber[i]
                    indices = [x for x in range(len(line)) if line[x] == "@"]

                    for index in indices:
                        chamber[i][index] = "."

                    for index in indices:
                        chamber[i][index + add] = "@"

            pos[0] += add

            h = pos[1]

            ok = False

            if pos[1] == 0:
                for i in range(pos[1], pos[1] + rock_height):
                    line = chamber[i]

                    indices = [x for x in range(len(line)) if line[x] == "@"]

                    for index in indices:
                        chamber[i][index] = "#"

                break

            for i in range(pos[1], pos[1] + rock_height):
                line = chamber[i]

                indices = [x for x in range(len(line)) if line[x] == "@"]

                for index in indices:
                    ok = not (chamber[i - 1][index] == "#")

                    if not ok:
                        break

                if not ok:
                    break

            if ok:
                for i in range(pos[1], pos[1] + rock_height):
                    line = chamber[i]

                    indices = [x for x in range(len(line)) if line[x] == "@"]

                    for index in indices:
                        chamber[i][index] = "."
                        chamber[i - 1][index] = "@"

            else:
                for i in range(pos[1], pos[1] + rock_height):
                    line = chamber[i]

                    indices = [x for x in range(len(line)) if line[x] == "@"]

                    for index in indices:
                        chamber[i][index] = "#"

                break

            pos[1] -= 1

        if rock == len(rocks) - 1:
            rock = 0
        else:
            rock += 1

        count += 1


    return calc_height()


if __name__ == '__main__':
    print(part_1())