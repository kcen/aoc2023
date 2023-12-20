"""--- Day 16: The Floor Will Be Lava ---"""
import aoc.util
from multiprocessing import Pool
from functools import partial

R, L, U, D = (0, 1), (0, -1), (-1, 0), (1, 0)
STEPS = {
    "\\": {R: [D], L: [U], D: [R], U: [L]},
    "/": {R: [U], L: [D], D: [L], U: [R]},
    "-": {R: [R], L: [L], D: [L, R], U: [L, R]},
    "|": {R: [U, D], L: [U, D], D: [D], U: [U]},
    ".": {R: [R], L: [L], D: [D], U: [U]},
}


def do_step(pos, step):
    return (pos[0] + step[0], pos[1] + step[1])


def energize(grid, start, direction):
    current = (start, direction)
    moving, seen = [current], {current}
    while any(moving):
        position, direction = moving.pop()
        for step in STEPS[grid[position]][direction]:
            next_pos = do_step(position, step)
            if next_pos not in grid or (next_pos, step) in seen:
                continue
            moving.append((next_pos, step))
            seen.add((next_pos, step))

    return len(set(pos for pos, _ in seen))


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.grid = {}

        for r, line in enumerate(input.splitlines(), 1):
            for c, v in enumerate(line, 1):
                self.grid[(r, c)] = v
        self.num_rows = r
        self.num_cols = c

    def part_one(self) -> int:
        return energize(self.grid, (1, 1), R)

    def part_two(self) -> int:
        starts = (
            [((1, c), D) for c in range(1, self.num_cols)]
            + [((self.num_rows, c), U) for c in range(1, self.num_cols)]
            + [((r, 1), D) for r in range(1, self.num_rows)]
            + [((r, self.num_cols), D) for r in range(1, self.num_rows)]
        )
        apply_func = partial(energize, self.grid)
        with Pool() as p:
            return max(p.starmap(apply_func, starts))
