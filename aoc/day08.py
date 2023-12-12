"""--- Day 8: Haunted Wasteland ---"""
import aoc.util

from math import lcm
from itertools import cycle


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        steps, _, *nodes = input.splitlines()
        self.steps = [(0, 1)[c == "R"] for c in steps]
        self.node_map = {l[:3]: (l[7:10], l[12:15]) for l in nodes}

    def steps_to(self, start, end):
        path = cycle(self.steps)
        current = start
        iterations = 0
        for step in path:
            current = self.node_map[current][step]
            iterations += 1
            if current.endswith(end):
                return iterations

    def part_one(self) -> int:
        return self.steps_to("AAA", "ZZZ")

    def part_two(self) -> int:
        steps = (self.steps_to(loc, "Z") for loc in self.node_map.keys() if loc.endswith("A"))
        return lcm(*steps)
