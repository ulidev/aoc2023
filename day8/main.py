"""
Author: Ferran Gonzalez Garcia
Day: 8
GitHub: https://github.com/ulidev
"""
import math
import re
from functools import reduce


def solve(instructions, graph, starting_node="AAA", part2=False):
    arrived = False
    node = starting_node
    counter = 0
    while not arrived:
        for ins in instructions:
            i = 0 if ins == "L" else 1
            node = graph[node][i]
            counter += 1
            if (part2 and node[2] == "Z") or (not part2 and node == "ZZZ"):
                arrived = True

    return counter


def get_graph(graph_input):
    graph = {}
    for line in graph_input:
        origin, destinations = line.split(" = ")
        left, right = destinations.split(", ")
        left = left[1:]
        right = right[:-1]
        graph[origin] = (left, right)

    return graph


def init(data):
    instructions, graph_input = data
    graph = get_graph(graph_input)
    return instructions, graph


def part1(data):
    instructions, graph = init(data)
    result = solve(instructions, graph)

    if result != -1:
        print("The solution to part one is: " + str(result))


def get_starting_nodes(graph):
    values = list(graph.keys())
    r = re.compile("A$")
    final = list(filter(lambda x: r.search(x), values))
    return final


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part2(data):
    instructions, graph = init(data)
    starting_nodes = get_starting_nodes(graph)
    factors = [solve(instructions, graph, sn, True) for sn in starting_nodes]
    result = reduce(lambda x, y: lcm(x,y), factors)

    if result != -1:
        print("The solution to part two is: " + str(result))


def parse_input(raw):
    data = raw.strip().split("\n\n")
    data[1] = data[1].split("\n")
    return data


def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    file = read_input()

    parsed = parse_input(file)

    part1(parsed)
    part2(parsed)
