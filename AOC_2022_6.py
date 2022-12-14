FILENAME = "input6.txt"


def lockOnToSignal(line, packet_marker):
    for i in range(packet_marker, len(line)):
        marker = line[i - packet_marker : i]
        if len(marker) == len(set(marker)):
            return i


def tuningTrouble(FILENAME):
    packet_marker, message_marker, p_mark, m_mark = 4, 14, [], []
    with open(FILENAME) as f:
        for line in f:
            p_mark.append(lockOnToSignal(line, packet_marker))
            m_mark.append(lockOnToSignal(line, message_marker))

    return p_mark, m_mark


def main():
    p_mark, m_mark = tuningTrouble(FILENAME)
    print(
        f"A total of {p_mark} characters are processed before the first start-of-packet marker is detected"
    )  # Question 1
    print(
        f"A total of {m_mark} characters are processed before the first start-of-packet marker is detected"
    )  # Question 2

    print("done")


if __name__ == "__main__":
    main()
