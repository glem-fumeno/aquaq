from pathlib import Path
from types import ModuleType

from challanges import (
    a_day_in_the_lift,
    big_data,
    let_me_count_the_ways,
    one_is_all_you_need,
    rose_by_any_other_name,
    short_walks,
    snake_eyes,
    this_is_good_co_primen,
    what_is_best_in_life,
    whats_a_numpad,
)


def solve(module: ModuleType):
    puzzle_name = module.__name__.split(".")[1]
    file_input = (
        Path("./inputs").joinpath(puzzle_name + ".txt").read_text().strip()
    )
    result = module.solve(file_input)
    print(f"{puzzle_name: >25}: {result}")


def main():
    solve(whats_a_numpad)
    solve(rose_by_any_other_name)
    solve(one_is_all_you_need)
    solve(short_walks)
    solve(this_is_good_co_primen)
    solve(snake_eyes)
    solve(let_me_count_the_ways)
    solve(what_is_best_in_life)
    solve(big_data)
    solve(a_day_in_the_lift)


if __name__ == "__main__":
    main()
