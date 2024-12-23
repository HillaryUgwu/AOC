FILENAME = "raw/2024/day_1.txt"


def get_total_distance(loc_id):
    return sum(abs(a - b) for a, b in loc_id)


def get_similarity_score(loc_id1, loc_id2):
    sim_score = 0
    for id1 in loc_id1:
        count = 0
        for id2 in loc_id2:
            if id1 == id2:
                count += 1
        sim_score += id1 * count
    return sim_score


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
    sim_score = get_similarity_score(loc_id1, loc_id2)
    print(
        f"The total distance between the left list and the right list is {t_dist}"
    )  # Question 1
    print(
        f"The similarity score between the left list and the right list is {sim_score}"
    )  # Question 2

    print("done")


if __name__ == "__main__":
    main()
