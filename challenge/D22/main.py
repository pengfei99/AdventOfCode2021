import math


def read_line(file_name):
    with open(file_name) as f:
        lines = []
        for line in f.readlines():
            s = line.strip()
            on_off = s.split()[0]
            bounds = [[int(x) for x in s.split()[1].split(',')[i].split('=')[1].split('..')] for i in range(3)]
            lines.append((on_off, *bounds))
    return lines


def intersection(cube1, cube2):
    xb1, yb1, zb1 = cube1
    xb2, yb2, zb2 = cube2
    for a, b in zip(cube1, cube2):
        if a[0] > b[1] or a[1] < b[0]:
            return None

    return tuple((max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(cube1, cube2))


def difference(cube1, cube2):
    int = intersection(cube1, cube2)
    if not int:
        return [cube1]
    new_cubes = []
    new_cubes.append((cube1[0], cube1[1], (cube1[2][0], int[2][0] - 1)))
    new_cubes.append((cube1[0], cube1[1], (int[2][1] + 1, cube1[2][1])))
    new_cubes.append(((cube1[0][0], int[0][0] - 1), cube1[1], int[2]))
    new_cubes.append(((int[0][1] + 1, cube1[0][1]), cube1[1], int[2]))
    new_cubes.append((int[0], (cube1[1][0], int[1][0] - 1), int[2]))
    new_cubes.append((int[0], (int[1][1] + 1, cube1[1][1]), int[2]))

    return [(x, y, z) for x, y, z in new_cubes if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]


def init_cubs(instruction_lines):
    cubes = []
    for line in instruction_lines:
        onoff = line[0]
        this_cube = line[1:]
        new_cubes = []
        for cube in cubes:
            new_cubes.extend(difference(cube, this_cube))
        if onoff == 'on':
            new_cubes.append(this_cube)
        cubes = new_cubes
    print(f"has total cubes: {len(cubes)}")
    return cubes


def part_1(cubes):
    s1 = 0
    for cube in cubes:
        s1 += math.prod(max(0, min(50, cube[i][1]) - max(-50, cube[i][0]) + 1) for i in range(3))
    print(f"part_1 result: {s1}")


def part_2(cubes):
    s2 = 0
    for cube in cubes:
        s2 += math.prod(cube[i][1] - cube[i][0] + 1 for i in range(3))
    print(f"part_2 result: {s2}")


def main():
    test_lines = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")

    cubes = init_cubs(prod_lines)
    part_1(cubes)
    part_2(cubes)


if __name__ == "__main__":
    main()
