"""--- Day 3: Gear Ratios ---"""
import aoc.util
from math import prod
from re import finditer
from itertools import chain


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        width = input.find("\n") + 1

        # Dict[Int, List] input position and empty list for parts
        parts = dict((m.start(), list()) for m in finditer(r"[^\d\.\n]", input))
        # star_parts = defaultdict(list)

        def neighbors(start, end):
            for x in range(start - 1, end + 1):
                yield x - width
                yield x + width
            yield start - 1
            yield end

        for digit_group in finditer(r"\d+", input):
            value = int(digit_group.group())
            for p in neighbors(digit_group.start(), digit_group.end()):
                if p in parts:
                    parts[p].append(value)
                    # if input[p] == '*':
                    #     star_parts[p].append(value)

        self.part_values = parts.values()
        # self.parts = parts
        # self.star_parts = star_parts

    def part_one(self) -> int:
        return sum(chain.from_iterable(self.part_values))

    def part_two(self) -> int:
        # return sum(prod(p) for p in self.star_parts.values() if len(p) == 2)
        return sum(prod(p) for p in self.part_values if len(p) == 2)
