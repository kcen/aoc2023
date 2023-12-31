"""--- Day 7: Camel Cards ---"""
import aoc.util

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
card_rank = dict((v, i) for i, v in enumerate("23456789TJQKA"))
wild_rank = dict((v, i) for i, v in enumerate("J23456789TQKA"))
__WILDS__ = False


def counter_like(vals):
    return {char: vals.count(char) for char in set(vals)}


class Hand:
    def __init__(self, line):
        # Parse line
        cards, bid = line.split()
        self.cards = cards
        self.bid = int(bid)

        # Card freq count
        counter = counter_like(self.cards)
        counts = sorted(counter.values(), reverse=True)
        self.typ = counts[0]
        if len(counts) > 1 and counts[1] == 2:
            self.typ += 0.5  # Full house, 2 pair

        jokers = counter.get("J", 0)
        if jokers:
            del counter["J"]
            counts = sorted(counter.values(), reverse=True)
            if jokers == 5:
                self.typ2 = 5
            else:
                self.typ2 = counts[0] + jokers

            if len(counts) > 1 and counts[1] == 2:
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
                    return card_rank[c] < card_rank[other_c]

    def __wild_lt__(self, other):
        if self.typ2 != other.typ2:
            return self.typ2 < other.typ2
        else:
            for c, other_c in zip(self.cards, other.cards):
                if c != other_c:
                    return wild_rank[c] < wild_rank[other_c]


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.hands = [Hand(l) for l in input.splitlines()]

    def part_one(self) -> int:
        global __WILDS__
        __WILDS__ = False
        return sum(i * h.bid for i, h in enumerate(sorted(self.hands), 1))

    def part_two(self) -> int:
        global __WILDS__
        __WILDS__ = True
        return sum(i * h.bid for i, h in enumerate(sorted(self.hands), 1))
