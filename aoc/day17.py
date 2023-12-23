"""--- Day 17: Clumsy Crucible ---"""
import aoc.util
from queue import PriorityQueue


def navigate(grid, target, step_min=1, step_max=3):
    q = PriorityQueue()
    height, width = target
    q.put((0, (0, 0), 0))
    q.put((0, (0, 0), 1))
    seen = set()
    while q:
        heat_loss, (row, col), direction = q.get()
        if (row, col) == target:
            break
        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))
        original_heat_loss = heat_loss
        for new_direction in [-1, 1]:
            heat_loss = original_heat_loss
            new_row, new_col = row, col
            for step in range(1, step_max + 1):
                if direction == 1:
                    new_col = col + step * new_direction
                else:
                    new_row = row + step * new_direction
                if new_col < 0 or new_row < 0 or new_col > width or new_row > height:
                    break
                heat_loss += grid[(new_row, new_col)]
                if ((new_row, new_col, 1 - direction)) in seen:
                    continue
                if step >= step_min:
                    q.put((heat_loss, (new_row, new_col), 1 - direction))
    return heat_loss


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        grid_dict = {(r, c): int(v) for r, l in enumerate(input.splitlines()) for c, v in enumerate(l)}
        target = max(grid_dict)
        self.part1 = navigate(grid_dict, target)
        self.part2 = navigate(grid_dict, target, 4, 8)

    def part_one(self) -> int:
        return self.part1

    def part_two(self) -> int:
        return self.part2
