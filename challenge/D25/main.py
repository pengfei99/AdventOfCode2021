def read_line(file_name):
    with open(file_name) as f:
        p_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            nums = list(line_text)
            p_list.append(nums)
    return p_list


def move_east(arr):
    height, width = len(arr), len(arr[0])
    moves = []
    for i in range(height):
        for j in range(width):
            if arr[i][j] == '>' and arr[i][(j + 1) % width] == '.':
                moves.append((i, j, (j + 1) % width))
    for i, j, nj in moves:
        arr[i][j] = '.'
        arr[i][nj] = '>'
    return arr, bool(moves)


def move_south(arr):
    height, width = len(arr), len(arr[0])
    moves = []
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 'v' and arr[(i + 1) % height][j] == '.':
                moves.append((i, (i + 1) % height, j))
    for i, ni, j in moves:
        arr[i][j] = '.'
        arr[ni][j] = 'v'
    return arr, bool(moves)


def part_1(arr):
    res = 0
    moved = True
    while moved:
        arr, east = move_east(arr)
        arr, south = move_south(arr)
        moved = east or south
        res += 1
    return res


def main():
    test_lines = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")
    # print(test_lines)
    print(f'Part 1: {part_1(prod_lines)}')


if __name__ == "__main__":
    main()
