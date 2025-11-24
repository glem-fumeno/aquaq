from pathlib import Path


def solve(input_file: str):
    numpad = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " ",
    }
    message = ""
    sequence = Path(input_file).read_text().strip()
    for line in sequence.split("\n"):
        num, count = line.split(" ")
        message += numpad[num][int(count) - 1]
    print(message)
