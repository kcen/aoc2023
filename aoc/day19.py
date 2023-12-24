"""--- Day 19: Aplenty ---"""
import aoc.util
import re
from math import prod


class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        self.flows, self.parts = input.split("\n\n")

    def part_one(self) -> int:
        flow_py = (
            self.flows.replace(":", " and ")
            .replace(",", "_func() or ")
            .replace("{", "_func = lambda: ")
            .replace("}", "_func()")
        )
        part_py = (
            self.parts.replace(",", ";").replace("{", "").replace("}", "; in_func() == 1 and pt_1a.append(x+m+a+s)")
        )
        state = {}
        setup = "pt_1a = []\npt1 = lambda: sum(pt_1a)\nR_func = lambda: -1\nA_func = lambda: 1"
        exec("\n".join([setup, flow_py, part_py]), state)
        return sum(state["pt_1a"])

    def part_two(self) -> int:
        rules = {
            x: [r.split(":") if ":" in r else ["=", r] for r in r.split(",")]
            for x, r in re.findall(r"^(\w+){(.+)}", self.flows, re.MULTILINE)
        }

        def filter_ranges(tests):
            while tests:
                c, xmas = tests.pop()
                if c == "A":
                    yield prod(len(x) + 1 for x in xmas.values())
                elif c == "R":
                    continue
                else:
                    for r, d in rules[c]:
                        v, s, n = re.split("([<=>])", r)
                        if s == "=":
                            tests.append((d, xmas.copy()))
                        elif s == ">":
                            a = xmas.get(v)
                            xmas[v] = range(1 + max(a.start, int(n)), a.stop)
                            tests.append((d, xmas.copy()))
                            xmas[v] = range(a.start, min(a.stop, int(n)))
                        elif s == "<":
                            a = xmas.get(v)
                            xmas[v] = range(a.start, min(a.stop, int(n)) - 1)
                            tests.append((d, xmas.copy()))
                            xmas[v] = range(max(a.start, int(n)), a.stop)

        ranges = {v: range(1, 4000) for v in "xmas"}
        return sum(filter_ranges([("in", ranges)]))
