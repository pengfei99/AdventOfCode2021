from collections import defaultdict


def read_line(file_name):
    neighbours = defaultdict(list)
    with open(file_name) as f:
        for line in f.readlines():
            line_text = line.strip("\n")
            items = line_text.split("-")
            print(f"a: {items[0]}, b: {items[1]}")
            neighbours[items[0]] += [items[1]]
            neighbours[items[1]] += [items[0]]
    return neighbours


def part_1(neighbours):
    queue = [['start']]
    finished = 0
    while queue:
        path = queue.pop(0)

        for next_node in neighbours[path[-1]]:
            if next_node == 'end':
                finished += 1
            elif not next_node.islower() or next_node not in path:
                queue.append(path + [next_node])
    return finished


def part_2(neighbours):
    queue = [['start']]
    finished = 0
    while queue:
        path = queue.pop(0)

        for next_node in neighbours[path[-1]]:
            is_repeat = next_node.islower() and next_node in path

            if next_node == 'end':
                finished += 1
            elif next_node != 'start' and not (path[0] == '*' and is_repeat):
                queue.append((['*'] if is_repeat else []) + path + [next_node])
    return finished

# this can do part1 and part2
def search(part, neighbours, seen=set(), cave='start'):
    if cave == 'end': return 1
    if cave in seen:
        if cave == 'start': return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(search(part, seen | {cave}, n)
               for n in neighbours[cave])


def main():
    test_neighbours = read_line("data/test.txt")
    prod_neighbours = read_line("data/prod.txt")
    part1 = part_1(prod_neighbours)
    print(f"total path number: {part1}")

    part2 = part_2(prod_neighbours)
    print(f"total path number: {part2}")


if __name__ == "__main__":
    main()
