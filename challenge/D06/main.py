import copy

from challenge.D06.Fish import Fish


def read_fish(file_name):
    with open(file_name) as f:
        fish_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            nums = line_text.split(",")
            for num in nums:
                fish_list.append(Fish(int(num)))
    return fish_list


def part_1(fish_list, day):
    for i in range(1, day + 1):
        tmp=[]
        for fish in fish_list:
            fish.pass_day()
            if fish.ready_to_make_fish():
                new_fish = fish.make_fish()
                tmp.append(new_fish)
        for new_fish in tmp:
            fish_list.append(new_fish)
        print(f"day: {i},fish number: {len(fish_list)}")
    return fish_list


def part_2(nums, matrix):
    pass


def main():
    test_fish_list = read_fish("data/test.txt")
    print(f"test length:{len(test_fish_list)}")
    prod_fish_list = read_fish("data/prod.txt")
    # print(f"prod fish : {len(prod_fish_list)}")
    part_1(prod_fish_list, 80)


if __name__ == "__main__":
    main()
