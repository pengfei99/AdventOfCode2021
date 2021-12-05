import copy
import numpy

# read the marker number file and return a list
from challenge.D05.Line import Line


def read_line(filename):
    with open(filename) as f:
        lines = []
        for line in f.readlines():
            line_text = line.strip("\n")
            # print(line_text)
            point = line_text.split("->")
            s_point = point[0].strip(" ").split(",")
            x1 = int(s_point[0])
            y1 = int(s_point[1])
            e_point = point[1].strip(" ").split(",")
            x2 = int(e_point[0])
            y2 = int(e_point[1])
            line = Line(x1, y1, x2, y2)
            lines.append(line)
            # print(f"starting point: {s_point}")
            # print(f"ending point: {e_point}")
    return lines


def get_danger_point(matrix):
    counter = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] > 1:
                counter += 1
    print(f"danger_point_count: {counter}")
    return counter


def part_1(lines, matrix_length, matrix_width):
    matrix = numpy.zeros((matrix_length, matrix_width))
    for line in lines:
        # print(line)
        matrix = line.draw_line(matrix)
        # print(matrix)
    get_danger_point(matrix)


def part_2(lines, matrix_length, matrix_width):
    matrix = numpy.zeros((matrix_length, matrix_width))
    for line in lines:
        # print(line)
        matrix = line.draw_line(matrix)
        # print(matrix)
    get_danger_point(matrix)


def main():
    test_data = "data/test.txt"
    test_lines = read_line(test_data)
    #
    prod_lines = read_line("data/prod.txt")

    # part1
    # part_1(prod_lines, 1000, 1000)

    # part2
    part_2(prod_lines, 1000, 1000)


if __name__ == "__main__":
    main()
