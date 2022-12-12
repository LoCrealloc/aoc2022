import aoc
from sys import maxsize
from copy import deepcopy


def get_neighbours(m, c_x, c_y):
    out = []

    max_x = len(m[0]) - 1
    max_y = len(m) - 1

    if c_x > 0:
        out.append((c_x - 1, c_y))

    if c_x < max_x:
        out.append((c_x + 1, c_y))

    if c_y > 0:
        out.append((c_x, c_y - 1))

    if c_y < max_y:
        out.append((c_x, c_y + 1))

    return out


def compare(one, two):
    if ord(one) == ord(two) or (ord(one) + 1 == ord(two)) or ord(one) > ord(two):
        return True

    return False


def is_dead_a(a):
    visited = []
    queue = [a]

    while queue:
        cur = queue.pop(0)

        for neighbour in get_neighbours(puzzle, *cur):
            if puzzle[neighbour[1]][neighbour[0]] == "b":
                return True

            if neighbour not in visited and not (ord(puzzle[neighbour[1]][neighbour[0]]) > ord("b")):
                visited.append(neighbour)
                queue.append(neighbour)

    return False



year, day = 2022, 12

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()

for i, line in enumerate(puzzle):
    puzzle[i] = list(line)

o_unvisited = []

e = s = (0,0)

for y, line in enumerate(puzzle):
    if "S" in line:
        s = (line.index("S"), y)

    if "E" in line:
        e = (line.index("E"), y)

    for x, _ in enumerate(line):
        o_unvisited.append((x, y))

puzzle[e[1]][e[0]] = "z"
puzzle[s[1]][s[0]] = "a"


o_path = {}
o_a_nodes = []

for u in o_unvisited:
    if puzzle[u[1]][u[0]] == "a":
        o_a_nodes.append(u)

    o_path[u] = maxsize


def part_1(path, unvisited):

    prev = {}

    path[s] = 0

    while unvisited:
        current = None

        for node in unvisited:
            if current is None:
                current = node
            elif path[node] < path[current]:
                current = node

        neighbours = get_neighbours(puzzle, *current)

        for n in neighbours:
            if not compare(
                    puzzle[current[1]][current[0]],
                    puzzle[n[1]][n[0]]
            ):
                c = maxsize
            else:
                c = 1

            value = path[current] + c

            if value < path[n]:
                path[n] = value
                prev[n] = current

        unvisited.remove(current)

    p = []

    node = e
    while node != s:
        p.append(node)
        node = prev[node]

    return len(p)


def part_2(original_path, original_unvisited, a_nodes):
    res = maxsize

    a_nodes = list(filter(is_dead_a, a_nodes))

    for a in a_nodes:
        prev = {}

        path = deepcopy(original_path)
        unvisited = deepcopy(original_unvisited)

        path[a] = 0

        while unvisited:
            current = None

            for node in unvisited:
                if current is None:
                    current = node
                elif path[node] < path[current]:
                    current = node

            neighbours = get_neighbours(puzzle, *current)

            for n in neighbours:
                if not compare(
                        puzzle[current[1]][current[0]],
                        puzzle[n[1]][n[0]]
                ):
                    c = maxsize
                else:
                    c_value = puzzle[current[1]][current[0]]
                    n_value = puzzle[n[1]][n[0]]

                    if ord(n_value) < ord(c_value):
                        c = 3
                    elif ord(n_value) == ord(c_value):
                        c = 2
                    else:
                        c = 1

                value = path[current] + c

                if value < path[n]:
                    path[n] = value

                    prev[n] = current

            unvisited.remove(current)

        p = []

        node = e
        while node != a:
            p.append(node)
            node = prev[node]

        if len(p) < res:
            res = len(p)

    return res


if __name__ == '__main__':
    print(part_1(deepcopy(o_path), deepcopy(o_unvisited)))
    print(part_2(o_path, o_unvisited, o_a_nodes))
