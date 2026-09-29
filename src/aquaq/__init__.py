import sys
import time
from collections import OrderedDict
from collections.abc import Callable
from pathlib import Path
from typing import Any

from aquaq.challenge_00 import solve_00
from aquaq.challenge_01 import solve_01
from aquaq.challenge_02 import solve_02
from aquaq.challenge_03 import solve_03
from aquaq.challenge_04 import solve_04
from aquaq.challenge_05 import solve_05
from aquaq.challenge_06 import solve_06
from aquaq.challenge_07 import solve_07
from aquaq.challenge_08 import solve_08
from aquaq.challenge_09 import solve_09
from aquaq.challenge_10 import solve_10
from aquaq.challenge_11 import solve_11
from aquaq.challenge_12 import solve_12
from aquaq.challenge_13 import solve_13
from aquaq.challenge_14 import solve_14
from aquaq.challenge_15 import solve_15
from aquaq.challenge_16 import solve_16
from aquaq.challenge_17 import solve_17
from aquaq.challenge_18 import solve_18
from aquaq.challenge_19 import solve_19
from aquaq.challenge_20 import solve_20
from aquaq.challenge_21 import solve_21
from aquaq.challenge_22 import solve_22
from aquaq.challenge_23 import solve_23
from aquaq.challenge_24 import solve_24
from aquaq.challenge_25 import solve_25
from aquaq.challenge_26 import solve_26
from aquaq.challenge_27 import solve_27
from aquaq.challenge_28 import solve_28
from aquaq.challenge_29 import solve_29
from aquaq.challenge_30 import solve_30
from aquaq.challenge_31 import solve_31
from aquaq.challenge_32 import solve_32
from aquaq.challenge_33 import solve_expedition
from aquaq.challenge_34 import solve_34

Solution = Callable[[str], Any]

challenges: OrderedDict[str, Solution] = OrderedDict(
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
        ("30", solve_30),  # takes 14 seconds
        ("31", solve_31),  # takes 14 seconds
        ("32", solve_32),
        ("33", solve_expedition), # takes 9.3 seconds
        ("34", solve_34),
    ]
)


def get_input(challenge: str) -> str:
    return Path(f"challenges/{challenge}.txt").read_text().removesuffix("\n")


def solve(get_solution: Solution, challenge: str):
    start = time.time()
    result = get_solution(get_input(challenge))
    end = time.time()
    print(f"--- challenge {challenge} ({end - start:.5f}s) ---")
    print(result)
    print()


def main() -> None:
    if len(sys.argv) <= 1:
        for challenge, solution in challenges.items():
            solve(solution, challenge)
    else:
        solve(challenges[sys.argv[1]], sys.argv[1])
