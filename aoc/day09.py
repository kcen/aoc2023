"""09: PROBLEM NAME"""
import aoc.util
from itertools import pairwise
from operator import itemgetter

first_last = itemgetter(0, -1)


def build_history(last_row):
    lasts = [first_last(last_row)]
    while not all(v == 0 for v in last_row):
        last_row = [b - a for a, b in pairwise(last_row)]
        lasts.append(first_last(last_row))

    left, right = 0, 0
    for row in reversed(lasts):
        left = row[0] - left
        right = row[-1] + right
    return (left, right)


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        entries = (build_history([int(i) for i in l.split()]) for l in input.splitlines())
        self.sol2, self.sol1 = (sum(x) for x in zip(*entries))

    def part_one(self) -> int:
        return self.sol1

    def part_two(self) -> int:
        return self.sol2
