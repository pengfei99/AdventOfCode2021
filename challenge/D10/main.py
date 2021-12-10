# read the marker number file and return a list
import math


def read_line(file_name):
    with open(file_name) as f:
        lines = []
        for line in f.readlines():
            line_text = line.strip("\n")
            lines.append(line_text)
    return lines


scores = {
    ')': (3, 1),
    ']': (57, 2),
    '}': (1197, 3),
    '>': (25137, 4),
}


def parse_line(line):
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line:
        if c in chunks:
            stack.append(chunks[c])
        elif c == stack[-1]:
            stack.pop()
        else:
            return scores[c][0], stack
    return 0, stack


def solve(lines):
    total = 0
    totals = []
    for line in lines:
        score, stack = parse_line(line)
        if score:
            total += score
        else:
            while stack:
                score = 5 * score + scores[stack.pop()][1]
            totals.append(score)
    mid = sorted(totals)[len(totals) // 2]
    return total, mid


def main():
    test_lines = read_line("data/test.txt")
    prod_lines = read_line("data/prod.txt")
    # print(test_lines)
    total,mid=solve(prod_lines)
    print(f"Total score is: {total}, mid is: {mid}")



if __name__ == "__main__":
    main()
