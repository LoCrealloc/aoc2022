import aoc


year, day = 2022, 20

puzzle_input = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def part_1():
    puzzle = list(map(int, puzzle_input))
    puzzle = list(zip(puzzle, range(len(puzzle))))

    zero = ()

    for p in puzzle[::]:
        index = puzzle.index(p)
        num = p[0]

        if num == 0:
            zero = p

        to = puzzle[:index]
        after = puzzle[(index + 1):]

        tmp = to + after

        new_index = (index + num) % len(tmp)

        to = tmp[:new_index]
        after = tmp[new_index:]

        puzzle = to + [p] + after

    res = 0

    for i in [1000, 2000, 3000]:
        index = (i + puzzle.index(zero)) % len(puzzle)

        res += puzzle[index][0]

    return res


def part_2():
    puzzle = list(map(lambda x: int(x) * 811589153, puzzle_input))
    puzzle = list(zip(puzzle, range(len(puzzle))))

    original_puzzle = puzzle[::]

    zero = ()

    for _ in range(10):
        for p in original_puzzle:

            index = puzzle.index(p)
            num = p[0]

            if num == 0:
                zero = p

            to = puzzle[:index]
            after = puzzle[(index + 1):]

            tmp = to + after

            new_index = (index + num) % len(tmp)

            to = tmp[:new_index]
            after = tmp[new_index:]

            puzzle = to + [p] + after

    res = 0

    for i in [1000, 2000, 3000]:
        index = (i + puzzle.index(zero)) % len(puzzle)
        res += puzzle[index][0]

    return res


if __name__ == '__main__':
    print(part_1())
    print(part_2())
