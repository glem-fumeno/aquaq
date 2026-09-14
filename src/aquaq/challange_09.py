def solve_09(file: str) -> int:
    product = 1
    for line in file.splitlines():
        product *= int(line)
    return product
