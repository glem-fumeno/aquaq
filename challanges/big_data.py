def solve(input_file: str):
    count = 1
    for line in input_file.splitlines():
        count *= int(line)
    return count
