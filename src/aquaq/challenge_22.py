order = [
    (1000, ["M", "×", "×"]),
    (100, ["C", "D", "M"]),
    (10, ["X", "L", "C"]),
    (1, ["I", "V", "X"]),
]


def solve_22(file: str) -> int:
    solution = 0
    for characters in file.split(" "):
        number = int(characters)
        answer = ""
        for magnitude, symbols in order:
            n = number // magnitude
            ones, fives, tens = symbols
            if n < 4:
                answer += ones * n
            elif n == 4:
                answer += ones + fives
            elif n < 9:
                answer += fives + ones * (n - 5)
            else:
                answer += ones + tens
            number -= n * magnitude
        for ch in answer:
            solution += ord(ch) - ord("A") + 1
    return solution
