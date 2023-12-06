# You can copy/paste this template to start a new day

"""05: PROBLEM NAME"""
import aoc.util
from re import findall

def apply_map(v, rules):
    for dest, src, count in rules:
        if src <= v < src + count:
            return dest + (v - src)
    return v


def get_location(seed, sections):
    temp = seed
    for map_list in sections:
        temp = apply_map(temp, map_list)
    return temp


def r_apply_map(src_ranges, rules):
    result = []
    for start, end in src_ranges:
        covered = []
        for dest, src, count in rules:
            x, y = src, src + count - 1
            if end < x or y < start:
                continue
            start_interval = max(start, x)
            end_interval = min(end, y)
            covered.append((start_interval, end_interval))
            result.append((start_interval - src + dest, end_interval - src + dest))

        if not covered:
            result.append((start, end))
            continue
        covered.sort()

        if covered[0][0] > start:
            result.append((start, covered[0][0] - 1))

        if covered[-1][1] < end:
            result.append((covered[-1][1] + 1, end))

        for i in range(len(covered) - 1):
            _, y1 = covered[i]
            x2, _ = covered[i + 1]
            if x2 > y1 + 1:
                result.append((y1 + 1, x2 - 1))
    return result


def r_get_location(seed_range, sections):
    temp = seed_range
    for map_list in sections:
        temp = r_apply_map(temp, map_list)
    return temp


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        parser = r"(?:[a-z][a-z\- ]+:)([\d\ \n]+)"
        almanac = [
            [
                [int(i) for i in x.split()]
                for x in filter(None, d.splitlines())
            ] for d in findall(parser, input)
        ]

        seeds = almanac[0][0]
        map_list = almanac[1:]

        self.lowest = min(get_location(seed, map_list) for seed in seeds)

        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

        self.lowest_b = min(r_get_location(seed_ranges, map_list))[0]

    def part_one(self) -> int:
        return self.lowest

    def part_two(self) -> int:
        return self.lowest_b
