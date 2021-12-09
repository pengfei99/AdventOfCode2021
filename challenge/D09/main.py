# read the marker number file and return a list
import math

import numpy

from challenge.D09.Point import Point


def read_line(file_name):
    with open(file_name) as f:
        # determine matrix dimension
        lines = f.readlines()
        h = len(lines)
        l = len(lines[0])
        # build matrix
        matrix = numpy.zeros((h, l - 1))
        for i in range(len(lines)):
            line_text = lines[i].strip("\n")
            char_list = []
            for c in line_text:
                char_list.append(c)
            for j in range(len(char_list)):
                matrix[i][j] = float(char_list[j])
    return matrix


def check_min(matrix):
    min_nums = []
    h, l = matrix.shape
    for i in range(0, h):
        for j in range(0, l):
            # left up corner case
            if i == 0 and j == 0 and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j + 1]:
                min_nums.append(int(matrix[i][j]))
            # first line mid column position case
            elif i == 0 and j > 0 and j < (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][
                j + 1] and matrix[i][j] < matrix[i][j - 1]:
                min_nums.append(int(matrix[i][j]))
            # first column mid line position case
            elif i > 0 and i < (h - 1) and j == 0 and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i + 1][
                j] and matrix[i][j] < matrix[i][j + 1]:
                min_nums.append(int(matrix[i][j]))
            # mid line, mid column position case
            elif i > 0 and i < (h - 1) and j > 0 and j < (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < \
                    matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1]:
                min_nums.append(int(matrix[i][j]))
            # left down corner case
            elif i == (h - 1) and j == 0 and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1]:
                min_nums.append(int(matrix[i][j]))
            # last line mid column case
            elif i == (h - 1) and j > 0 and j < (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                    matrix[i][j - 1] and matrix[i][j] < matrix[i][j + 1]:
                min_nums.append(int(matrix[i][j]))
            # right up corner case
            elif i == 0 and j == (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1]:
                min_nums.append(int(matrix[i][j]))
            # last column mid line case
            elif i > 0 and i < (h - 1) and j == (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                    matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1]:
                min_nums.append(int(matrix[i][j]))
            # right down corner case
            elif i == (h - 1) and j == (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j - 1]:
                min_nums.append(int(matrix[i][j]))
    return min_nums


def check_up(base_i, base_j, matrix):
    # check up point
    if (base_i - 1) >= 0:
        left_point = matrix[base_i - 1][base_j]
        right_point = matrix[base_i][base_j]
        if left_point.get_value() == right_point.get_value() + 1:
            mark_point_of_basin((base_i - 1), base_j, matrix)


def check_down(base_i, base_j, matrix):
    h, l = len(matrix), len(matrix[0])
    print(f"base_i: {base_i}, base_j:{base_j}, h:{h},l:{l}")
    # check down
    if (base_i + 1) < h:
        left_point = matrix[base_i + 1][base_j]
        right_point = matrix[base_i][base_j]
        if left_point.get_value() == right_point.get_value() + 1:
            mark_point_of_basin((base_i + 1), base_j, matrix)


def check_left(base_i, base_j, matrix):
    # check left
    if (base_j - 1) >= 0:
        left_point = matrix[base_i][base_j - 1]
        right_point = matrix[base_i][base_j]
        if left_point.get_value() == right_point.get_value() + 1:
            mark_point_of_basin(base_i, (base_j - 1), matrix)


def check_right(base_i, base_j, matrix):
    h, l = len(matrix), len(matrix[0])
    # check right
    if (base_j + 1) < l:
        left_point = matrix[base_i][base_j + 1]
        right_point = matrix[base_i][base_j]
        if left_point.get_value() == right_point.get_value() + 1:
            mark_point_of_basin(base_i, (base_j + 1), matrix)


def mark_point_of_basin(base_i, base_j, matrix):
    print(f"in mark_point_of_basin, base point: {base_i}, {base_j}")
    h, l = len(matrix), len(matrix[0])
    if 0 <= base_i < h and 0 <= base_j < l:
        # mark the current point
        matrix[base_i][base_j].mark_point()
        # check neighbour for possible basin point
        check_up(base_i, base_j, matrix)
        check_down(base_i, base_j, matrix)
        check_left(base_i, base_j, matrix)
        check_right(base_i, base_j, matrix)


def get_basin_size(base_i, base_j, matrix):
    # build a point matrix from the float matrix
    rows, cols = matrix.shape[0], matrix.shape[1]
    point_matrix = []
    for i in range(0, rows):
        point_row = []
        for j in range(0, cols):
            point = Point(matrix[i][j])
            point_row.append(point)
        point_matrix.append(point_row)
    print(f"in get_basin_size, base point: {base_i}, {base_j}")
    mark_point_of_basin(base_i, base_j, point_matrix)
    return get_marked_point_num(point_matrix)



def get_marked_point_num(point_matrix):
    count = 0
    for row in point_matrix:
        for point in row:
            if point.get_mark():
                count += 1
    return count


def get_basin_list(matrix):
    all_basin_size_list = []
    h, l = matrix.shape
    for i in range(0, h):
        for j in range(0, l):
            # left up corner case
            if i == 0 and j == 0 and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j + 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # first line mid column position case
            elif i == 0 and 0 < j < (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][
                j + 1] and matrix[i][j] < matrix[i][j - 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # first column mid line position case
            elif (h - 1) > i > 0 == j and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i + 1][
                j] and matrix[i][j] < matrix[i][j + 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # mid line, mid column position case
            elif 0 < i < (h - 1) and 0 < j < (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < \
                    matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # left down corner case
            elif i == (h - 1) and j == 0 and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # last line mid column case
            elif i == (h - 1) and 0 < j < (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                    matrix[i][j - 1] and matrix[i][j] < matrix[i][j + 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # right up corner case
            elif i == 0 and j == (l - 1) and matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # last column mid line case
            elif 0 < i < (h - 1) and j == (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                    matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
            # right down corner case
            elif i == (h - 1) and j == (l - 1) and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j - 1]:
                all_basin_size_list.append(get_basin_size(i, j, matrix))
    return all_basin_size_list


def part_1(min_nums):
    count = 0
    for num in min_nums:
        count = count + num + 1
    print(f"total:{count}")
    return count


def main():
    test_matrix = read_line("data/test.txt")
    prod_matrix = read_line("data/prod.txt")
    # print(prod_matrix)

    # part1
    # res = check_min(prod_matrix)
    # part_1(res)

    # part2
    basin_size_list = get_basin_list(test_matrix)
    print(f"size list:{basin_size_list}")


if __name__ == "__main__":
    main()
