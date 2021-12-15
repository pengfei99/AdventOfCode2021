# read the marker number file and return a list

import heapq
from collections import defaultdict
from itertools import filterfalse
from math import inf as INFINITY


def read_line(file_name):
    with open(file_name) as f:
        matrix = []
        for line in f.readlines():
            line_text = line.strip("\n")
            row = []
            for c in line_text:
                row.append(int(c))
            matrix.append(row)
    return matrix


def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < w and 0 <= cc < h:
            yield rr, cc


def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    source = (0, 0)
    destination = (h - 1, w - 1)

    queue = [(0, source)]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    visited = set()

    while queue:
        dist, node = heapq.heappop(queue)

        if node == destination:
            return dist

        if node in visited:
            continue

        visited.add(node)
        r, c = node

        for neighbor in filterfalse(visited.__contains__, neighbors4(r, c, h, w)):
            nr, nc = neighbor
            newdist = dist + grid[nr][nc]

            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))

    return INFINITY


def part_2(grid):
    tilew = len(grid)
    tileh = len(grid[0])

    for _ in range(4):
        for row in grid:
            tail = row[-tilew:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(4):
        for row in grid[-tileh:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)

    return dijkstra(grid)


def main():
    test_matrix = read_line("data/test.txt")
    prod_matrix = read_line("data/prod.txt")

    minrisk = dijkstra(prod_matrix)

    print(f"part1: {minrisk}")

    part2_res = part_2(prod_matrix)
    print(f"part2: {part2_res}")


if __name__ == "__main__":
    main()
