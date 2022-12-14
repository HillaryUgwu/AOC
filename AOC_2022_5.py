import numpy as np
from collections import deque


FILENAME = "input5.txt"


def initializeCargo():
    with open(FILENAME) as f:
        n = round(len(f.readline().strip("\n")) / 4)
    cargo = dict(zip(range(1, n + 1), [deque([]) for _ in range(1, n + 1)]))
    return cargo


def stackedCargos(cargo, line):
    for stack, crate in enumerate(line.strip("\n")):
        if crate.strip(" ") and not crate.isdigit() and (stack - 1) % 4 == 0:
            cargo[(round(stack / 4) + 1)].appendleft(crate)

    return cargo


def rearrangeCrates(cargo, line):
    if line.strip("\n"):
        a, b, c = [int(s) for s in line.split() if s.isdigit()]
        [cargo[c].append(cargo[b].pop()) for _ in range(a)]
    return cargo


def rearrangeMultipleCrates(cargo, line):
    l = []
    if line.strip("\n"):
        a, b, c = [int(s) for s in line.split() if s.isdigit()]
        [l.append(cargo[b].pop()) for _ in range(a)]
        [cargo[c].append(l.pop()) for _ in range(a)]

    return cargo


def topMostCrates(cargo):
    top_crate = ""
    for keys in cargo:
        top_crate += cargo[keys].pop()

    return top_crate


def getCrateStacks(FILENAME):
    s_cargo = initializeCargo()
    m_cargo = initializeCargo()
    rearrange = False
    with open(FILENAME) as f:
        for line in f:
            if line == "\n":
                rearrange = True

            if not rearrange:
                s_cargo = stackedCargos(s_cargo, line)
                m_cargo = stackedCargos(m_cargo, line)

            else:
                s_cargo = rearrangeCrates(s_cargo, line)
                m_cargo = rearrangeMultipleCrates(m_cargo, line)

    top_crate = topMostCrates(s_cargo)
    m_top_crate = topMostCrates(m_cargo)

    return top_crate, m_top_crate


def main():
    top_crate, m_top_crate = getCrateStacks(FILENAME)
    print(
        f"The top crates of each stack after the rearrangement procedure are {top_crate}"
    )  # Question 1
    print(
        f"The top crates of each stack after the rearrangement procedure are {m_top_crate}"
    )  # Question 2

    print("done")


if __name__ == "__main__":
    main()
