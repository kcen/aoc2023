"""08: PROBLEM NAME"""
import aoc.util

from math import lcm
from itertools import cycle


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        steps, _, *nodes = input.splitlines()
        self.steps = steps
        self.node_map = {l[:3]: (l[7:10], l[12:15]) for l in nodes}

    def steps_to(self, start, end):
        path = cycle(self.steps)
        current = start
        iterations = 0
        while not current.endswith(end):
            step = next(path)
            current = self.node_map[current][step == "R"]
            iterations += 1
        return iterations

    def part_one(self) -> int:
        return self.steps_to("AAA", "ZZZ")

    def part_two(self) -> int:
        return lcm(self.steps_to(loc, "Z") for loc in self.node_map.keys() if loc[-1] == "A")
