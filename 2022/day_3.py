import numpy as np
from string import ascii_letters
import textwrap


FILENAME = "input3.txt"


def commonBadge(rucksack):
    first, second, third = rucksack
    item_type = [
        i
        for i in set(first)
        for j in set(second)
        if i == j
        for k in set(third)
        if i == k
    ]
    return item_type.pop() if len(item_type) == 1 else print("Too many matching items")


def commonItem(rucksack):
    if len(rucksack) % 2 != 0:
        first, second = textwrap.wrap(rucksack, int(len(rucksack) / 2))
        item_type = [i for i in set(first) for j in set(second) if i == j]
        return (
            item_type.pop() if len(item_type) == 1 else print("Too many matching items")
        )
    else:
        print("Wrong input. Character length not even")


def getPriority(item_type):
    priority = [i + 1 for i, letter in enumerate(ascii_letters) if letter == item_type]
    return priority


def rucksackReorganization(FILENAME):
    total = []
    with open(FILENAME) as f:
        for line in f:
            item_type = commonItem(line)
            priority = getPriority(item_type)
            total.append(priority)

    return np.sum(total)


def groupBadges(FILENAME):
    total, rusckack = [], []
    with open(FILENAME) as f:
        for i, line in enumerate(f):
            rusckack.append(line.strip("\n"))
            if (i + 1) % 3 == 0:
                item_type = commonBadge(rusckack)
                priority = getPriority(item_type)
                total.append(priority)
                rusckack = []

    return np.sum(total)


def main():
    p_total = rucksackReorganization(FILENAME)
    print(f"The sum of the priorities of all the item types is {p_total}")  # Question 1
    g_total = groupBadges(FILENAME)
    print(f"The sum of the priorities of all the item types is {g_total}")  # Question 2

    print("done")


if __name__ == "__main__":
    main()
