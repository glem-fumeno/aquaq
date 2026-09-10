letters_by_number: dict[int, str] = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def solve_00(file: str):
    solution = ""
    for line in file.splitlines():
        number, amount = map(int, line.split(" "))
        solution += letters_by_number[number][amount - 1]
    print(solution)
