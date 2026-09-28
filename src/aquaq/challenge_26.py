from collections.abc import Collection, Generator


def get_permutations(text: Collection[str]) -> Generator[str]:
    if len(text) <= 1:
        yield next(iter(text))
        return
    prefix, *rest = text
    for permutation in get_permutations(rest):
        for i in range(len(text)):
            yield permutation[:i] + prefix + permutation[i:]


def solve_26(file: str) -> int:
    total = 0
    for line in file.splitlines():
        if list(line) == sorted(line, reverse=True):
            continue
        number = int(line)
        p = number
        for i in range(len(line) - 1, -1, -1):
            permutated = [
                int(line[:i] + permutation)
                for permutation in get_permutations(line[i:])
                if int(line[:i] + permutation) > number
            ]
            if len(permutated) > 0:
                p = min(permutated)
                break
        total += p - number
    return total
