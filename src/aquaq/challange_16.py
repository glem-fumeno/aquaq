from collections import defaultdict

letters: dict[str, list[str]] = defaultdict(list)

with open("./additional/ascii-alphabet.txt") as f:
    for i, line in enumerate(f.read().splitlines()):
        letters[chr(ord("A") + i // 6)].append(line)


def solve_16(file: str) -> int:
    result: list[str] = ["", "", "", "", "", ""]
    for c in file:
        for i, line in enumerate(letters[c]):
            result[i] += line

    print("\n".join(result))
    return 0
