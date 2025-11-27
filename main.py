import sys
from importlib import import_module
from pathlib import Path

puzzles = [
    "whats_a_numpad",
    "rose_by_any_other_name",
    "one_is_all_you_need",
    "short_walks",
    "this_is_good_co_primen",
    "snake_eyes",
    "let_me_count_the_ways",
    "what_is_best_in_life",
    "cron_flakes",
    "big_data",
    "troll_toll",
    "boxed_in",
    "a_day_in_the_lift",
    "o_rle",
    "thats_a_bingo",
]


def solve(name: str):
    module = import_module(f"challanges.{name}")
    file_input = Path("./inputs").joinpath(name + ".txt").read_text().strip()
    return module.solve(file_input)


def main():
    args = sys.argv
    if len(args) == 2:
        if args[-1] == "-h":
            print(*puzzles)
            return
        print(solve(args[1]))
    else:
        for name in puzzles:
            result = solve(name)
            print(
                " " * (max(map(len, puzzles)) - len(name)), f"{name}: {result}"
            )


if __name__ == "__main__":
    main()
