
import re


def read_line(file_name):
    with open(file_name) as f:
        x_min, x_max, y_min, y_max = map(int, re.findall(r"[-\d]+", f.read()))
    return x_min, x_max, y_min, y_max


def check(vx, vy, tops, x_min, x_max, y_min, y_max):
    px, py = 0, 0
    while px <= x_max and y_min <= py:
        px, py = px + vx, py + vy
        vx, vy = max(vx - 1, 0), vy - 1
        tops.append(py)
        if x_min <= px <= x_max and y_min <= py <= y_max:
            return True


def main():
    # x_min, x_max, y_min, y_max = read_line("data/test.txt")
    x_min, x_max, y_min, y_max = read_line("data/prod.txt")
    # print(test_lines)
    print(f"x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}")
    tops = []
    hits = {(x, y) for x in range(1, x_max + 1)
            for y in range(y_min, -y_min) if check(x, y, tops, x_min, x_max, y_min, y_max)}
    print(max(tops), len(hits))


if __name__ == "__main__":
    main()
