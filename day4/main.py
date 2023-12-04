"""
Author: Ferran Gonzalez Garcia
Day: 4
GitHub: https://github.com/ulidev
"""
from functools import reduce


class Card:
    def __init__(self, id, winning, owned):
        self.id = id,
        self.winning = winning,
        self.owned = owned

    def part1(self):
        matches = len(self.winning[0].intersection(self.owned))
        if matches <= 1:
            return matches
        return pow(2, matches-1)

    def part2(self, n):
        matches = len(self.winning[0].intersection(self.owned))
        matching_dict = {}
        for i in range(self.id[0]+1, self.id[0]+matches+1):
            matching_dict[i] = n

        return matching_dict


def process_input(input_data):
    cards = []

    for line in input_data:
        sep = line.split(':')
        id = int(sep[0].split()[1])

        num_sep = sep[1].split(' | ')
        winning = set(num_sep[0].split())
        owned = set(num_sep[1].split())

        cards.append(Card(id, winning, owned))

    return cards


def part1(input_data):
    cards = process_input(input_data)
    result = [card.part1() for card in cards]

    result = reduce(lambda x, y: x + y, result)

    if result != -1:
        print("The solution to part one is: " + str(result))


def add_map(map1, map2):
    for k, v in map2.items():
        map1[k] = map1[k] + v

    return map1

def part2(input_data):
    how_of_each = {}
    for i in range(1,220):
        how_of_each[i] = 1

    cards = process_input(input_data)
    for card in cards:
        card_map = card.part2(how_of_each[card.id[0]])
        how_of_each = add_map(how_of_each, card_map)

    result = 0
    for value in how_of_each.values():
        result += value

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
