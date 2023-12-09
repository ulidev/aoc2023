"""
Author: Ferran Gonzalez Garcia
Day: 9
GitHub: https://github.com/ulidev
"""


def same(list):
    return len(set(list)) == 1


def get_next_value(line, part2 = False):
    last_els = []
    while not same(line):
        last_els.append(line[0]) if part2 else last_els.append(line[-1])
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]

    addition = line[0]
    for element in reversed(last_els):
        if part2:
            addition = element - addition
        else:
            addition += element

    return addition


def part1(input_data):
    result = sum([get_next_value(line) for line in input_data])
    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(input_data):
    result = sum([get_next_value(line, True) for line in input_data])

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    return [list(map(int, line.split())) for line in raw.strip().split("\n")]


def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    file = read_input()

    parsed = parse_input(file)

    part1(parsed)
    part2(parsed)
