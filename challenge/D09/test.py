import math
from typing import List


class Location:
    def __init__(self, value):
        self.value = value
        self.basin = None
        self.adjacent = None  # type: List[Location]
        self.is_basin_border = False if value < 9 else True


class Heightmap:
    def __init__(self, _data, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = []
        for d in _data:
            self.data.append(list(Location(int(x)) for x in list(d)))

        self.basins = []  # type: List[Location]

    def get(self, x, y):
        return self.data[y][x]

    def add_lowpoint(self, lp: Location):
        self.basins.append([lp])
        lp.basin = len(self.basins)

    def solve_basins(self):
        all_locations = [item for sublist in self.data for item in sublist]  # just flattened data list

        # spread assigned basins until all non-border locations have assigned basin value
        while len([loc for loc in all_locations if not loc.is_basin_border and not loc.basin]) > 0:
            for loc in [loc for loc in all_locations if loc.basin]:
                for adj in [adj for adj in loc.adjacent if not adj.basin]:
                    if loc.value < adj.value and not adj.is_basin_border:
                        adj.basin = loc.basin
                        self.basins[loc.basin-1].append(adj)


def determine_adjacents_and_lowpoints(_hm):
    for r_idx, row in enumerate(_hm.data):
        for c_idx, loc in enumerate(row):
            adjacent = []
            if c_idx > 0:  # left
                adjacent.append(row[c_idx-1])
            if c_idx < _hm.num_cols-1:  # right
                adjacent.append(row[c_idx+1])
            if r_idx > 0:  # top
                adjacent.append(_hm.data[r_idx-1][c_idx])
            if r_idx < _hm.num_rows-1:
                adjacent.append(_hm.data[r_idx+1][c_idx])

            loc.adjacent = adjacent

            # if is a low point
            if loc.value < min([adj.value for adj in adjacent]):
                _hm.add_lowpoint(loc)


if __name__ == '__main__':
    data = [d.strip() for d in open('data/prod.txt', 'r').readlines()]

    test = False  # make True if you wanna work on test data instead
    if test:
        data = "2199943210 3987894921 9856789892 8767896789 9899965678".split(' ')

    hm = Heightmap(data, len(data), len(data[0]))

    determine_adjacents_and_lowpoints(hm)
    hm.solve_basins()

    if test:
        # print out basin assignment for test data
        for r in hm.data:
            print([(str(l.basin) if l.basin else "*") if not l.is_basin_border else "X" for l in r])

    sizes_of_three_biggest_basins = sorted([len(b) for b in hm.basins], reverse=True)[:3]
    print(f'Puzzle2: Three largest basin sizes multiplied: >>{math.prod(sizes_of_three_biggest_basins)}<<')