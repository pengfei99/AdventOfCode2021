import re
from collections import deque, Counter
from scipy.spatial.transform import Rotation as R
import numpy as np
import itertools


def rotation_gen(scanner_list):
    rots = [
        R.from_euler('ZX', [0, 0], degrees=True),
        R.from_euler('ZX', [0, 90], degrees=True),
        R.from_euler('ZX', [0, 180], degrees=True),
        R.from_euler('ZX', [0, 270], degrees=True),
        R.from_euler('ZX', [90, 0], degrees=True),
        R.from_euler('ZX', [90, 90], degrees=True),
        R.from_euler('ZX', [90, 180], degrees=True),
        R.from_euler('ZX', [90, 270], degrees=True),
        R.from_euler('ZX', [180, 0], degrees=True),
        R.from_euler('ZX', [180, 90], degrees=True),
        R.from_euler('ZX', [180, 180], degrees=True),
        R.from_euler('ZX', [180, 270], degrees=True),
        R.from_euler('ZX', [270, 0], degrees=True),
        R.from_euler('ZX', [270, 90], degrees=True),
        R.from_euler('ZX', [270, 180], degrees=True),
        R.from_euler('ZX', [270, 270], degrees=True),
        R.from_euler('YX', [90, 0], degrees=True),
        R.from_euler('YX', [90, 90], degrees=True),
        R.from_euler('YX', [90, 180], degrees=True),
        R.from_euler('YX', [90, 270], degrees=True),
        R.from_euler('YX', [270, 0], degrees=True),
        R.from_euler('YX', [270, 90], degrees=True),
        R.from_euler('YX', [270, 180], degrees=True),
        R.from_euler('YX', [270, 270], degrees=True),
    ]

    for r in rots:
        yield np.round(r.apply(scanner_list)).astype(int)


def read_line(file_name):
    with open(file_name) as f:
        scanner_lines = []
        scanner = []
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(line)
            # if we a new scanner, add the scanner to the list, and reset the scanner to []
            if lines[i] == "\n":
                scanner_lines.append(scanner)
                scanner = []
            # if it's the last line
            elif i == (len(lines) - 1):
                scanner.append(lines[i])
                scanner_lines.append(scanner)
            else:
                scanner.append(lines[i])

        scanners = {
            int(re.search(r'[0-9]+', x[0]).group(0)):
                np.array([np.array(list(map(int, y.split(','))), dtype=float) for y in x[1:]])
            for x in scanner_lines
        }
    return scanners


def part_1(scanners):
    beacons = set(tuple(x) for x in scanners[0].astype(int))
    remaining = deque(v for k, v in scanners.items() if k != 0)
    scanner_poss = list(np.array([0, 0, 0]))

    while len(remaining):
        cur = remaining.pop()
        for rotd in rotation_gen(cur):
            c = Counter()
            for v in beacons:
                c.update(tuple(x) for x in rotd - np.array(v, dtype=int))
            [(diff, count)] = c.most_common(1)
            if count >= 12:
                beacons |= set(tuple(x) for x in rotd - np.array(diff, dtype=int))
                scanner_poss.append(np.array(diff, dtype=int))
                break
        else:
            remaining.appendleft(cur)
    print(f'Part 1: {len(beacons)}')
    return scanner_poss


def part_2(scanner_poss):
    result = max(np.abs(x - y).sum() for x in scanner_poss for y in scanner_poss)
    print(f'Part 2: {result}')


def main():
    test_scanner = read_line("data/test.txt")
    prod_scanner = read_line("data/prod.txt")

    # print(test_scanner)
    scanner_poss = part_1(prod_scanner)

    part_2(scanner_poss)


if __name__ == "__main__":
    main()
