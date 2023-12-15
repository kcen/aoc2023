"""--- Day 14: Parabolic Reflector Dish ---"""
import aoc.util
from re import sub


def transpose(grid):
    grid_lines = grid.splitlines()
    return "\n".join(map("".join, zip(*grid_lines)))


def rotate(grid):
    grid_lines = grid.splitlines()
    return "\n".join(map("".join, zip(*reversed(grid_lines))))


def score(grid):
    grid_lines = grid.splitlines()
    return sum(line.count("O") * row_num for row_num, line in enumerate(reversed(grid_lines), 1))


def tilt(grid):
    grid_lines = transpose(grid).splitlines()
    tilted = []
    for line in grid_lines:
        tilted.append(sub(r"[\.O]+", lambda x: "".join(reversed(sorted(x.group()))), line))
    return transpose("\n".join(tilted))


def apply_cycle(g):
    for _ in range(4):
        g = rotate(tilt(g))
    return g


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.input = input

    def part_one(self) -> int:
        return score(tilt(self.input))

    def part_two(self) -> int:
        seen_befores = {}
        scores = {}
        target = 1000000000

        grid = self.input
        i = 0

        while not hash(grid) in seen_befores:
            scores[i] = score(grid)
            seen_befores[hash(grid)] = i
            grid = apply_cycle(grid)
            i += 1

        start = seen_befores[hash(grid)]
        period = i - start
        winner = (target - start) % period + start

        return scores[winner]
