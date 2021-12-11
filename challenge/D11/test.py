import sys


def in_bounds(xy):
    (x, y) = xy
    return x >= 0 and x < 10 and y >= 0 and y < 10


def neighbours(xy):
    (x, y) = xy
    n = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
         (x - 1, y), (x + 1, y),
         (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return filter(in_bounds, n)


def do_flashes(I, visited=set()):
    flashes = filter(lambda xy: I[xy] > 9 and xy not in visited, I)

    if not flashes:
        return

    for xy in flashes:
        for nb_xy in neighbours(xy):
            I[nb_xy] += 1

    do_flashes(I, visited.union(set(flashes)))


def get_result(matrix):
    num_flashes = 0
    for step in range(1000):
        for xy in matrix:
            matrix[xy] += 1

        do_flashes(matrix)

        for xy in filter(lambda xy: matrix[xy] > 9, matrix):
            num_flashes += 1
            matrix[xy] = 0

        if (step == 99):
            print("part1", num_flashes)

        if all(map(lambda xy: I[xy] == 0, I)):
            print("part2", step + 1)
            break


def read_line(file_name):
    with open(file_name) as f:
        matrix = {(x, y): int(c) for y, line in enumerate(f.readlines())
                  for x, c in enumerate(line.strip("\n"))}
    return matrix


def main():
    sys.setrecursionlimit(15000)
    test_matrix = read_line("data/test.txt")

    assert (set(neighbours((0, 0))) == set([(0, 1), (1, 0), (1, 1)]))
    assert (set(neighbours((1, 1))) == set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]))
    assert (set(neighbours((9, 9))) == set([(8, 8), (8, 9), (9, 8)]))
    # get_result(test_matrix)


if __name__ == "__main__":
    main()
