hex_numbers = {f"{i:X}": f"{i:X}" for i in range(16)}


def solve_01(file: str) -> str:
    if len(file) % 3 > 0:
        file += (3 - len(file) % 3) * "0"
    section = len(file) // 3
    solution = ""
    for i in range(3):
        solution += hex_numbers.get(file[i * section].upper(), "0")
        solution += hex_numbers.get(file[i * section + 1].upper(), "0")
    return solution
