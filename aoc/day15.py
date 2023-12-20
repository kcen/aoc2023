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
        self.input = input.strip().split(",")

    def part_one(self) -> int:
        return sum(hasher(x) for x in self.input)

    def part_two(self) -> int:
        boxes = [[] for _ in range(256)]
        labels = {}
        for command in self.input:
            if "-" in command:
                label = command[:-1]
                box = hasher(label)
                try:
                    idx = boxes[box].index(label)
                    boxes[box].pop(idx)
                except ValueError:
                    pass
            else:
                label = command[:-2]
                i = int(command[-1])
                box = hasher(label)
                try:
                    idx = boxes[box].index(label)
                    boxes[box][idx] = label
                except ValueError:
                    boxes[box].append(label)
                labels[label] = i

        runner = 0
        for box_num, box_labels in enumerate(boxes, 1):
            for slot, label in enumerate(box_labels, 1):
                runner += box_num * slot * labels[label]

        return runner
