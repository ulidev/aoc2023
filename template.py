"""
Author: Ferran Gonzalez Garcia
Day:
GitHub: https://github.com/ulidev
"""


def part1(input_data):
    result = -1
    # PART 1 SOLUTION

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(input_data):
    result = -1
    # PART 2 SOLUTION

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    return raw


def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    file = read_input()

    parsed = parse_input(file)

    part1(parsed)
    part2(parsed)
