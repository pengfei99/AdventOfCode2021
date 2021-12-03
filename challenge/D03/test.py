import numpy as np


def readInput3(filename):
    with open(filename) as f:
        nums=[]
        for l in f.readlines():
            # strip removes an character from both left and right of a string
            num = l.strip("\n")
            int_num=[]
            for n in num:
                int_num.append(int(n))
            nums.append(int_num)
        print(nums)
        return np.array(nums)
        # return np.array([[int(n) for n in list(l.strip("\n"))] for l in f.readlines()])


def part_2(li):
    i = 0
    l = np.copy(li)
    while True:
        b = [int(sum(r) >= len(r) - sum(r)) for r in np.flipud(np.rot90(l))]
        l = np.array([list(r) for r in l if r[i] == b[i]])
        if (len(l) == 1):
            break
        i += 1
    oxy = int("".join([str(i) for i in l[0]]), 2)
    i = 0
    l = np.copy(li)
    while True:
        b = [int(sum(r) < len(r) - sum(r)) for r in np.flipud(np.rot90(l))]
        l = np.array([list(r) for r in l if r[i] == b[i]])
        if (len(l) == 1):
            break
        i += 1
    CO2 = int("".join([str(i) for i in l[0]]), 2)
    print(f"oxy:{oxy}")
    print(f"co2:{CO2}")
    return oxy * CO2


def main():
    l = readInput3("data/number.csv")
    print("total: "+str(part_2(l)))


if __name__ == "__main__":
    main()
