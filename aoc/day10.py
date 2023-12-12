"""10: PROBLEM NAME"""
import aoc.util
from collections import deque

T = {
    "|": {(0, -1), (0, 1)},
    "-": {(-1, 0), (1, 0)},
    "L": {(0, -1), (1, 0)},
    "J": {(-1, 0), (0, -1)},
    "7": {(-1, 0), (0, 1)},
    "F": {(1, 0), (0, 1)},
}


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        pipe_map = input.splitlines()
        w = len(pipe_map[0])
        h = len(pipe_map)
        y, x = divmod(input.index("S"), w + 1)

        q = deque()
        starting_dirs = set()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c = pipe_map[y + dy][x + dx]
            for dx2, dy2 in T.get(c, []):
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.append((x + dx, y + dy))
                    starting_dirs.add((dx, dy))
        for sym, orient in T.items():
            if starting_dirs == orient:
                row = pipe_map[y]
                new_row = row[:x] + sym + row[x + 1 :]
                pipe_map[y] = new_row
                break

        pipe_loc = set((x, y))

        while len(q) > 0:
            (x, y) = q.popleft()

            if (x, y) in pipe_loc:
                continue

            pipe_loc.add((x, y))

            for dx, dy in T[pipe_map[y][x]]:
                q.append((x + dx, y + dy))

        self.part1 = (len(pipe_loc) - 1) // 2
        insides = 0
        for y, line in enumerate(pipe_map):
            for x, c in enumerate(line):
                if (x, y) in pipe_loc:
                    continue

                crosses = 0
                x2, y2 = x, y

                while x2 < w and y2 < h:
                    c_next = pipe_map[y2][x2]
                    if (x2, y2) in pipe_loc and c_next != "L" and c_next != "7":
                        crosses += 1
                    x2 += 1
                    y2 += 1

                if crosses % 2 == 1:
                    insides += 1
        self.part2 = insides

    def part_one(self) -> int:
        return self.part1

    def part_two(self) -> int:
        return self.part2
