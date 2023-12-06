"""
Author: Ferran Gonzalez Garcia
Day: 6
GitHub: https://github.com/ulidev
"""
from functools import reduce


def get_distance(pressed, total_time):
    speed = pressed
    total_time -= pressed
    return speed * total_time


def find_record_point(init, final, target, total_time):  # 0,15,9
    middle_point = int((init + final) / 2)
    distance_travelled = get_distance(middle_point, total_time)
    if init == final:
        return init
    if distance_travelled <= target:
        return find_record_point(middle_point + 1, final, target, total_time)
    return find_record_point(init, middle_point, target, total_time)


def part1(input_data):
    result = -1
    factors = []
    # PART 1 SOLUTION
    for time, distance in input_data:
        total_time = time
        is_odd = True if time % 2 != 0 else False
        time = int(time / 2) + 1
        record_point = find_record_point(1, time, distance, total_time)
        n_correct = (time - record_point) * 2
        if not is_odd: n_correct -= 1
        factors.append(n_correct)

    result = reduce(lambda x, y: x * y, factors)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2_parse(raw):
    data = raw.strip().split('\n')
    data = [line.split(':')[1].split() for line in data]
    data = [int(reduce(lambda x, y: x+y, line)) for line in data]
    return data

def part2(input_data):
    result = -1
    # PART 2 SOLUTION
    time, distance = input_data

    total_time = time
    is_odd = True if time % 2 != 0 else False
    time = int(time / 2) + 1
    record_point = find_record_point(1, time, distance, total_time)
    n_correct = (time - record_point) * 2
    if not is_odd: n_correct -= 1

    result = n_correct

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    data = raw.strip().split('\n')
    data = [line.split(':')[1].split() for line in data]
    data = [(int(data[0][i]), int(data[1][i])) for i in range(len(data[0]))]
    return data


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

    parsed1 = parse_input(file)
    parsed2 = part2_parse(file)

    part1(parsed1)
    part2(parsed2)
