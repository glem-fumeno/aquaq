board = [
    [6, 17, 34, 50, 68],
    [10, 21, 45, 53, 66],
    [5, 25, 36, 52, 69],
    [14, 30, 33, 54, 63],
    [15, 23, 41, 51, 62],
]
bingo_numbers = [
    *[{board[i][j] for i in range(5)} for j in range(5)],
    *[{board[i][j] for j in range(5)} for i in range(5)],
    {board[i][i] for i in range(5)},
    {board[i][4 - i] for i in range(5)},
]


def solve_14(file: str) -> int:
    total = 0
    for line in file.splitlines():
        grid = set[int]()
        for i, number in enumerate(map(int, line.split(" "))):
            grid.add(number)
            if any(grid.issuperset(numbers) for numbers in bingo_numbers):
                break
        total += i + 1
    return total
