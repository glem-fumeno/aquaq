from pathlib import Path

number_pad = Path("./additional/number-pad.txt").read_text()
number_letter = map(lambda v: v.split(" "), number_pad.splitlines())
letter_by_number: dict[int, str] = {
    int(number): letter.replace("_", " ") for number, letter in number_letter
}


def solve_00(file: str) -> str:
    solution = ""
    for line in file.splitlines():
        number, amount = map(int, line.split(" "))
        solution += letter_by_number[number][amount - 1]
    return solution
