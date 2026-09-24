import sys
import time
from collections import OrderedDict
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
from aquaq.challange_15 import solve_15
from aquaq.challange_16 import solve_16
from aquaq.challange_17 import solve_17
from aquaq.challange_18 import solve_18
from aquaq.challange_19 import solve_19
from aquaq.challange_20 import solve_20
from aquaq.challange_21 import solve_21
from aquaq.challange_22 import solve_22
from aquaq.challange_23 import solve_23
from aquaq.challange_24 import solve_24
from aquaq.challange_25 import solve_25
from aquaq.challange_26 import solve_26
from aquaq.challange_27 import solve_27
from aquaq.challange_28 import solve_28
from aquaq.challange_29 import solve_29

Solution = Callable[[str], Any]

challanges: OrderedDict[str, Solution] = OrderedDict(
    [
        ("00", solve_00),
        ("00", solve_00),
        ("01", solve_01),
        ("02", solve_02),
        ("03", solve_03),
        ("04", solve_04),
        ("05", solve_05),
        ("06", solve_06),
        ("07", solve_07),
        ("08", solve_08),
        ("09", solve_09),
        ("10", solve_10),
        ("11", solve_11),
        ("12", solve_12),
        ("13", solve_13),
        ("14", solve_14),
        ("15", solve_15),  # takes 1.4 seconds
        ("16", solve_16),  # takes 5.5 seconds
        ("17", solve_17),
        ("18", solve_18),  # takes 1.2 seconds
        ("19", solve_19),  # takes 13 minutes
        ("20", solve_20),
        ("21", solve_21),
        ("22", solve_22),
        ("23", solve_23),
        ("24", solve_24),
        ("25", solve_25),
        ("26", solve_26),
        ("27", solve_27),
        ("28", solve_28),
        ("29", solve_29),
    ]
)


def get_input(challange: str) -> str:
    return Path(f"challanges/{challange}.txt").read_text().removesuffix("\n")


def solve(get_solution: Solution, challange: str):
    start = time.time()
    result = get_solution(get_input(challange))
    end = time.time()
    print(f"--- challange {challange} ({end - start:.5f}s) ---")
    print(result)
    print()


def main() -> None:
    if len(sys.argv) <= 1:
        for challange, solution in challanges.items():
            solve(solution, challange)
    else:
        solve(challanges[sys.argv[1]], sys.argv[1])
