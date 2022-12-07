import aoc
from utils import find_ints


year, day = 2022, 7

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()

dirs = {}

formers = []

for l in puzzle:
    if l.startswith("dir"):
        continue

    if l.startswith("$ cd"):
        if ".." in l:
            formers.pop(-1)

        else:
            dir = l.split()[2]

            subdir = dirs
            for f in formers:
                subdir = subdir[f]

            subdir[dir] = {}
            subdir[dir]["VALUE"] = 0
            formers.append(dir)

    elif not l.startswith("$ ls"):
        subdir = dirs
        for f in formers:
            subdir = subdir[f]

        subdir["VALUE"] += find_ints(l)[0]


dir_values = []


def evaluate(name, cur_dir: dict):
    subvalues = 0

    for k, v in cur_dir.items():
        if k == "VALUE":
            continue

        subvalues += evaluate(k, v)

    myValue = cur_dir["VALUE"] + subvalues

    dir_values.append(myValue)
    return myValue


evaluate("/", dirs["/"])


def part_1():
    return sum(filter(lambda x: x <= 100000, dir_values))


def part_2():
    available = 70000000 - dir_values[-1]
    needed = 30000000
    toFree = needed - available

    return min(filter(lambda x: x >= toFree, dir_values))


if __name__ == '__main__':
    print(part_1())
    print(part_2())