import z3
from z3 import And, If, Int


# pip install z3-solver

def read_line(file_name):
    lst = open(file_name, 'r').read().splitlines()
    lst = [[int(y.split()[-1]) for y in [lst[i + 4], lst[i + 5], lst[i + 15]]] for i in range(0, len(lst), 18)]
    # The given input instructions in prod.txt has 14 repeat blocks of instructions.
    # Each block contains 18 instructions. Among these blocks, most of them all identical except for
    # the parameters on instructions 4, 5, and 15
    # Below is a template 18 instructions. Notice that we name the changing parameters with a in line 4, b in line 5
    # c in line 15
    # For each block, we need to extract these 3 changing parameters.
    """
    inp w
mul x 0
add x z
mod x 26
div z {a}
add x {b}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {c}
mul y x
add z y
    """
    return lst


def solve(maximize, lst):
    s = z3.Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    value = 0  # this is the value from concatenating our digits
    for (i, [p, q, r]) in enumerate(lst):
        w = Int(f'w{i}')
        value = value * 10 + w
        s.add(And(w >= 1, w <= 9))
        z = If(z % 26 + q == w, z / p, z / p * 26 + w + r)
    s.add(z == 0)
    if maximize:
        s.maximize(value)
    else:
        s.minimize(value)
    assert s.check() == z3.sat
    return s.model().eval(value)


def main():
    prod_params = read_line("data/prod.txt")
    print(prod_params)
    print(f"len: {len(prod_params)}")

    # part_1 = solve(True, prod_params)
    # print(f"part_1 result: {part_1}")

    part_2 = solve(False, prod_params)
    print(f"part_2 result: {part_2}")


if __name__ == "__main__":
    main()
