import aoc


year, day = 2022, 25

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def part_1():
    def snafu_to_dec(num):
        s = 0

        cnum = list(num)
        cnum.reverse()

        for j, c in enumerate(cnum):
            m = 5 ** j

            if c == "=":
                s -= 2 * m
            elif c == "-":
                s -= 1 * m
            else:
                s += int(c) * m

        return s

    res = 0

    for n in puzzle:
        res += snafu_to_dec(n)

    exp = 0
    while 2 * (5 ** exp) < res:
        exp += 1

    snafu = ["0"] * (exp + 1)

    for index, i in enumerate(range(exp, -1, -1)):

        if (snafu_dec := snafu_to_dec("".join(snafu))) < res:

            if abs(res - (snafu_dec + (5 ** i))) < abs(res - (snafu_dec + (2 * (5 ** i)))):
                snafu[index] = "1"
            else:
                snafu[index] = "2"

        elif snafu_dec > res:

            if abs(res - (snafu_dec - (5 ** i))) < abs(res - (snafu_dec - (2 * (5 ** i)))):
                snafu[index] = "-"
            else:
                snafu[index] = "="

        if abs(res - snafu_to_dec(snafu)) > abs(res - snafu_dec):
            snafu[index] = "0"

    return "".join(snafu)


if __name__ == '__main__':
    print(part_1())
