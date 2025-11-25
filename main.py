from pathlib import Path
from types import ModuleType

from challanges import (
    a_day_in_the_lift,
    cron_flakes,
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
    file_path = module.__name__.split(".")[1] + ".txt"
    file_input = Path("./inputs").joinpath(file_path).read_text().strip()
    module.solve(file_input)


def main():
    solve(whats_a_numpad)
    solve(rose_by_any_other_name)
    solve(one_is_all_you_need)
    solve(short_walks)
    solve(this_is_good_co_primen)
    solve(snake_eyes)
    solve(let_me_count_the_ways)
    solve(what_is_best_in_life)
    solve(a_day_in_the_lift)
    solve(cron_flakes)


if __name__ == "__main__":
    main()
