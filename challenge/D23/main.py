# read the marker number file and return a list
import heapq
import math

import typing
from pprint import pprint

T = typing.TypeVar("T")

TARGET = r"""#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
"""

WAITING_AREAS = [
    (1, x)
    for x in [1, 2, 4, 6, 8, 10, 11]
]

WAITING_COLS = [1, 2, 4, 6, 8, 10, 11]
ROOM_COLS = [3, 5, 7, 9]

WAITING_ROW = 1

COST = {"A": 1, "B": 10, "C": 100, "D": 1000}


def read_line(file_name):
    with open(file_name) as f:
        content = ""
        for line in f.readlines():
            content += line
    return content


# region Strings, lists, dicts
def lmap(func, *iterables):
    return list(map(func, *iterables))


def part_1(input_str: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k):
        sample and print(*a, **k)

    lines: typing.List[str] = input_str.splitlines()
    paras: typing.List[typing.List[str]] = lmap(str.splitlines, input_str.split("\n\n"))
    out = 0

    FINAL_NODE = tuple()

    COST = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def expand(node):
        # (weight, node)
        out = []

        # node should store waiting areas + rooms
        cur_waitings, cur_rooms = node

        # waitings is a list of None or string
        if cur_rooms == (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")):
            return [(0, FINAL_NODE)]

        for i, room in enumerate(cur_rooms):
            # find the thing to move
            # sprint(room)
            first, second = room
            if first == "":
                if second == "":
                    continue
                else:
                    to_move = second
                    to_move_coord = (3, ROOM_COLS[i])
                    room_idx = 1
            else:
                to_move = first
                to_move_coord = (2, ROOM_COLS[i])
                room_idx = 0
            for j, waiting_area in enumerate(WAITING_AREAS):
                if cur_waitings[j] == "":
                    # CHECK IF BLOCKED OFF.
                    c1, c2 = waiting_area[1], to_move_coord[1]
                    if c1 > c2:
                        c1, c2 = c2, c1
                    bad = False
                    for col in range(c1 + 1, c2):
                        if col in WAITING_COLS and cur_waitings[WAITING_COLS.index(col)] != "":
                            bad = True
                            break
                    if bad:
                        continue

                    # have this person move over there
                    new_waitings = list(cur_waitings)
                    new_rooms = lmap(list, cur_rooms)

                    cost = pdist1(to_move_coord, waiting_area) * COST[to_move]
                    new_waitings[j] = to_move
                    new_rooms[i][room_idx] = ""
                    out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        # move from waiting to room
        for j, waiting_area in enumerate(WAITING_AREAS):
            to_move = cur_waitings[j]
            if to_move == "":
                continue
            target_room = ord(to_move) - ord('A')
            target_room_actual = cur_rooms[target_room]
            # first, then second
            if target_room_actual[0] == "" and (target_room_actual[1] == "" or target_room_actual[1] == to_move):
                # move in
                col = ROOM_COLS[target_room]
                if target_room_actual[1] == "":
                    # move to second
                    row = 3
                    room_idx = 1
                else:
                    row = 2
                    room_idx = 0

                # CHECK IF BLOCKED OFF.
                c1, c2 = waiting_area[1], col
                if c1 > c2:
                    c1, c2 = c2, c1
                bad = False
                for col2 in range(c1 + 1, c2):
                    if col2 in WAITING_COLS and cur_waitings[WAITING_COLS.index(col2)] != "":
                        bad = True
                        break
                if bad:
                    continue

                cost = pdist1((row, col), waiting_area) * COST[to_move]

                new_waitings = list(cur_waitings)
                new_rooms = lmap(list, cur_rooms)

                new_waitings[j] = ""
                new_rooms[target_room][room_idx] = to_move
                # out.append((cost, (new_waitings, new_rooms)))
                out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        return out

    # extract words
    rooms = []
    for room_col in ROOM_COLS:
        rooms.append(tuple(lines[row][room_col] for row in [2, 3]))
    rooms = tuple(rooms)
    print(rooms)
    waitings = ("",) * len(WAITING_AREAS)

    out, path = a_star((waitings, rooms), expand, FINAL_NODE)
    for p in path:
        pprint(p)

    if out:
        print(f"part 1 result: {out}")
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


def psub(x, y):
    return [a - b for a, b in zip(x, y)]


def pdist1(x, y=None):
    if y is not None: x = psub(x, y)
    return sum(map(abs, x))


def a_star(
        from_node: T,
        expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
        to_node: T,
        heuristic: typing.Optional[typing.Callable[[T], int]] = None,
) -> typing.Tuple[int, typing.List[T]]:
    """
    expand should return an iterable of (dist, successor node) tuples.
    Returns (distance, path).
    """
    g_values, parents = dijkstra(from_node, to_node=to_node, expand=expand, heuristic=heuristic)
    if to_node not in g_values:
        raise Exception("couldn't reach to_node")
    return (g_values[to_node], path_from_parents(parents, to_node))


def path_from_parents(parents: typing.Dict[T, T], end: T) -> typing.List[T]:
    out = [end]
    while out[-1] in parents:
        out.append(parents[out[-1]])
    out.reverse()
    return out


def dijkstra(
        from_node: T,
        expand: typing.Callable[[T], typing.Iterable[typing.Tuple[int, T]]],
        to_node: typing.Optional[T] = None,
        heuristic: typing.Optional[typing.Callable[[T], int]] = None,
) -> typing.Tuple[typing.Dict[T, int], typing.Dict[T, T]]:
    """
    expand should return an iterable of (dist, successor node) tuples.
    Returns (distances, parents).
    Use path_from_parents(parents, node) to get a path.
    """
    if heuristic is None:
        heuristic = lambda _: 0
    seen = set()  # type: typing.Set[T]
    g_values = {from_node: 0}  # type: typing.Dict[T, int]
    parents = {}  # type: typing.Dict[T, T]

    # (f, g, n)
    todo = [(0 + heuristic(from_node), 0, from_node)]  # type: typing.List[typing.Tuple[int, int, T]]

    while todo:
        f, g, node = heapq.heappop(todo)

        assert node in g_values
        assert g_values[node] <= g

        if node in seen:
            continue

        assert g_values[node] == g
        if to_node is not None and node == to_node:
            break
        seen.add(node)

        for cost, new_node in expand(node):
            new_g = g + cost
            if new_node not in g_values or new_g < g_values[new_node]:
                parents[new_node] = node
                g_values[new_node] = new_g
                heapq.heappush(todo, (new_g + heuristic(new_node), new_g, new_node))

    return (g_values, parents)


def part_2(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k):
        sample and print(*a, **k)

    lines: typing.List[str] = inp.splitlines()
    out = 0

    FINAL_NODE = tuple()

    def expand(node):
        # (weight, node)
        out = []

        # I wrote this line of code first before doing anything else
        # with the problem. It's good to know your search space!
        cur_waitings, cur_rooms = node

        if all(all(chr(ord('A') + i) == x for x in room) for i, room in enumerate(cur_rooms)):
            return [(0, FINAL_NODE)]

        def is_blocked(col_1, col_2):
            if col_1 > col_2:
                col_1, col_2 = col_2, col_1
            for blocked_col in range(col_1 + 1, col_2):
                # This could really be improved...
                if blocked_col in WAITING_COLS and cur_waitings[WAITING_COLS.index(blocked_col)] != "":
                    return True
            return False

        # Move from a room to a waiting spot.
        for room_idx, room in enumerate(cur_rooms):
            # The below uses the fact that:
            # - loop variables are still in-scope after the loop is finished, and
            # - you can add an "else" to a for loop which is run if it's not `break`ed from.
            for room_position, to_move in enumerate(room):
                if to_move == "":
                    continue
                to_move_row = 2 + room_position
                break
            else:
                continue
            for waiting_idx, waiting_col in enumerate(WAITING_COLS):
                if cur_waitings[waiting_idx] == "":
                    if is_blocked(waiting_col, ROOM_COLS[room_idx]):
                        continue

                    new_waitings = list(cur_waitings)
                    new_rooms = list(map(list, cur_rooms))

                    # To get the cost of moving, I used the Manhattan distance
                    # between the source and destination as it should always work
                    # for this with a single corridor.
                    # If the corridor was expanded, this wouldn't be as simple...
                    cost = pdist1((to_move_row, ROOM_COLS[room_idx]), (WAITING_ROW, waiting_col)) * COST[to_move]
                    new_waitings[waiting_idx] = to_move
                    new_rooms[room_idx][room_position] = ""
                    out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        # Move from a waiting spot to a room.
        for waiting_idx, waiting_col in enumerate(WAITING_COLS):
            to_move = cur_waitings[waiting_idx]
            if to_move == "":
                continue

            target_room_idx = ord(to_move) - ord('A')
            target_room = cur_rooms[target_room_idx]

            if target_room[0] == "" and all(x == "" or x == to_move for x in target_room[1:]):
                for room_position in range(len(target_room))[::-1]:
                    if target_room[room_position] != "":
                        continue
                    room_row = room_position + 2
                    break
                else:
                    assert False

                room_col = ROOM_COLS[target_room_idx]
                if is_blocked(waiting_col, room_col):
                    continue

                cost = pdist1((room_row, room_col), (WAITING_ROW, waiting_col)) * COST[to_move]

                new_waitings = list(cur_waitings)
                new_rooms = list(map(list, cur_rooms))

                new_waitings[waiting_idx] = ""
                new_rooms[target_room_idx][room_position] = to_move
                out.append((cost, (tuple(new_waitings), tuple(map(tuple, new_rooms)))))

        return out

    rooms = []
    PART2 = ["DD", "CB", "BA", "AC"]
    for i, room_col in enumerate(ROOM_COLS):
        a, b = [lines[row][room_col] for row in [2, 3]]

        rooms.append(tuple(a + PART2[i] + b))
        # Replace the above with the below for part 1.
        # This also came in handy for testing my generalised part 2 code
        # to make sure that it works with part 1.
        # rooms.append(tuple(a+b))
    rooms = tuple(rooms)
    print(rooms)
    waitings = ("",) * len(WAITING_COLS)

    # "A*" here is actually "Dijkstra, with a target node".
    # My internal implementation also returns a path from start to finish,
    # but I don't use it here.
    out, _ = a_star((waitings, rooms), expand, FINAL_NODE)

    if out:
        print(f"part 2 result : {out}")
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


def main():
    test_lines = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")
    print(prod_lines)
    part_1(prod_lines)
    part_2(prod_lines)


def show_r_string_example():
    # r"" means raw string
    r1 = r"\n"
    r2 = r"\t"
    print(f"r1 : {r1}, r2 : {r2}")


if __name__ == "__main__":
    main()
