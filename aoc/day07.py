"""07: PROBLEM NAME"""
import aoc.util
from collections import Counter
from dataclasses import dataclass, field

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
card_rank = "23456789TJQKA"
wild_rank = "J23456789TQKA"
__WILDS__ = False


@dataclass
class Hand:
    cards: str = field(init=False)
    bid: int = field(init=False)
    line: str

    def __post_init__(self):
        # Parse line
        cards, bid = self.line.split()
        self.cards = cards
        self.bid = int(bid)

        # Card freq count
        counter = Counter(self.cards)
        counts = sorted(counter.values())
        self.typ = counts[-1]
        if len(counts) > 1 and counts[-2] == 2:
            self.typ += 0.5  # Full house, 2 pair

        jokers = counter["J"]
        if jokers:
            del counter["J"]
            counts = sorted(counter.values())
            if jokers == 5:
                self.typ2 = 5
            else:
                self.typ2 = counts[-1] + jokers

            if len(counts) > 1 and counts[-2] == 2:
                self.typ2 += 0.5  # Full house, 2 pair
        else:
            self.typ2 = self.typ

    def __lt__(self, other):
        if __WILDS__:
            return self.__wild_lt__(other)
        if self.typ != other.typ:
            return self.typ < other.typ
        else:
            for c, other_c in zip(self.cards, other.cards):
                if c != other_c:
                    return card_rank.index(c) < card_rank.index(other_c)

    def __wild_lt__(self, other):
        if self.typ2 != other.typ2:
            return self.typ2 < other.typ2
        else:
            for c, other_c in zip(self.cards, other.cards):
                if c != other_c:
                    return wild_rank.index(c) < wild_rank.index(other_c)


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.hands = [Hand(line=l) for l in input.splitlines()]

    def part_one(self) -> int:
        global __WILDS__
        __WILDS__ = False
        return sum(i * h.bid for i, h in enumerate(sorted(self.hands), 1))

    def part_two(self) -> int:
        global __WILDS__
        __WILDS__ = True
        return sum(i * h.bid for i, h in enumerate(sorted(self.hands), 1))
