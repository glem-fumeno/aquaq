def solve_06(file: str) -> int:
    number = int(file)
    solution = 0
    for i in range(number + 1):
        for j in range(number + 1 - i):
            k = number - i - j
            solution += f"{i}{j}{k}".count("1")
    return solution
