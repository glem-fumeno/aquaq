from collections.abc import Callable
from pathlib import Path

from aquaq.challange_00 import solve_00
from aquaq.challange_01 import solve_01
from aquaq.challange_02 import solve_02
from aquaq.challange_03 import solve_03


def get_input(challange: str) -> str:
    return Path(f"challanges/{challange}.txt").read_text().removesuffix("\n")


def solve(solution: Callable[[str], None], challange: str):
    print(f"--- {challange} ---")
    solution(get_input(challange))


def main() -> None:
    solve(solve_00, "00")
    solve(solve_01, "01")
    solve(solve_02, "02")
    solve(solve_03, "03")
