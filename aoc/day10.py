# You can copy/paste this template to start a new day

"""10: PROBLEM NAME"""
import aoc.util
from queue import Queue

T = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        pipe_map = input.splitlines()
        w = len(pipe_map[0])
        h = len(pipe_map)
        y, x = divmod(input.index("S"), w + 1)

        q = Queue()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c = pipe_map[y + dy][x + dx]
            for dx2, dy2 in T.get(c, []):
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

        pipe_distance = {(x, y): 0}

        while not q.empty():
            d, (x, y) = q.get()

            if (x, y) in pipe_distance:
                continue

            pipe_distance[(x, y)] = d

            for dx, dy in T[pipe_map[y][x]]:
                q.put((d + 1, (x + dx, y + dy)))

        self.part1 = max(pipe_distance.values())
        insides = 0
        for y, line in enumerate(pipe_map):
            for x, c in enumerate(line):
                if (x, y) in pipe_distance:
                    continue

                crosses = 0
                x2, y2 = x, y

                while x2 < w and y2 < h:
                    c_next = pipe_map[y2][x2]
                    if (x2, y2) in pipe_distance and c_next != "L" and c_next != "7":
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
