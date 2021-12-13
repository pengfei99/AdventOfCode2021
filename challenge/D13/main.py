# read the marker number file and return a list


def read_line(file_name):
    with open(file_name) as f:
        p_list = []
        wait_fold = True
        for line in f.readlines():
            line = line.strip("\n")
            if not line:
                wait_fold = False
            # get the raw character position of the paper
            elif wait_fold:
                p_list.append(tuple(map(int, line.split(','))))
            # get how to fold the paper
            else:
                n = []
                a, b = line.split('=')
                b = int(b)
                for x, y in p_list:
                    if a[-1] == 'x' and x > b:
                        n.append((b - (x - b), y))
                    elif a[-1] == 'y' and y > b:
                        n.append((x, b - (y - b)))
                    else:
                        n.append((x, y))
                p_list = list(set(n))
                break
    print(len(p_list))
    return p_list


def part_2(p_list):
    grid = [['.'] * 1000 for _ in range(10)]
    for x, y in p_list:
        grid[y][x] = '#'

    for row in grid:
        print(*row, sep='')


def main():
    # test_lines = read_line("data/test.txt")
    prod_list = read_line("data/prod.txt")
    print(prod_list)
    # part_2(test_lines)
    part_2(prod_list)


if __name__ == "__main__":
    main()
