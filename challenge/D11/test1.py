import time
from collections import deque


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time() - t) + ' sec')
        return ret

    return wrapper_method


deltas = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]


def print_grid(grid):
    for l in grid:
        print(' '.join(map(str, l)))


@profiler
def part1(path):
    grid = [list(map(int, list(l.strip()))) for l in open(path)]

    flashes = 0

    trig = set()
    ready = deque()

    for _ in range(100):

        trig.clear()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    ready.append((x, y))
                    trig.add((x, y))

        while ready:
            nx, ny = ready.popleft()
            for dx, dy in deltas:
                if 0 <= nx + dx < len(grid) and 0 <= ny + dy < len(grid[0]):
                    grid[nx + dx][ny + dy] += 1
                    if grid[nx + dx][ny + dy] > 9 and (nx + dx, ny + dy) not in trig:
                        ready.append((nx + dx, ny + dy))
                        trig.add((nx + dx, ny + dy))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 9:
                    grid[x][y] = 0
                    flashes += 1

    print(flashes)


@profiler
def part2(path):
    grid = [list(map(int, list(l.strip()))) for l in open(path)]

    ready = deque()

    cnt = 0
    while True:
        if all([all([i == 0 for i in l]) for l in grid]):
            break

        cnt += 1
        trig = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    ready.append((x, y))
                    trig.add((x, y))

        while ready:
            nx, ny = ready.popleft()
            for dx, dy in deltas:
                if 0 <= nx + dx < len(grid) and 0 <= ny + dy < len(grid[0]):
                    grid[nx + dx][ny + dy] += 1
                    if grid[nx + dx][ny + dy] > 9 and (nx + dx, ny + dy) not in trig:
                        ready.append((nx + dx, ny + dy))
                        trig.add((nx + dx, ny + dy))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 9:
                    grid[x][y] = 0

    print(cnt)


def main():
    test_path = "data/test.txt"
    prod_path="data/prod.txt"
    part1(prod_path)
    part2(prod_path)


if __name__ == "__main__":
    main()
