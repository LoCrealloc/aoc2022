import aoc
from utils import find_ints


year, day = 2022, 15

y = 2000000

puzzle = aoc.setup(year, day, show_title=False, f="input.txt").splitlines()


def calc_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


beacons = []
sensors = []

for line in puzzle:
    nums = find_ints(line)

    beacons.append(nums[2:])
    sensors.append(nums[:2])


def part_1():
    points = set()

    for beacon, sensor in zip(beacons, sensors):

        distance = calc_distance(sensor, beacon)

        x1 = - abs(y - sensor[1]) + distance + sensor[0]
        x2 = abs(y - sensor[1]) - distance + sensor[0]

        if calc_distance(sensor, [x1, y]) != distance:
            continue

        if x1 < x2:
            for p in range(x1, x2+1):
                points.add(p)
        else:
            for p in range(x2, x1+1):
                points.add(p)

    res = len(points)

    new_beacons = list()

    for beacon in beacons:
        if beacon not in new_beacons:
            new_beacons.append(beacon)

    for beacon in new_beacons:
        if beacon[1] == y:
            if beacon[0] in points:
                res -= 1

    return res


if __name__ == '__main__':
    print(part_1())
