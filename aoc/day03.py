# You can copy/paste this template to start a new day

"""03: PROBLEM NAME"""
import aoc.util
from math import prod
from re import finditer
from collections import defaultdict


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        width = input.find("\n")
        schematic = input.replace("\n", "")

        symbols = {divmod(m.start(), width) for m in finditer(r"[^\d\.]", schematic)}
        stars = {divmod(m.start(), width) for m in finditer(r"\*", schematic)}
        parts = defaultdict(set)

        touching = [-width - 1, -width, -width + 1, -1, +1, width - 1, width, width + 1]

        for digit_group in finditer(r"\d+", schematic):
            positions = range(*digit_group.span())
            value = int(digit_group.group())
            neighbors = {divmod(pos + neighbor, width) for neighbor in touching for pos in positions}
            for p in neighbors & symbols:
                parts[p].add(value)

        self.parts = parts
        self.stars = stars

    def part_one(self) -> int:
        return sum(sum(p) for p in self.parts.values())

    def part_two(self) -> int:
        star_parts = [self.parts[x] for x in self.stars if len(self.parts[x]) == 2]
        return sum(prod(p) for p in star_parts)
