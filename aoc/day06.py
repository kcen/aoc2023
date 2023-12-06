# You can copy/paste this template to start a new day

"""06: PROBLEM NAME"""
import aoc.util
from math import prod, sqrt, pow, floor, ceil


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        times, records = [[int(i) for i in l.split(":")[1].split()] for l in input.splitlines()]

        def min_maxer(t, r):
            b = r + 0.1  # Just a smidge faster
            Δ = sqrt(pow(t, 2) - (4.0 * b))
            low = 0.5 * (t - Δ)
            high = 0.5 * (t + Δ)
            return floor(high) - ceil(low) + 1

        self.sol1 = prod(min_maxer(*v) for v in zip(times, records))
        p2_time = int("".join(str(i) for i in times))
        p2_dist = int("".join(str(i) for i in records))
        self.sol2 = min_maxer(p2_time, p2_dist)

    def part_one(self) -> int:
        return self.sol1

    def part_two(self) -> int:
        return self.sol2
