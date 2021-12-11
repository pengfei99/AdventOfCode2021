# read the marker number file and return a list
import math


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


# # upper line
# matrix[i - 1][j - 1] += 1
# matrix[i - 1][j] += 1
# matrix[i - 1][j + 1] += 1
#

# increase_point(i, j, matrix)

# # mid line
# matrix[i][j - 1] += 1
# matrix[i][j + 1] += 1

# increase_point(i, j - 1, matrix)
# increase_point(i, j + 1, matrix)
#
# # lower line
# matrix[i + 1][j - 1] += 1
# matrix[i + 1][j] += 1
# matrix[i + 1][j + 1] += 1
# left up corner case
def increase_point(i, j, matrix):
    if matrix[i][j] > 0:
        matrix[i][j] += 1


def increase_adj(i, j, matrix):
    h = len(matrix)
    l = len(matrix[0])
    if i == 0 and j == 0:
        increase_point(i, j + 1, matrix)
        increase_point(i + 1, j, matrix)
        increase_point(i + 1, j + 1, matrix)
    # first line mid column position case
    elif i == 0 and 0 < j < (l - 1):
        increase_point(i, j - 1, matrix)
        increase_point(i, j + 1, matrix)
        increase_point(i + 1, j - 1, matrix)
        increase_point(i + 1, j, matrix)
        increase_point(i + 1, j + 1, matrix)
    # first column mid line position case
    elif (h - 1) > i > 0 == j:
        increase_point(i - 1, j, matrix)
        increase_point(i - 1, j + 1, matrix)
        increase_point(i, j + 1, matrix)
        increase_point(i + 1, j, matrix)
        increase_point(i + 1, j + 1, matrix)


    # mid line, mid column position case
    elif 0 < i < (h - 1) and 0 < j < (l - 1):
        increase_point(i - 1, j - 1, matrix)
        increase_point(i - 1, j, matrix)
        increase_point(i - 1, j + 1, matrix)
        increase_point(i, j - 1, matrix)
        increase_point(i, j + 1, matrix)
        increase_point(i - 1, j - 1, matrix)
        increase_point(i - 1, j, matrix)
        increase_point(i - 1, j + 1, matrix)
    # left down corner case
    elif i == (h - 1) and j == 0:
        increase_point(i - 1, j, matrix)
        increase_point(i - 1, j + 1, matrix)
        increase_point(i, j + 1, matrix)

        # last line mid column case
    elif i == (h - 1) and 0 < j < (l - 1):
        increase_point(i - 1, j - 1, matrix)
        increase_point(i - 1, j, matrix)
        increase_point(i - 1, j + 1, matrix)
        increase_point(i, j - 1, matrix)
        increase_point(i, j + 1, matrix)


    # right up corner case
    elif i == 0 and j == (l - 1):
        increase_point(i, j - 1, matrix)
        increase_point(i + 1, j - 1, matrix)
        increase_point(i + 1, j, matrix)


    # last column mid line case
    elif 0 < i < (h - 1) and j == (l - 1):
        increase_point(i - 1, j - 1, matrix)
        increase_point(i - 1, j, matrix)
        increase_point(i, j - 1, matrix)
        increase_point(i + 1, j - 1, matrix)
        increase_point(i + 1, j, matrix)

    # right down corner case
    elif i == (h - 1) and j == (l - 1):
        increase_point(i - 1, j - 1, matrix)
        increase_point(i - 1, j, matrix)
        increase_point(i, j - 1, matrix)


def pass_day(matrix):
    h = len(matrix)
    l = len(matrix[0])
    flash_count = 0
    # increce
    for i in range(h):
        for j in range(l):
            matrix[i][j] += 1
    # check light,
    # - if value==0 don't increase,
    # - if value > 9, reset to 0, counter+=1, increase all adjason point, set has flash to true
    has_flash = True
    while has_flash:
        # set has_flash to False
        has_flash = False
        for i in range(h):
            for j in range(l):
                if matrix[i][j] > 9:
                    flash_count += 1
                    matrix[i][j] = 0
                    increase_adj(i, j, matrix)
                    has_flash = True
    print(f"flash count: {flash_count}")
    return flash_count


def part_1(day, matrix):
    flash_count = 0
    for i in range(0, day):
        flash_count += pass_day(matrix)
    print(f"Total flash count: {flash_count}")


def main():
    test_matrix = read_line("data/test.txt")
    # prod_lines = read_line("data/prod.txt")
    part_1(2, test_matrix)


if __name__ == "__main__":
    main()
