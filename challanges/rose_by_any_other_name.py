import math


def solve(input_file: str):
    hex_digits = {k: k for k in "0123456789abcdef"}
    s = input_file
    i = math.ceil(len(s) / 3)
    result = ""
    for ch in [s[0], s[1], s[i], s[i + 1], s[2 * i], s[2 * i + 1]]:
        result += hex_digits.get(ch, "0")
    print(result)
