import re

FILENAME = "raw/2024/day_3.txt"


def check_dont(text):
    do_text = ""
    dont_text = text.split("don't()")
    for itext in dont_text[1:]:
        txt = itext.split("do()")[1:]
        do_text += txt[0] if txt != [] else ""

    do_text += dont_text[0]
    return do_text


# def check_dont(text):
#     parts = re.split(r"don't\(\)|do\(\)", text)
#     enable = True
#     if re.findall(r"don't\(\)", text):
#         enable = False
#     if re.findall(r"do\(\)", text):
#         enable = True

#     matches = []
#     for part in parts:
#         if inside_dont_block:
#             inside_dont_block = False
#         else:
#             matches.extend(re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", part))
#             inside_dont_block = True

#     return sum(int(a) * int(b) for a, b in matches)


def match_text(text):
    match = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(match, text)


def get_total_uncorrupted_memory(memory):
    return sum(int(a) * int(b) for a, b in memory)


def get_corrupted_memory(FILENAME):
    with open(FILENAME, "r") as file:
        text = file.read()

    return text


def main():
    text = get_corrupted_memory(FILENAME)
    mul_inst = get_total_uncorrupted_memory(match_text(text))
    mul_enb = get_total_uncorrupted_memory(match_text(check_dont(text)))
    # mul_enb = check_dont(text)
    print(f"The uncorrupted memory mul instructions: {mul_inst}")  # Question 1
    print(
        f"The uncorrupted instructions for enabled multiplications: {mul_enb}"
    )  # Question 2
    #
    print("done")


if __name__ == "__main__":
    main()
