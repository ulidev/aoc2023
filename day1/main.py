"""
Author: Ferran Gonzalez Garcia
Day: 1
GitHub: https://github.com/ulidev
"""


def part1(input_data):
    result = -1
    # PART 1 SOLUTION
    parsed = row_input(input_data)
    sum = 0
    for r in parsed:
        first_char = 0
        second_char = 0
        for c in r:
            if c.isdigit():
                first_char = c
                break
        for c in reversed(r):
            if c.isdigit():
                second_char = c
                break

        sum += int(first_char + second_char)

    result = sum

    # if result != -1:
    #    print("The solution to part one is: " + str(result))


def part2(input_data):
    result = -1
    # PART 2 SOLUTION
    text_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    def replace_nums(text):
        for key, value in text_to_digit.items():
            text = text.replace(key, value)
        return text

    parsed = row_input(input_data)[:5]
    res = map(replace_nums, parsed)

    sum = 0
    for row in res:
        first_char = 0
        second_char = 0
        for c in row:
            if c.isdigit():
                print(c)
                first_char = c
                break
        for c in reversed(row):
            if c.isdigit():
                print(c)
                second_char = c
                break

        sum += int(first_char + second_char)

    result = sum

    if result != -1:
        print("The solution to part two is: " + str(result))


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

    part1(file)
    part2(file)
