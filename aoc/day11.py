"""--- Day 11: Cosmic Expansion ---"""
import aoc.util
from itertools import combinations


def enumerate_p(image):
    for row_p, row in enumerate(image):
        for col_p, char in enumerate(row):
            yield (row_p, col_p), char


def manhattan(p1, p2):
    Δx, Δy = [p - q for p, q in zip(p1, p2)]
    return abs(Δx) + abs(Δy)


def expand_and_solve(galaxies, empty_rows, empty_cols, expansion_factor):
    for r in reversed(empty_rows):
        for i, (gr, gc) in enumerate(galaxies):
            if gr > r:
                galaxies[i] = (gr + (expansion_factor - 1), gc)
    for c in reversed(empty_cols):
        for i, (gr, gc) in enumerate(galaxies):
            if gc > c:
                galaxies[i] = (gr, gc + (expansion_factor - 1))
    # Measure distances
    return sum(manhattan(g1, g2) for g1, g2 in combinations(galaxies, 2))


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        image = input.splitlines()
        num_rows = len(image)
        num_cols = len(image[0])
        galaxies = [p for p, char in enumerate_p(image) if char == "#"]
        empty_rows = [r for r in range(num_rows) if not any(p[0] == r for p in galaxies)]
        empty_cols = [c for c in range(num_cols) if not any(p[1] == c for p in galaxies)]
        # Expand rows and cols
        self.pt1 = expand_and_solve(galaxies.copy(), empty_rows, empty_cols, 2)
        self.pt2 = expand_and_solve(galaxies.copy(), empty_rows, empty_cols, 1_000_000)

    def part_one(self) -> int:
        return self.pt1

    def part_two(self) -> int:
        return self.pt2
