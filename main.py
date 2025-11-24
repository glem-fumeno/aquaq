from pathlib import Path

from challanges import (
    a_day_in_the_lift,
    let_me_count_the_ways,
    one_is_all_you_need,
    rose_by_any_other_name,
    short_walks,
    snake_eyes,
    this_is_good_co_primen,
    whats_a_numpad,
)


def prepare(file_path: str) -> str:
    return Path("./inputs").joinpath(file_path).read_text().strip()


def main():
    whats_a_numpad.solve(prepare("whats_a_numpad.txt"))
    rose_by_any_other_name.solve(prepare("rose_by_any_other_name.txt"))
    one_is_all_you_need.solve(prepare("one_is_all_you_need.txt"))
    short_walks.solve(prepare("short_walks.txt"))
    this_is_good_co_primen.solve(prepare("this_is_good_co_primen.txt"))
    snake_eyes.solve(prepare("snake_eyes.txt"))
    let_me_count_the_ways.solve(prepare("let_me_count_the_ways.txt"))
    a_day_in_the_lift.solve(prepare("a_day_in_the_lift.txt"))


if __name__ == "__main__":
    main()
