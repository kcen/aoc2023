"""12: PROBLEM NAME"""
import aoc.util
from functools import cache

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


@cache
def match_count(structure, size, groups):
    if len(groups) == 0:
        if DAMAGED in structure:
            return 0
        else:
            return 1
    next_group, *others = groups
    extra = sum(others) + len(others)  # minimum damaged gears and padding
    count = 0
    available = size - extra - next_group + 1
    for b in range(available):
        candidate = f"{OPERATIONAL * b}{DAMAGED * next_group}{OPERATIONAL}"
        comp = zip(structure, candidate)
        if all(s in [c, UNKNOWN] for s, c in comp):
            count += match_count(structure[len(candidate) :], size - next_group - b - 1, tuple(others))
    return count


class Arrangements:
    def __init__(self, line):
        layout, groups = line.split(" ")
        group_counts = tuple(int(i) for i in groups.split(","))
        self.combos = match_count(layout, len(layout), tuple(group_counts))
        big_layout = "?".join((layout,) * 5)
        self.big_combos = match_count(big_layout, len(big_layout), group_counts * 5)


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.arrs = [Arrangements(l) for l in input.splitlines()]

    def part_one(self) -> int:
        return sum(x.combos for x in self.arrs)

    def part_two(self) -> int:
        return sum(x.big_combos for x in self.arrs)
