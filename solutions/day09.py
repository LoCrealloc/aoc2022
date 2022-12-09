import aoc

year, day = 2022, 9

def calcAllowed(x, y):
    return [
        (x-1, y+1), (x, y+1), (x+1, y+1),
        (x - 1, y), (x, y), (x + 1, y),
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
    ]


puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def part_1():
    visited = set()

    xH = 0
    yH = 0

    x, y = 0, 0

    for line in puzzle:
        d, t = line.split(" ")

        visited.add((x, y))

        for i in range(int(t)):

            former = (xH, yH)

            if d in ("L", "R"):
                xH = xH + 1 if d == "R" else xH - 1

            else:
                yH = yH + 1 if d == "U" else yH - 1

            if (x, y) not in calcAllowed(xH, yH):
                x, y = former

                visited.add((x, y))

    return len(visited)

if __name__ == '__main__':
    print(part_1())