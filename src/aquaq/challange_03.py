from pathlib import Path

board = Path("./additional/short-room.txt").read_text().splitlines()


def get_new_position(x1: int, y1: int, x2: int, y2: int) -> tuple[int, int]:
    if not (0 <= y2 <= len(board) - 1):
        return x1, y1
    if not (0 <= x2 <= len(board[y2]) - 1):
        return x1, y1
    if board[y2][x2] == "#":
        return x2, y2
    return x1, y1


def solve_03(file: str) -> int:
    solution = 0
    y, x = 0, 2
    for c in file:
        match c:
            case "U":
                x, y = get_new_position(x, y, x, y - 1)
            case "D":
                x, y = get_new_position(x, y, x, y + 1)
            case "L":
                x, y = get_new_position(x, y, x - 1, y)
            case "R":
                x, y = get_new_position(x, y, x + 1, y)
            case v:
                raise ValueError(f"invalid value: {v}")
        solution += x + y
    return solution
