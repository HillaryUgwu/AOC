FILENAME = "raw/2024/day_2.txt"


def get_total_distance(loc_id):
    return sum(abs(a - b) for a, b in loc_id)


def check_increasing_or_decreasing(lst, flag=False):
    if all((lst[i] - lst[i - 1]) in [1, 2, 3] for i in range(1, len(lst))):
        return 1
    elif all((lst[i - 1] - lst[i]) in [1, 2, 3] for i in range(1, len(lst))):
        return 1
    if not flag:
        return 0
    check_increasing_or_decreasing(lst)


def count_safe_reports(reports, flag=False):
    safe_reps = 0
    for lines in reports:
        reps = check_increasing_or_decreasing(lines, flag)
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
    # damp = count_safe_reports(reports, True)
    print(f"The total number of safe reports: {safe_reps}")  # Question 1
    # print(f"The Problem Dampener number of safe reports: {damp}")  # Question 2

    print("done")


if __name__ == "__main__":
    main()
