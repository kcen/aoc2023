# You can copy/paste this template to start a new day

"""04: PROBLEM NAME"""
import aoc.util
from math import pow

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.cards = []
        for line in input.splitlines():
            start, targets = line.split('|')
            _, this = start.split(':')
            left = [x for x in this.split(' ') if x]
            right = {x for x in targets.split(' ') if x}
            match_count = len([1 for x in left if x in right])
            self.cards.append(match_count)
    def part_one(self) -> int:
        points = 0
        for match_count in self.cards:
            if match_count > 0:
                points += 2**(match_count-1)
        return points

    def part_two(self) -> int:
        quantity = len(self.cards)
        card_count = [1] * quantity
        for i, match_count in enumerate(self.cards):
            this_count = card_count[i]
            for bonus in range(i+1, i+1+match_count):
                card_count[bonus] += this_count

        return sum(card_count)
