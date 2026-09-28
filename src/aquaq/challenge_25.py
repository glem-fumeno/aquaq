from datetime import date, datetime, time
from pathlib import Path

file = Path("./additional/morse.txt").read_text()
morse_by_letter = dict([line.split(" ") for line in file.splitlines()])
letter_by_morse = {k: v for v, k in morse_by_letter.items()}


def get_delta(d1: datetime, d2: datetime) -> int:
    return abs(int((d2 - d1).total_seconds() * 1000))


def date_from_time(time_string: str) -> datetime:
    return datetime.combine(date.today(), time.fromisoformat(time_string))


def solve_25(file: str) -> str:
    deltas: list[list[int]] = [[]]
    last_d = None
    for line in file.splitlines():
        if line.strip() == "":
            last_d = None
            deltas.append([])
            continue
        d = date_from_time(line)
        if last_d is not None:
            deltas[-1].append(get_delta(last_d, d))
        last_d = d
    unique_deltas = {v for d in deltas for v in d}
    assert len(unique_deltas) == 3, "invalid input file"
    dot = min(unique_deltas)
    assert (dash := 3 * dot) in unique_deltas, "invalid input file"
    assert (spacing := 7 * dot) in unique_deltas, "invalid input file"

    solution = []
    for delta_list in deltas:
        char = ""
        solution.append("")
        for i, delta in enumerate(delta_list):
            if i % 2 == 0:
                char += "·" if delta == dot else "-"
            elif delta == dash:
                solution[-1] += letter_by_morse[char]
                char = ""
            elif delta == spacing:
                solution[-1] += letter_by_morse[char] + " "
                char = ""
        solution[-1] += letter_by_morse[char]
    return "\n".join(solution)
