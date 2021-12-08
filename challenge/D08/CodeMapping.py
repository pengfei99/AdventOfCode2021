def processLine(line):
    lhs, rhs = line.split('|')
    return list(map(frozenset, lhs.split())), list(map(frozenset, rhs.split()))


# Intuition:
# 1, 4, 7, 8 all have specific lengths
# 6 has all of 5 + 1 extra
# 3 has both chars of 1
# 9 is the union of 4 and 3
# 5 has 5 chars of 6
# 0 is the only one left with 6 chars at this point
# 2 is the only number left
# We can narrow all numbers if we discover them in a specific order

rules = {
    0: lambda num, rules: len(num) == 6,
    1: lambda num, rules: len(num) == 2,
    2: lambda num, rules: num,
    3: lambda num, rules: len(num) == 5 and len(num & rules[1]) == 2,
    4: lambda num, rules: len(num) == 4,
    5: lambda num, rules: len(num) == 5 and len(num & rules[6]) == 5,
    6: lambda num, rules: len(num) == 6 and len(num & rules[1]) == 1,
    7: lambda num, rules: len(num) == 3,
    8: lambda num, rules: len(num) == 7,
    9: lambda num, rules: num == (rules[4] | rules[3])
}


def applyRule(pool, rule, lookup):
    ruleFn = rules[rule]
    return list(filter(lambda num: ruleFn(num, lookup), pool))[0]


def createLookup(lhs, ruleOrder):
    lookup = {}
    pool = set(lhs)
    for rule in ruleOrder:
        result = applyRule(pool, rule, lookup)
        lookup[rule] = result
        pool.discard(result)
    reverse = {v: k for (k, v) in lookup.items()}
    return reverse


def part1(lhs, rhs, ruleOrder):
    lookup = createLookup(lhs, ruleOrder)
    return len([lookup[r] for r in rhs if r in lookup])


def part2(lhs, rhs, ruleOrder):
    lookup = createLookup(lhs, ruleOrder)
    result = [lookup[r] for r in rhs]
    result = int(''.join(map(str, result)))
    return result


def read_line(file_name):
    with open(file_name) as f:
        r_list = []
        for line in f.readlines():
            line_text = line.strip("\n")
            r_list.append(line_text)
    return r_list


data = list(map(processLine, read_line("data/prod.txt")))

# Part 1
ruleOrder = [1, 4, 7, 8]
print(sum([part1(lhs, rhs, ruleOrder) for lhs, rhs in data]))

# Part 2
ruleOrder = [1, 4, 7, 8, 6, 3, 9, 5, 0, 2]
print(sum([part2(lhs, rhs, ruleOrder) for lhs, rhs in data]))
