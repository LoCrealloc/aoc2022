import aoc

year, day = 2022, 8

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def part_1():
    res = 0

    for i, line in enumerate(puzzle):
        for j, tree in enumerate(line):
            tree = int(tree)

            if all([
                any(int(t) >= tree for t in line[:j]),
                any(int(t) >= tree for t in line[j + 1:]),
                any(int(t) >= tree for t in [l[j] for l in puzzle[:i]]),
                any(int(t) >= tree for t in [l[j] for l in puzzle[i + 1:]])
            ]):
                continue

            res += 1

    return res


def part_2():
    def evaluate(trees):
        value = 0

        for x in trees:
            value += 1
            if int(x) >= tree:
                break

        return value

    res = 0

    for i, line in enumerate(puzzle):
        for j, tree in enumerate(line):
            tree = int(tree)

            left = list(line[:j])
            right = list(line[j + 1:])
            top = list([l[j] for l in puzzle[:i]])
            bottom = list([l[j] for l in puzzle[i + 1:]])

            left.reverse()
            top.reverse()

            total = (evaluate(left) * evaluate(right) * evaluate(top) * evaluate(bottom))
            if total > res:
                res = total

    return res


if __name__ == '__main__':
    print(part_1())
    print(part_2())
