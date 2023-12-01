"""01: PROBLEM NAME"""
import aoc.util
import re
import string

class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()

    def part_one(self) -> int:
        numerics = (re.findall(r'\d', l) for l in self.lines)
        first_last = (int(i[0]+i[-1]) for i in numerics)
        res = sum(first_last)
        return res

    def part_two(self) -> int:
        digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        digit_map = dict(zip(digit_words, string.digits))
        num_word_pattern = fr"(?=({'|'.join(digit_words + [r'\d'])}))"
        word_to_num = lambda word: digit_map.get(word, word)
        numerics = (re.findall(num_word_pattern, l) for l in self.lines)
        first_last = (int(word_to_num(i[0])+word_to_num(i[-1])) for i in numerics)
        res = sum(first_last)
        return res
