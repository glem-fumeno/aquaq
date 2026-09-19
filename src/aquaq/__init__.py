import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

from aquaq.challange_00 import solve_00
from aquaq.challange_01 import solve_01
from aquaq.challange_02 import solve_02
from aquaq.challange_03 import solve_03
from aquaq.challange_04 import solve_04
from aquaq.challange_05 import solve_05
from aquaq.challange_06 import solve_06
from aquaq.challange_07 import solve_07
from aquaq.challange_08 import solve_08
from aquaq.challange_09 import solve_09
from aquaq.challange_10 import solve_10
from aquaq.challange_11 import solve_11
from aquaq.challange_12 import solve_12
from aquaq.challange_13 import solve_13
from aquaq.challange_14 import solve_14
# from aquaq.challange_15 import solve_15
from aquaq.challange_16 import solve_16
from aquaq.challange_17 import solve_17
# from aquaq.challange_18 import solve_18


def get_input(challange: str) -> str:
    return Path(f"challanges/{challange}.txt").read_text().removesuffix("\n")


def solve(get_solution: Callable[[str], Any], challange: str):
    start = time.time()
    result = get_solution(get_input(challange))
    end = time.time()
    print(f"--- challange {challange} ({end - start:.5f}s) ---")
    print(result)
    print()


def main() -> None:
    solve(solve_00, "00")
    solve(solve_01, "01")
    solve(solve_02, "02")
    solve(solve_03, "03")
    solve(solve_04, "04")
    solve(solve_05, "05")
    solve(solve_06, "06")
    solve(solve_07, "07")
    solve(solve_08, "08")
    solve(solve_09, "09")
    solve(solve_10, "10")
    solve(solve_11, "11")
    solve(solve_12, "12")
    solve(solve_13, "13")
    solve(solve_14, "14")
    # solve(solve_15, "15") # run for all solutions
    solve(solve_16, "16")
    solve(solve_17, "17")
    # solve(solve_18, "18") # run for all solutions
