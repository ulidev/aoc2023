"""
Author: Ferran Gonzalez Garcia
Day: 5
GitHub: https://github.com/ulidev
"""
import sys

MAX_INT = sys.maxsize


def special_input(raw):
    data = raw.strip().split('\n\n')
    seeds = [int(element) for element in data[0].split(':')[1].split()]
    return seeds, [[el.split() for el in line.split('\n')[1:]] for line in data[1:]]


def create_maps(map_values):
    maps = []
    for m in map_values:
        new_map = {}
        for entry in m:
            destination = int(entry[0])
            origin = int(entry[1])
            rng = int(entry[2])
            new_map[(origin, origin + rng)] = destination - origin
        maps.append(new_map)

    return maps


def next_destination(origin, map):
    for key, value in map.items():
        if key[0] <= origin < key[1]:
            return origin + value

    return origin


def part1(input_data):
    result = -1
    # PART 1 SOLUTION
    # print(input_data)
    seeds, map_values = special_input(input_data)

    maps = create_maps(map_values)
    result = MAX_INT
    for seed in seeds:
        destination = seed
        for map in maps:
            destination = next_destination(destination, map)
        result = min(result, destination)

    if result != -1:
        print("The solution to part one is: " + str(result))


def get_seed_ranges(original_seeds):
    joined = [(original_seeds[i], original_seeds[i + 1]) for i in range(0, len(original_seeds), 2)]
    return [(j[0], j[0] + j[1]) for j in joined]



def next_destination_range(rng, map):
    lowest_rng = rng[0]
    highest_rng = rng[1]

    return_ranges = []
    finished = False
    for key, value in map.items():
        lowest_map = key[0]
        highest_map = key[1]

        if lowest_rng < highest_map and highest_rng > lowest_map:
            if lowest_map <= lowest_rng and highest_rng < highest_map:
                return_ranges.append((lowest_rng + value, highest_rng + value))
                finished = True
                break

            if lowest_map <= lowest_rng:
                return_ranges.append((lowest_rng + value, highest_map + value))
                lowest_rng = highest_map + 1

            if highest_rng <= highest_map:
                return_ranges.append((lowest_map + value, highest_rng + value))
                highest_rng = highest_map + 1

    if not finished:
        return_ranges.append((lowest_rng, highest_rng))

    return return_ranges


def part2(input_data):
    # PART 2 SOLUTION
    original_seeds, map_values = special_input(input_data)

    seed_ranges = get_seed_ranges(original_seeds)
    maps = create_maps(map_values)
    result = MAX_INT

    for sr in seed_ranges:  # (,)
        acc_ranges = [sr]
        for map in maps:  # ((I,F),V) PASADA POR TODOS LOS MAPAS
            results = []
            for r in acc_ranges:  # (,)
                ndr = next_destination_range(r, map)
                for pair in ndr:
                    results.append(pair)
            acc_ranges = results

        for ac in acc_ranges:
            result = min(result, ac[0])

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    return raw


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
