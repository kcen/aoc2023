"""--- Day 4: Scratchcards ---"""
import aoc.util


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.cards = []
        for line in input.splitlines():
            this, targets = line.split(":")[1].split("|")
            target_set = {x for x in targets.split(" ") if x}
            match_count = len([1 for x in this.split(" ") if x in target_set])
            self.cards.append(match_count)

    def part_one(self) -> int:
        points_map = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        return sum(points_map[match_count] for match_count in self.cards)

    def part_two(self) -> int:
        quantity = len(self.cards)
        card_count = [1] * quantity
        for i, match_count in enumerate(self.cards):
            for bonus in range(i, i + match_count):
                if bonus < quantity:
                    card_count[bonus + 1] += card_count[i]

        return sum(card_count)
