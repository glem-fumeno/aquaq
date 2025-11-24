def get_scores(ra: int, rb: int, a_won: bool):
    coef = 1 if a_won else -1
    diff = 20 - 20 / (1 + 10 ** ((rb - ra) * coef / 400))
    return ra + diff * coef, rb - diff * coef


def solve(input_file: str):
    scores = {}
    for line in input_file.splitlines():
        p1, p2, score = line.split(",")
        s1, s2 = score.split("-")
        scores[p1], scores[p2] = get_scores(
            scores.get(p1, 1200),
            scores.get(p2, 1200),
            int(s1) > int(s2),
        )
    print(int(max(scores.values())) - int(min(scores.values())))
