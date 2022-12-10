import aoc
from copy import deepcopy

year, day = 2022, 10

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def plot(img):
    for line in img:
        for c in line:
            print(c, end=" ")

        print("")


def part_1():
    cycle = 0
    x = 1
    res = 0

    for ins in puzzle:
        cycle += 1

        if cycle == 20 or cycle % 40 == 20:
            res += cycle * x

        if ins.startswith("addx"):
            cycle += 1

            if cycle == 20 or cycle % 40 == 20:
                res += cycle * x

            x += int(ins.split()[1])

    return res


def part_2():
    spriteLine = ["."] * 40

    sprite = []
    for _ in range(6):
        sprite.append(deepcopy(spriteLine))

    x = 1
    crtX = crtY = 0

    def cycle_execution(posX, posY):
        for i in [x - 1, x, x + 1]:
            if i == posX:
                sprite[posY][posX] = "#"

        if posX == 39:
            posX = 0

            if posY == 5:
                posY = 0
            else:
                posY += 1

        else:
            posX += 1

        return posX, posY

    for ins in puzzle:
        crtX, crtY = cycle_execution(crtX, crtY)

        if ins.startswith("addx"):
            crtX, crtY = cycle_execution(crtX, crtY)

            x += int(ins.split()[1])

    return sprite


if __name__ == '__main__':
    print(part_1())
    plot(part_2())
