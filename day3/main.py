"""
Author: Ferran Gonzalez Garcia
Day: 3
GitHub: https://github.com/ulidev
"""
import numpy as np


def surrounding_mask(matrix):
    rows, cols = matrix.shape
    surrounding_mask = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            if not (matrix[i, j].isdigit() or matrix[i, j] == '.'):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if 0 <= i + di < rows and 0 <= j + dj < cols:
                            surrounding_mask[i + di, j + dj] = 1
    return surrounding_mask


def create_digit_mask(matrix):
    rows, cols = matrix.shape
    digit_mask = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j].isdigit():
                digit_mask[i, j] = 1
    return digit_mask


def apply_mask(matrix, mask):
    rows, cols = matrix.shape
    masked_matrix = np.empty(matrix.shape, dtype='object')
    for i in range(rows):
        for j in range(cols):
            if mask[i, j] == 1:
                masked_matrix[i, j] = matrix[i, j]
            else:
                masked_matrix[i, j] = ''
    return masked_matrix


def sum_numbers(matrix):
    total_sum = 0
    for row in matrix:
        number = ''
        for element in row:
            if element.isdigit():
                number += element
            elif number:
                total_sum += int(number)
                number = ''
        if number:
            total_sum += int(number)
    return total_sum


def sum_gear_ratio(matrix):
    rows, cols = matrix.shape
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == '*':
                numbers_around = set()
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if not (di == 0 and dj == 0):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni, nj].isdigit():
                                start = end = nj
                                while start > 0 and matrix[ni, start - 1].isdigit():
                                    start -= 1
                                while end + 1 < cols and matrix[ni, end + 1].isdigit():
                                    end += 1

                                number = int(''.join(matrix[ni, start:end + 1]))
                                numbers_around.add(number)

                if len(numbers_around) == 2:
                    total_sum += np.prod(list(numbers_around))

    return total_sum


def part1(input_data):
    # PART 1 SOLUTION
    mat = np.array([list(row) for row in input_data])

    digit_mask = create_digit_mask(mat)
    symbol_mask = surrounding_mask(mat)

    rows, cols = digit_mask.shape
    final_mask = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            if digit_mask[i, j] == 1 and symbol_mask[i, j] == 1:
                k = j
                while k < cols and digit_mask[i, k] == 1:
                    final_mask[i, k] = 1
                    k += 1
                k = j - 1
                while k >= 0 and digit_mask[i, k] == 1:
                    final_mask[i, k] = 1
                    k -= 1

    nums = apply_mask(mat, final_mask)
    result = sum_numbers(nums)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(input_data):
    # PART 2 SOLUTION
    mat = np.array([list(row) for row in input_data])

    result = sum_gear_ratio(mat)

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    return matrix_input(raw)


def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        return file.read()


def row_input(data, separator="\n"):
    return data.strip().split(separator)


def matrix_input(data, element_sep=None, row_sep="\n"):
    return [list(row) for row in data.strip().split(row_sep)]


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
