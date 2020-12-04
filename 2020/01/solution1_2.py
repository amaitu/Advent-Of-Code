import json
from itertools import combinations
from math import prod


def import_json(path):
    with open(path) as file:
        return json.load(file)


def find_entries_that_sum_to_year(target_year: int, numbers: list, no_of_entries: int):
    return [
        prod(combination)
        for combination in combinations(numbers, no_of_entries)
        if sum(combination) == target_year
    ][0]


print(
    find_entries_that_sum_to_year(2020, import_json("input.json"), 2),
    find_entries_that_sum_to_year(2020, import_json("input.json"), 3),
)
