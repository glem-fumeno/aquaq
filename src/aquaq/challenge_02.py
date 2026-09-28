def solve_02(file: str) -> int:
    solution = []
    for number in file.split(" "):
        number = int(number)
        if number in solution:
            idx = solution.index(number)
            solution = solution[: idx + 1]
        else:
            solution.append(number)
    return sum(solution)
