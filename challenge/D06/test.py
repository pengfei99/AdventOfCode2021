from collections import defaultdict


def read_fish(file_name):
    with open(file_name) as f:
        fish_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            nums = line_text.split(",")
            for num in nums:
                fish_list.append(int(num))
    return fish_list


fishList = read_fish("data/prod.txt")
fish_population = defaultdict(lambda: 0)
print(f"fish population: {fish_population}")

for f in fishList:
    fish_population[f] += 1

days = 256

for i in range(0, days):
    new_population = defaultdict(lambda: 0)

    for k, v in fish_population.items():
        if k == 0:
            new_population[6] += v
            new_population[8] += v
        else:
            new_population[k - 1] += v
            fish_population = new_population

fish = 0

for k, v in fish_population.items():
    fish += v

print(fish)
