from collections import defaultdict

letters: dict[str, list[str]] = defaultdict(list)

with open("./additional/ascii-alphabet.txt") as f:
    for i, line in enumerate(f.read().splitlines()):
        letters[chr(ord("A") + i // 6)].append(line)


def solve_16(file: str) -> int:
    result: list[str] = ["#", "#", "#", "#", "#", "#"]
    for c in file:
        free_space = len(result[0])
        for i, line in enumerate(letters[c]):
            ch_left = len(result[i]) - 1 - result[i].rfind("#")
            ch_right = line.find("#")
            free_space = min(free_space, ch_left + ch_right)
        for i, line in enumerate(letters[c]):
            result[i] += "·"
            if free_space < 1:
                result[i] += line
                continue
            remainder = result[i][-free_space:]
            result[i] = result[i][:-free_space]
            for n in range(free_space):
                result[i] += line[n] if line[n] == "#" else remainder[n]
            result[i] += line[free_space:]
    for i, line in enumerate(result):
        result[i] = line[2:]

    # print("\n".join(result))
    return sum(c == "·" for line in result for c in line)
