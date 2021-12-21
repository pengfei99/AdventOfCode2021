from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product


def part_1(input_pos):
    score = [0, 0]

    die = 0
    turn = 0
    rolls = 0
    while score[0] < 1000 and score[1] < 1000:
        for r in range(3):
            die = die % 100 + 1
            input_pos[turn] += die
            rolls += 1
        input_pos[turn] = (input_pos[turn] - 1) % 10 + 1
        score[turn] += input_pos[turn]
        print(
            f"Player {turn + 1} rolls {die - 2}+{die - 1}+{die} and moves to space {input_pos[turn]} for a total score of {score[turn]}")
        turn = (turn + 1) % 2

    return min(score) * rolls


def part_2(input_pos):
    turn = 0
    universes = defaultdict(int)
    universes[(input_pos[0], input_pos[1], 0, 0)] = 1

    # Count all possible outcomes of rolling 3 3-sided dice
    possible_rolls = defaultdict(int)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                possible_rolls[d1 + d2 + d3] += 1

    # Play games in all universes at once
    in_progress = True
    while in_progress:
        in_progress = False
        next = defaultdict(int)
        for key in universes:
            p1, p2, s1, s2 = key
            if max([s1, s2]) < 21:
                in_progress = True
                for roll in possible_rolls:
                    p1, p2, s1, s2 = key
                    if turn == 0:
                        p1 = (p1 - 1 + roll) % 10 + 1
                        s1 += p1
                    else:
                        p2 = (p2 - 1 + roll) % 10 + 1
                        s2 += p2
                    next[(p1, p2, s1, s2)] += possible_rolls[roll] * universes[key]
            else:
                if universes[key]:
                    next[key] += universes[key]
        print(f"{turn + 1}. {len(next)} {sum(next.values())}")
        universes = next
        turn = (turn + 1) % 2

    win1 = sum([count for key, count in universes.items() if key[2] >= 21])
    win2 = sum([count for key, count in universes.items() if key[3] >= 21])
    print(win1, " ", win2)

    return max([win1, win2])


# def play(starting_positions, starting_scores, player, sumcounts):
#     wins = [0, 0]
#
#     for sum_throw, universes in sumcounts.items():
#         positions = list(starting_positions)
#         scores = list(starting_scores)
#
#         positions[player] = (positions[player] + sum_throw - 1) % 10 + 1
#         scores[player] += positions[player]
#
#         if scores[player] >= 21:
#             wins[player] += universes
#         else:
#             deepwins = play(tuple(positions), tuple(scores), (player + 1) % 2, sumcounts)
#             for i in range(2):
#                 wins[i] += deepwins[i] * universes
#
#     return wins
#
#
# def part_2_recursive(starting_pos):
#     sumcounts = Counter(sum(t) for t in product([1, 2, 3], repeat=3))
#     wins = play(starting_pos, (0, 0), 0, sumcounts)
#     return wins


def main():
    test = [4, 8]
    prod = [5, 9]

    # note part 1 modifies the value in prod, so use a copy to avoid interference with part 2.
    part1_res = part_1(prod.copy())
    print(f"part_1 result: {part1_res}")
    print(f"prod after part1: {prod}")

    # part2_res = part2(tuple(prod))
    # print(f"part_2 result: {part2_res}")
    part2_ite=part_2(prod)
    print(f"part_2 result: {part2_ite}")


if __name__ == "__main__":
    main()
