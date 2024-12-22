FILENAME = "raw/2024/day_1/input.txt"


def get_total_distance(loc_id):
    return sum(abs(a - b) for a, b in loc_id)


def get_location_id(FILENAME):
    loc1, loc2 = [], []
    with open(FILENAME) as f:
        for line in f:
            lineid = line.strip("\n").split("  ")
            loc1.append(int(lineid[0]))
            loc2.append(int(lineid[1]))

    return loc1, loc2


def main():
    loc_id1, loc_id2 = get_location_id(FILENAME)
    loc_id1.sort()
    loc_id2.sort()
    t_dist = get_total_distance(zip(loc_id1, loc_id2))
    print(
        f"The total distance between the left list and the right list is {t_dist}"
    )  # Question 1

    print("done")


if __name__ == "__main__":
    main()
