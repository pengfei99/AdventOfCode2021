from collections import defaultdict


def read_line(file_name):
    with open(file_name) as f:
        rule_dict = {}
        wait_rule = True
        for line in f.readlines():
            line = line.strip("\n")
            if not line:
                wait_rule = False
                # get the raw character position of the paper
            elif wait_rule:
                poly = line
            # get the init position
            else:
                key, val = line.split(' -> ')
                rule_dict[key] = val
    return poly, rule_dict


def polymer_counts(polymer):
    elem_count = defaultdict(int)
    pair_count = defaultdict(int)

    for i in range(len(polymer) - 1):
        elem_count[polymer[i]] += 1
        pair_count[polymer[i:i + 2]] += 1
    elem_count[polymer[-1]] += 1

    return elem_count, pair_count


def insert_pairs(pairs):
    for pair, count in pair_count.copy().items():
        pair_count[pair] -= count
        add = pairs[pair]
        elem_count[add] += count
        pair_count[pair[0] + add] += count
        pair_count[add + pair[1]] += count


elem_count, pair_count = polymer_counts(polymer)

for i in range(40):
    insert_pairs()

print(max(elem_count.values()) - min(elem_count.values()))


def main():
    poly, rule_lines = read_line("data/test.txt")
    # prod_lines = read_line("data/prod.txt")

    print(f"poly:{poly}, rule_lines:{rule_lines}")


if __name__ == "__main__":
    main()
