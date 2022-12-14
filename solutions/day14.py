# Inspired by Defelo https://github.com/Defelo/AdventOfCode

from datetime import date

import pyperclip

import aoc
import re
from collections import deque, Counter
from utils import find_ints
from copy import deepcopy


x_killer = 0


def ans(answer):
    print(answer)
    pyperclip.copy(str(answer))


def plot(img):
    for line in img:
        for c in line:
            print(c, end="")

        print("")


year, day = (t := date.today()).year, t.day

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()

line = ["."] * 1000
cave = []
for i in range(200):
    cave.append(deepcopy(line))

bottom = 0

for l in puzzle:
    ints = find_ints(l)

    pairs = []

    old_x = None
    old_y = None

    for i in range(0, len(ints), 2):
        pairs.append(ints[i:i + 2])

    for x, y in pairs:
        x = x - x_killer

        if old_y is not None:

            if x == old_x:
                for j in range(old_y, y + 1 if old_y < y else y - 1, 1 if old_y < y else -1):
                    cave[j][x] = "#"

            else:
                for j in range(old_x, x + 1 if old_x < x else x - 1, 1 if old_x < x else -1):
                    cave[y][j] = "#"

        old_x = x
        old_y = y

        if y > bottom:
            bottom = y


def part_1(m):
    global bottom

    res = 0

    while True:
        pos = (500 - x_killer, 0)

        m[0][500 - x_killer] = "o"

        while True:
            if pos[1] > bottom:
                break

            if m[pos[1] + 1][pos[0]] == ".":
                m[pos[1] + 1][pos[0]] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0], pos[1] + 1)

            elif m[pos[1] + 1][pos[0] - 1] == ".":
                m[pos[1] + 1][pos[0] - 1] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0] - 1, pos[1] + 1)

            elif m[pos[1] + 1][pos[0] + 1] == ".":
                m[pos[1] + 1][pos[0] + 1] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0] + 1, pos[1] + 1)

            else:
                res += 1

                break

        if pos[1] > bottom:
            break

    return res


def part_2(m):
    global bottom

    bottom = bottom + 2

    for index, _ in enumerate(m[bottom]):
        m[bottom][index] = "#"

    res = 0

    while True:
        pos = (500-x_killer, 0)

        m[0][500-x_killer] = "o"

        instant = False

        while True:
            if m[pos[1] + 1][pos[0]] == ".":
                m[pos[1] + 1][pos[0]] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0], pos[1] + 1)

            elif m[pos[1] + 1][pos[0] - 1] == ".":
                m[pos[1] + 1][pos[0] - 1] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0] - 1, pos[1] + 1)

            elif m[pos[1] + 1][pos[0] + 1] == ".":
                m[pos[1] + 1][pos[0] + 1] = "o"

                m[pos[1]][pos[0]] = "."

                pos = (pos[0] + 1, pos[1] + 1)

            else:
                res += 1

                if pos[1] == 0:
                    instant = True

                break

        if instant:
            break

    return res


if __name__ == '__main__':
    print(part_1(deepcopy(cave)))
    print(part_2(cave))
