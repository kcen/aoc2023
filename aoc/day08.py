"""08: PROBLEM NAME"""
import aoc.util

from math import lcm
from itertools import cycle


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        steps, _, *nodes = input.splitlines()
        self.steps = steps
        self.node_map = {l[:3]: (l[7:10], l[12:15]) for l in nodes}

    def part_one(self) -> int:
        path = cycle(self.steps)
        start = "AAA"
        end = "ZZZ"
        current = start
        iterations = 0
        while True:
            step = next(path)
            current = self.node_map[current][step == "R"]
            iterations += 1
            if current == end:
                break
        return iterations

    def part_two(self) -> int:
        workers = [v for v in self.node_map.keys() if v[-1] == "A"]
        freqs = []
        for loc in workers:
            iterations = 1
            path = cycle(self.steps)
            current = self.node_map[loc][next(path) == "R"]
            while True:
                step = next(path)
                current = self.node_map[current][step == "R"]
                iterations += 1
                if current[-1] == "Z":
                    break
            freqs.append(iterations)
        return lcm(*freqs)
