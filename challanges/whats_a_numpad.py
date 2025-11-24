from pathlib import Path


def solve():
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
    sequence = Path("inputs/whats_a_numpad.txt").read_text().strip()
    for line in sequence.split("\n"):
        num, count = line.split(" ")
        message += numpad[num][int(count) - 1]
    print(message)

