def read_line(file_name):
    with open(file_name) as f:
        algo, img_line = f.read().split('\n\n')
        image = img_line.splitlines()
        # algo, _, *image = [line.strip() for line in f]
        print(f"algo: {algo}")
        print(f"image: {image}")
        pixels = set()
        for y, row in enumerate(image):
            for x, cell in enumerate(row):
                if cell == '#':
                    pixels.add((x, y))
        print(f"pixel: {pixels}")
    return algo, pixels


def get_neighbours(x, y):
    return [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
    ]


def get_bit(x, y, pixels, boundary, outside_on):
    if outside_on:
        return '1' if (x, y) in pixels or (x, y) not in boundary else '0'
    else:
        return '1' if (x, y) in pixels else '0'


def enhance(algorithm, pixels, outside_on=False):
    new_pixels = set()
    min_x = min([p[0] for p in pixels])
    min_y = min([p[1] for p in pixels])
    max_x = max([p[0] for p in pixels])
    max_y = max([p[1] for p in pixels])
    boundary = {
        (x, y)
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    }
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            s = ''.join([
                get_bit(x2, y2, pixels, boundary, outside_on)
                for (x2, y2) in get_neighbours(x, y)
            ])
            b = int(s, 2)
            if algorithm[b] == '#':
                new_pixels.add((x, y))
    return new_pixels


def draw_image(pixels):
    min_x = min([p[0] for p in pixels])
    min_y = min([p[1] for p in pixels])
    max_x = max([p[0] for p in pixels])
    max_y = max([p[1] for p in pixels])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in pixels:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def calculate_result(algo, pixels):
    for i in range(50):
        pixels = enhance(algo, pixels, outside_on=i % 2 == 1)
        if i == 1:
            part1 = len(pixels)
            draw_image(pixels)
    part2 = len(pixels)
    return part1, part2


def main():
    test_algo, test_pixels = read_line("data/test.txt")
    algo, pixels = read_line("data/prod.txt")
    # print(test_lines)
    # draw_image(test_pixels)
    part1, part2 = calculate_result(algo, pixels)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
