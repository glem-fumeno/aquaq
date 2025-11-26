from csv import DictReader


def get_scores(ra: int, rb: int, a_won: bool):
    coef = 1 if a_won else -1
    diff = 20 - 20 / (1 + 10 ** ((rb - ra) * coef / 400))
    return ra + diff * coef, rb - diff * coef


def solve(input_file: str):
    scores = {}
    for line in DictReader(input_file.splitlines()):
        s1, s2 = line["score"].split("-")
        scores[line["h"]], scores[line["a"]] = get_scores(
            scores.get(line["h"], 1200),
            scores.get(line["a"], 1200),
            int(s1) > int(s2),
        )
    return int(max(scores.values())) - int(min(scores.values()))
