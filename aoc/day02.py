# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util
from re import findall

rgb = ['red', 'green', 'blue']
hand_regex = r'(?:(?P<red>\d+) red)|(?:(?P<green>\d+) green)|(?:(?P<blue>\d+) blue)'
collapse_single_num = lambda list: int(''.join(list) or 0)
merge_pulls = lambda pull: zip(*findall(hand_regex, pull))
split_pulls = lambda game: game.split(';')
game_hands = lambda game: [
        [
            collapse_single_num(l)
            for l in merge_pulls(pull)
        ]
        for pull in split_pulls(game)
    ]

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        games_raw = input.splitlines()
        self.games = [game_hands(game) for game in games_raw]


    def part_one(self) -> int:
        rgb_start = (12,13,14)
        red_start, blue_start, green_start = rgb_start
        is_valid_hand = lambda hand_val: (red_start >= hand_val[0] and blue_start >= hand_val[1] and green_start >= hand_val[2])
        is_valid_game = lambda game: all(is_valid_hand(hand) for hand in game)
        results = map(is_valid_game, self.games)
        res = sum(i + 1 for i, is_valid in enumerate(results) if is_valid)
        return res

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
