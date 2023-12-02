"""
Author: Ferran Gonzalez Garcia
Day: 2
GitHub: https://github.com/ulidev
"""

from functools import reduce

def part1(input_data):
    result = -1
    # PART 1 SOLUTION
    sum_ids = 0

    tolerance = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    ids = []

    for game in input_data:
        split = game.split(':')
        id = int(split[0].split()[1])

        sets = split[1].split(';')

        is_valid = True

        for game_set in sets:
            if not is_valid:
                break
            for pair in game_set.split(','):
                if not is_valid:
                    break
                number, color = pair.split()
                if tolerance[color] < int(number):
                    is_valid = False

        if is_valid: ids.append(id)

    result = sum(ids)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(input_data):
    result = -1
    # PART 2 SOLUTION

    product = 0

    for game in input_data:
        min_n = {"red": 0, "blue": 0, "green": 0}

        sets = game.split(':')[1].split(';')
        for game_set in sets:  # Aqui tindrem (), (), ()
            for pair in game_set.split(','):  # Aqui tindrem (,)
                number, color = pair.split()
                min_n[color] = max(int(number), min_n[color])

        values = min_n.values()
        product += reduce(lambda x, y: x*y, values)

    result = product

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
