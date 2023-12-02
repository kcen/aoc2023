# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util
from re import findall
from functools import reduce

hand_regex = r"(?:(\d+) red)|(?:(\d+) green)|(?:(\d+) blue)"
collapse_single_num = lambda list: int("".join(list) or 0)
merge_pulls = lambda pull: zip(*findall(hand_regex, pull))
split_pulls = lambda game: game.split(";")
game_hands = lambda game: [[collapse_single_num(l) for l in merge_pulls(pull)] for pull in split_pulls(game)]

# part 1
rgb_start = (12, 13, 14)
is_valid_hand = lambda hand_val: all(this_hand <= total for this_hand, total in zip(hand_val, rgb_start))
is_valid_game = lambda game: all(is_valid_hand(hand) for hand in game)

# part 2
mult_pair = lambda x, y: x * y
min_balls = lambda game: reduce(mult_pair, map(max, zip(*game)))

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        games_raw = input.splitlines()
        self.games = [game_hands(game) for game in games_raw]

    def part_one(self) -> int:
        valid_games = enumerate(map(is_valid_game, self.games), 1)
        results = (i for i, is_valid in valid_games if is_valid)
        return sum(results)

    def part_two(self) -> int:
        results = map(min_balls, self.games)
        return sum(results)
