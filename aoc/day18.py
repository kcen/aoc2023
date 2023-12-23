"""--- Day 18: Lavaduct Lagoon ---"""
import aoc.util

directions = {
    "R": (0, 1),
    "0": (0, 1),
    "D": (1, 0),
    "1": (1, 0),
    "L": (0, -1),
    "2": (0, -1),
    "U": (-1, 0),
    "3": (-1, 0),
}


def parse(line):
    direction, distance, color = line.split()
    distance = int(distance)
    yield (directions[direction], distance)
    distance_rgb = int(color[2:7], 16)
    yield (directions[color[7]], distance_rgb)


def dig(steps):
    pos, result = 0, 1
    for (row_delta, col_delta), distance in steps:
        pos += col_delta * distance
        result += row_delta * distance * pos + distance / 2
    return int(result)


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.pt1_in, self.pt2_in = zip(*map(parse, input.splitlines()))

    def part_one(self) -> int:
        return dig(self.pt1_in)

    def part_two(self) -> int:
        return dig(self.pt2_in)
