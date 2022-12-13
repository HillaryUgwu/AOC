import numpy as np


FILENAME = "input4.txt"


def fullyContains(a, b, c, d):
    ab = set(np.linspace(a, b, b - a + 1))
    cd = set(np.linspace(c, d, d - c + 1))
    overlap = ab.intersection(cd)
    overlap1 = True if overlap == ab or overlap == cd else False
    overlap2 = True if overlap else False
    return overlap1, overlap2


def campCleanup(FILENAME):
    total1, total2 = 0, 0
    with open(FILENAME) as f:
        for line in f:
            ab, cd = line.strip("\n").split(",")
            a, b = ab.split("-")
            c, d = cd.split("-")
            overlap1, overlap2 = fullyContains(int(a), int(b), int(c), int(d))
            if overlap1:
                total1 += 1
            if overlap2:
                total2 += 1

    return total1, total2


def main():
    r_total, f_total = campCleanup(FILENAME)
    print(f"The assignment pairs ranges fully overlap {r_total} times")  # Question 1
    print(f"The assignment pairs ranges overlap at all {f_total} times")  # Question 2

    print("done")


if __name__ == "__main__":
    main()
