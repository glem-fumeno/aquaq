def solve(input_file: str):
    number = int(input_file)
    counts = [str(i).count("1") * (number + 1 - i) for i in range(number + 1)]
    return sum(counts) * 3
