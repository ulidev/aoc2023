"""
Author: Ferran Gonzalez Garcia
Day: 7
GitHub: https://github.com/ulidev
"""

from collections import Counter
from functools import reduce

char_to_num = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def part2_hand_type(hand):
    c = Counter(hand)
    if c["J"] == 5: return 7
    js = c.pop("J", 0)
    c_sorted = sorted(c.values(), reverse=True)
    c_sorted[-1] += js

    if len(c_sorted) == 1:
        return 7

    if len(c_sorted) == 2:
        if c_sorted[0] == 4:
            return 6
        return 5

    if len(c_sorted) == 3:
        if c_sorted[0] == 3:
            return 4
        return 3

    if len(c_sorted) == 4:
        return 2

    return 1

def get_hand_type(hand):
    c = Counter(hand)
    c_sorted = sorted(c.values(), reverse=True)

    if len(c_sorted) == 1:
        return 7

    if len(c_sorted) == 2:
        if c_sorted[0] == 4:
            return 6
        return 5

    if len(c_sorted) == 3:
        if c_sorted[0] == 3:
            return 4
        return 3

    if len(c_sorted) == 4:
        return 2

    return 1


def to_value(char):
    if char.isdigit():
        return int(char)
    return char_to_num[char]


def part2_to_value(char):
    return to_value(char) if char != "J" else 1


def part1(input_data):
    result = 0
    input_data = [line.split() for line in input_data]

    acc = []
    # PART 1 SOLUTION
    for (hand, bid) in input_data:
        hand_type = get_hand_type(hand)
        values = map(to_value, hand)
        acc.append((hand_type, *values, int(bid)))

    acc = sorted(acc)
    result = sum((i * h[-1]) for i, h in enumerate(acc, 1))

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(input_data):
    result = -1
    # PART 2 SOLUTION
    input_data = [line.split() for line in input_data]

    acc = []
    # PART 1 SOLUTION
    for (hand, bid) in input_data:
        hand_type = part2_hand_type(hand)
        values = map(part2_to_value, hand)
        acc.append((hand_type, *values, int(bid)))

    acc = sorted(acc)
    result = sum((i * h[-1]) for i, h in enumerate(acc, 1))

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    return row_input(raw)


def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        return file.read()


def row_input(data, separator="\n"):
    return data.strip().split(separator)


def matrix_input(data, element_sep=None, row_sep="\n"):
    rows = row_input(data, row_sep)
    return [row.split() if element_sep is None else row.split(element_sep) for row in rows]


def multi_row_input(data, separator="\n"):
    return [row_input(block, separator) for block in data.strip().split("\n\n")]


def multi_matrix_input(data, element_sep=None, row_sep="\n"):
    matrices = data.strip().split(row_sep)
    return [matrix_input(matrix, element_sep, row_sep) for matrix in matrices]


if __name__ == "__main__":
    file = read_input()

    parsed = parse_input(file)

    part1(parsed)
    part2(parsed)
