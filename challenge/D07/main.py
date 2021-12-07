# read the marker number file and return a list
import math


def read_line(file_name):
    with open(file_name) as f:
        p_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            nums = line_text.split(",")
            for num in nums:
                p_list.append((int(num)))
    return p_list


def get_fuel_cost(p_list, destination):
    fuel_sum = 0
    for p in p_list:
        fuel = abs(p - destination)
        fuel_sum = fuel_sum + fuel
    return fuel_sum


# part I
def get_min_fuel_p1(p_list):
    min_fuel = 100000000
    min_p = min(p_list)
    max_p = max(p_list)
    res_p = 0
    for p in range(min_p, max_p + 1):
        curr_fuel = get_fuel_cost(p_list, p)
        if min_fuel > curr_fuel:
            min_fuel = curr_fuel
            res_p = p
    return min_fuel, res_p


# part II
def consecutive_sum(n: int) -> int:
    nums = range(1, n + 1)
    return sum(nums)


def get_one_crab_fuel_cost(start, end):
    steps = abs(start - end)
    fuel_cost = consecutive_sum(steps)
    return fuel_cost


def get_fuel_cost_part2(p_list, destination):
    fuel_sum = 0
    for p in p_list:
        fuel = get_one_crab_fuel_cost(p, destination)
        fuel_sum = fuel_sum + fuel
    return fuel_sum


def get_min_fuel_p2(p_list):
    min_fuel = 100000000
    min_p = min(p_list)
    max_p = max(p_list)
    res_p = 0
    for p in range(min_p, max_p + 1):
        curr_fuel = get_fuel_cost_part2(p_list, p)
        if min_fuel > curr_fuel:
            min_fuel = curr_fuel
            res_p = p
    return min_fuel, res_p


def main():
    test_lines = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")
    # print(test_lines)

    # part1
    # min_fuel, res_p = get_min_fuel_p(test_lines)
    # print(f"min_fuel : {min_fuel}, at position : {res_p}")

    # min_fuel, res_p = get_min_fuel_p(prod_lines)
    # print(f"min_fuel : {min_fuel}, at position : {res_p}")
    # part2

    min_fuel, res_p = get_min_fuel_p2(prod_lines)
    print(f"min_fuel : {min_fuel}, at position : {res_p}")


if __name__ == "__main__":
    main()
