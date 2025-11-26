def rotate(state: dict[str, int], sides: list[str]):
    tmp = state[sides[0]]
    for i, side in enumerate(sides[:-1]):
        state[side] = state[sides[i + 1]]
    state[sides[-1]] = tmp


def solve(input_file: str):
    rotations = {
        "L": ["F", "R", "B", "L"],
        "R": ["F", "L", "B", "R"],
        "U": ["F", "D", "B", "U"],
        "D": ["F", "U", "B", "D"],
    }
    dice1 = {"F": 1, "L": 2, "U": 3, "B": 6, "R": 5, "D": 4}
    dice2 = {"F": 1, "L": 3, "U": 2, "B": 6, "R": 4, "D": 5}
    count = 0
    for i, direction in enumerate(input_file):
        rotate(dice1, rotations[direction])
        rotate(dice2, rotations[direction])
        if dice1["F"] == dice2["F"]:
            count += i
    return count
