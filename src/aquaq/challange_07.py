def get_new_ranking(winning: float, losing: float) -> tuple[float, float]:
    delta = 1 / (1 + 10 ** ((losing - winning) / 400))
    winning += 20 * (1 - delta)
    losing -= 20 * (1 - delta)
    return winning, losing


def solve_07(file: str) -> int:
    _, *games = file.splitlines()
    scores: dict[str, float] = {}

    for game in games:
        player_a, player_b, score = game.split(",")
        a_match_score, b_match_score = map(int, score.split("-"))
        a_score = scores.get(player_a, 1200)
        b_score = scores.get(player_b, 1200)

        if a_match_score > b_match_score:
            a_score, b_score = get_new_ranking(a_score, b_score)
        else:
            b_score, a_score = get_new_ranking(b_score, a_score)
        scores[player_a] = a_score
        scores[player_b] = b_score

    return int(max(scores.values())) - int(min(scores.values()))
