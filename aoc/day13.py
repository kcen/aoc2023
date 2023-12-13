"""-- Day 13: Point of Incidence ---"""
import aoc.util


def reflection(lines, smudged=0):
    for i in range(len(lines) - 1):
        smudges = (x for x in [smudged, 0, 0])
        if all(
            char1 == char2 or next(smudges)
            for chunk1, chunk2 in zip(lines[i::-1], lines[i + 1 :])
            for char1, char2 in zip(chunk1, chunk2)
        ) and not next(smudges):
            return i + 1
    return 0


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        blocks = [c.splitlines() for c in input.split("\n\n")]
        horiz = (reflection(blk) for blk in blocks)
        vert = (reflection(list(zip(*blk))) for blk in blocks)
        self.pt1 = sum((v or h * 100) for h, v in zip(horiz, vert))
        horiz = (reflection(blk, 1) for blk in blocks)
        vert = (reflection(list(zip(*blk)), 1) for blk in blocks)
        self.pt2 = sum((v or h * 100) for h, v in zip(horiz, vert))

    def part_one(self) -> int:
        return self.pt1

    def part_two(self) -> int:
        return self.pt2
