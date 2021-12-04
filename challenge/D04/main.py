import copy


# read the marker number file and return a list
def read_num(filename):
    with open(filename) as f:
        nums = []
        for line in f.readlines():
            line_text = line.strip("\n")
            row = line_text.split(",")
            for n in row:
                if n.isnumeric():
                    nums.append(int(n))
    return nums


# redd the bingo matrix file and return a matrix (2d array)
# each cell of the matrix is a dict with key(int) as number, value(bool) as status of the number (e.g. marked or not)
def read_matrix(filename):
    with open(filename) as f:
        matrix_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            if len(line_text) > 5:
                # print(line_text)
                row = line_text.split(" ")
                int_row = []
                for n in row:
                    if n.isnumeric():
                        int_row.append({int(n): False})
                matrix_list.append(int_row)
        return matrix_list


# mark the numbers in the matrix
def mark_matrix(matrix, number):
    for row in matrix:
        for item in row:
            if number in item:
                item[number] = True
    return matrix


# at instant t (after i marking), get all successfully bingo board
def check_bingo_all(matrix):
    all_bingo = []
    for i in range(0, len(matrix), 5):
        tmp = [matrix[i], matrix[i + 1], matrix[i + 2], matrix[i + 3], matrix[i + 4]]
        if check_rows(tmp) or check_cols(tmp):
            all_bingo.append(tmp)
    return all_bingo


# at instant t (after i marking), get the first successfully bingo board
def check_bingo(matrix):
    for i in range(0, len(matrix), 5):
        tmp = [matrix[i], matrix[i + 1], matrix[i + 2], matrix[i + 3], matrix[i + 4]]
        if check_rows(tmp) or check_cols(tmp):
            return tmp
    return None


# check all rows in a matrix, if there is at least one row that are marked
def check_rows(tmp_matrix):
    for row in tmp_matrix:
        # print(f"check row: {row}")
        if check_row(row):
            return True
    return False


# check one row, if there all number are marked
def check_row(row):
    # print(f"check row: {row}")
    for item in row:
        if False in item.values():
            return False
    return True


# check all columns in a matrix, if there is at least one column where all numbers are marked
def check_cols(tmp_matrix):
    col = []
    for i in range(0, 5):
        if (False in tmp_matrix[0][i].values()) or (False in tmp_matrix[1][i].values()) or (
                False in tmp_matrix[2][i].values()) or (False in tmp_matrix[3][i].values()) or (
                False in tmp_matrix[4][i].values()):
            col.append(False)
        else:
            col.append(True)
    if True in col:
        return True
    else:
        return False


# get the sum of all unmarked number in a matrix
def sum_unmarked(matrix):
    res = 0
    for i in range(0, 5):
        for j in range(0, 5):
            curr = matrix[i][j]
            if False in curr.values():
                res = res + list(curr.keys())[0]
    print(f"sum of unmarked numbers:{res}")
    return res


def part_1(nums, matrix):
    for num in nums:
        # iterate the marker numbers, and mark all cells of the matrix
        matrix = mark_matrix(matrix, num)
        # after each marking, we check if a bingo is formed
        tmp = check_bingo(matrix)
        # if a bingo is find (first bingo), calculate the sum of the unmarked number
        # then multiple the sum with the current marker
        if tmp is not None:
            print(f"result bingo matrix: {tmp}")
            unmarked_sum = sum_unmarked(tmp)
            res = unmarked_sum * num
            print(f"current number: {num}")
            print(f"result: {res}")
            return res


def part_2(nums, matrix):
    # store all the possible bingo after finding the last possible bingo
    last_all_bingo = []
    # store the last marker number after finding the last possible bingo
    last_index = 0
    # store the number marked status of the last finding bingo. Because the next marker will destroy the status by
    # marking new numbers in the bingo, thus we can't have the right unmark number's sum
    last_bingo = None
    for num in nums:
        matrix = mark_matrix(matrix, num)
        # after mark, we find all possible bingo
        all_bingo = check_bingo_all(matrix)
        # we check the current success bingo size with previous success size
        # if current is bigger, it means we find a new successful bingo
        # - replace the last_index by the current marker number, it may be the last
        # - replace the last_bingo by the new successful bingo , it may be the last
        curr_bingo_size = len(all_bingo)
        if curr_bingo_size > len(last_all_bingo):
            last_index = num
            for bingo in all_bingo:
                if bingo not in last_all_bingo:
                    last_bingo = copy.deepcopy(bingo)
            last_all_bingo = all_bingo
    # after the iteration, use the last_index, and last_bingo to calculate the final result
    if last_bingo is not None:
        unmarked_sum = sum_unmarked(last_bingo)
        res = unmarked_sum * last_index
        print(f"last_index number: {last_index}")
        print(f"result: {res}")
        return res


def main():
    # nums = read_num("data/test_n.txt")
    # matrix = read_matrix("data/test_m.txt")
    # part_1(nums, matrix)
    # part_2(nums, matrix)

    prod_nums = read_num("data/nums.txt")
    prod_matrix = read_matrix("data/matrix.txt")
    print("PART I:")
    part_1(prod_nums, prod_matrix)
    print("PART II:")
    part_2(prod_nums, prod_matrix)


if __name__ == "__main__":
    main()
