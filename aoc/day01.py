"""--- Day 1: Trebuchet?! ---"""
import aoc.util
from re import findall

digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", r"\d"]
digits = "0123456789"
digit_map = dict(zip(digit_words, digits))
num_word_pattern = rf"(?=({'|'.join(digit_words)}))"
word_to_num = lambda word: digit_map.get(word, word)


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.matches = [findall(num_word_pattern, l) for l in input.splitlines()]

    def part_one(self) -> int:
        numerics = ([x for x in i if len(x) == 1] for i in self.matches)
        first_last = (int(i[0] + i[-1]) for i in numerics)
        return sum(first_last)

    def part_two(self) -> int:
        first_last = (int(word_to_num(i[0]) + word_to_num(i[-1])) for i in self.matches)
        return sum(first_last)
