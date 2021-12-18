# read the marker number file and return a list
import ast
import math

from challenge.D18.SnailNumber import SnailNumber


def read_line(file_name):
    with open(file_name) as f:
        snail_number_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            # use the python abstract syntax tree lib to pass the string to a list
            parsed_line = ast.literal_eval(line_text.strip())
            # print(type(parsed_line))
            # print(parsed_line)
            # print((parsed_line[0]))
            snail_number = SnailNumber.parse(parsed_line)
            snail_number_list.append(snail_number)
    return snail_number_list


# do the sum of all the snail numbers in the list one by one
def part_1(snail_number_list):
    lst = list(snail_number_list)
    i = iter(lst)
    base = next(i)
    for x in i:
        base = base + x
    return base


# brut force get the addition of any two snail numbers in the list, return the max mag of the addition
def part_2(snail_number_list):
    max_mag = 0
    for x in snail_number_list:
        for y in snail_number_list:
            if x != y:
                current_mag = (x + y).magnitude()
                if max_mag < current_mag:
                    max_mag = current_mag
    return max_mag


def main():
    test_numbers = read_line("data/test.txt")
    prod_numbers = read_line("data/prod.txt")

    # part 1, add all num in the list one by one, get the magnitude of the sum result
    res: SnailNumber = part_1(prod_numbers)
    print(res.magnitude())
    # part 2, get the max of any two number sum
    res2 = part_2(prod_numbers)
    print(f"max mag: {res2}")


if __name__ == "__main__":
    main()
