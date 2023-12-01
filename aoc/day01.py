"""01: PROBLEM NAME"""
import aoc.util
from re import findall
from string import digits


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = input.splitlines()
        digit_words = [r"\d", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        digit_map = dict(zip(digit_words, digits))
        self.num_word_pattern = rf"(?=({'|'.join(digit_words)}))"
        self.word_to_num = lambda word: digit_map.get(word, word)

    def part_one(self) -> int:
        numerics = (findall(r"\d", l) for l in self.lines)
        first_last = (int(i[0] + i[-1]) for i in numerics)
        return sum(first_last)

    def part_two(self) -> int:
        numerics = (findall(self.num_word_pattern, l) for l in self.lines)
        first_last = (int(self.word_to_num(i[0]) + self.word_to_num(i[-1])) for i in numerics)
        return sum(first_last)
