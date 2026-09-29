def solve_expedition(file: str) -> int:
    scores = {i * j for i in range(1, 21) for j in range(1, 4)}.union((25, 50))
    targets = set(range(1, int(file) + 1))
    amounts = {0: 0}
    to_check = {0: 0}
    while not targets.issubset(amounts):
        to_check = {
            score + amount: steps + 1
            for score in scores
            for amount, steps in to_check.items()
            if score + amount not in amounts
        }
        amounts |= to_check
    return sum(amounts[k] for k in targets)
