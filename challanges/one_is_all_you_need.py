def solve(input_file: str):
    sequence = list(map(int, input_file.split(" ")))
    result = []
    for number in sequence:
        if number in result:
            result = result[: result.index(number)]
        result.append(number)
    return sum(result)
