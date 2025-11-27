from copy import deepcopy


def solve(input_file: str):
    board = [
        ["6", "17", "34", "50", "68"],
        ["10", "21", "45", "53", "66"],
        ["5", "25", "36", "52", "69"],
        ["14", "30", "33", "54", "63"],
        ["15", "23", "41", "51", "62"],
    ]
    w = len(board)
    win_conditions: list[set[str]] = [set() for _ in range(w + w + 2)]
    condition_map: dict[str, list[int]] = {}
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            conditions = [i, w + j]
            if i == j:
                conditions.append(w + w)
            if i == w - 1 - j:
                conditions.append(w + w + 1)
            for idx in conditions:
                win_conditions[idx].add(tile)
            condition_map[tile] = conditions
    count = 0
    for game in input_file.splitlines():
        state = deepcopy(win_conditions)
        for i, tile in enumerate(game.split(" ")):
            for idx in condition_map.get(tile, []):
                state[idx].remove(tile)
            if any([len(s) < 1 for s in state]):
                break
        count += i + 1
    return count
