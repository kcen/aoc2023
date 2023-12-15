"""--- Day 15: Lens Library ---"""
import aoc.util


def hasher(stringy):
    runner = 0
    for c in stringy:
        runner += ord(c)
        runner = (runner * 17) % 256
    return runner


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.input = input.split(",")

    def part_one(self) -> int:
        return sum(hasher(x) for x in self.input)

    def part_two(self) -> int:
        boxes = {i: [] for i in range(256)}
        for command in self.input:
            if "-" in command:
                label = command[:-1]
                box = hasher(label)
                box_labels = [a for a, _ in boxes[box]]
                try:
                    idx = box_labels.index(label)
                    boxes[box].pop(idx)
                except ValueError:
                    pass
            else:
                label = command[:-2]
                i = int(command[-1])
                box = hasher(label)
                box_labels = [a for a, _ in boxes[box]]
                try:
                    idx = box_labels.index(label)
                    boxes[box][idx] = (label, i)
                except ValueError:
                    boxes[box].append((label, i))

        runner = 0
        for key, box in boxes.items():
            for i, box_item in enumerate(box):
                runner += (key + 1) * (i + 1) * box_item[1]

        return runner
