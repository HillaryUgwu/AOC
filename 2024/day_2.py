FILENAME = "raw/2024/day_2.txt"


def check_increasing_or_decreasing(replst, n, new_replst=None, flag=False):
    new_replst = replst if not new_replst else new_replst
    increasing = all(
        (replst[i] - replst[i - 1]) in [1, 2, 3] for i in range(1, len(replst))
    )
    decreasing = all(
        (replst[i - 1] - replst[i]) in [1, 2, 3] for i in range(1, len(replst))
    )

    if increasing or decreasing:
        return 1

    if not flag or (n >= len(new_replst)):
        return 0

    reptup = tuple(new_replst)
    while True:
        n += 1
        reptuplst = list(reptup)
        reptuplst.pop(len(reptup) - n)
        return check_increasing_or_decreasing(reptuplst, n, new_replst, flag=True)


def count_safe_reports(reports, flag=False):
    safe_reps = 0
    for i, lines in enumerate(reports):
        n = 0
        reps = check_increasing_or_decreasing(lines, n, flag=flag)
        safe_reps += reps
    return safe_reps


def get_location_id(FILENAME):
    reports = []
    with open(FILENAME) as f:
        for line in f:
            lineid = line.strip("\n").split(" ")
            reports.append([int(i) for i in lineid])

    return reports


def main():
    reports = get_location_id(FILENAME)
    safe_reps = count_safe_reports(reports)
    damp = count_safe_reports(reports, flag=True)
    print(f"The total number of safe reports: {safe_reps}")  # Question 1
    print(f"The Problem Dampener number of safe reports: {damp}")  # Question 2

    print("done")


if __name__ == "__main__":
    main()
