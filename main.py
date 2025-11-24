from pathlib import Path

from challanges import (
    a_day_in_the_lift,
    one_is_all_you_need,
    rose_by_any_other_name,
    short_walks,
    whats_a_numpad,
)


def prepare(file_path: str) -> str:
    return Path("./inputs").joinpath(file_path).read_text().strip()


def main():
    whats_a_numpad.solve(prepare("whats_a_numpad.txt"))
    rose_by_any_other_name.solve(prepare("rose_by_any_other_name.txt"))
    one_is_all_you_need.solve(prepare("one_is_all_you_need.txt"))
    a_day_in_the_lift.solve(prepare("a_day_in_the_lift.txt"))
    short_walks.solve(prepare("short_walks.txt"))


if __name__ == "__main__":
    main()
