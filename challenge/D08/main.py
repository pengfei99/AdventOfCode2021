# read the marker number file and return a list
from challenge.D08.Record import Record


def read_line(file_name):
    with open(file_name) as f:
        r_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            nums = line_text.split("|")
            input_str = nums[0]
            output_str = nums[1]
            r = Record(input_str, output_str)
            r_list.append(r)
    return r_list


def part_1(records):
    counter = 0
    for r in records:
        out_nums = r.get_output_nums()
        for num in out_nums:
            if len(num) in [2, 3, 4, 7]:
                counter += 1
    print(f"total is: {counter}")
    return counter


def main():
    test_records = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")

    for r in test_records:
        print(r)

    # part_1(test_records)
    part_1(prod_lines)

    base_line1 = {"cf": 1,
                 "acf": 7,
                 "bcdf": 4,
                 "acdeg": 2, "acdfg": 3, "abdfg": 5,
                 "abcefg": 0, "abdefg": 6, "abcdfg": 9,
                 "abcdefg": 8}

    base_line = {1: "cf",
                 7: "acf",
                 4: "bcdf",
                 2: "acdeg", 3: "acdfg", 5: "abdfg",
                 0: "abcefg", 6: "abdefg", 9: "abcdfg",
                 8: "abcdefg"}
    # part1
    # min_fuel, res_p = get_min_fuel_p(test_lines)
    # print(f"min_fuel : {min_fuel}, at position : {res_p}")

    # min_fuel, res_p = get_min_fuel_p(prod_lines)
    # print(f"min_fuel : {min_fuel}, at position : {res_p}")
    # part2


if __name__ == "__main__":
    main()
