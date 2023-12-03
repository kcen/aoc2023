# You can copy/paste this template to start a new day

"""03: PROBLEM NAME"""
import aoc.util
from math import prod
from re import finditer
from collections import defaultdict
from itertools import chain


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        width = input.find("\n") + 1

        symbols = {m.start() for m in finditer(r"[^\d\.\n]", input)}
        parts = defaultdict(list)
        # star_parts = defaultdict(list)

        for digit_group in finditer(r"\d+", input):
            neighbors = set()
            start, end = digit_group.start(), digit_group.end()
            for x in range(start - 1, end + 1):
                neighbors.add(x - width)
                neighbors.add(x + width)
            neighbors.add(start - 1)
            neighbors.add(end)

            value = int(digit_group.group())
            for p in neighbors & symbols:
                parts[p].append(value)
                # if input[p] == '*':
                #     star_parts[p].append(value)

        self.parts = parts
        # self.star_parts = star_parts

    def part_one(self) -> int:
        return sum(chain.from_iterable(self.parts.values()))

    def part_two(self) -> int:
        # return sum(prod(p) for p in self.star_parts.values() if len(p) == 2)
        return sum(prod(p) for p in self.parts.values() if len(p) == 2)
