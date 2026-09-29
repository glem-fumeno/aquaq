brackets: dict[str, str] = {"[": "[", "{": "{", "(": "(", "]": "[", "}": "{", ")": "("}


def is_balanced(line: str) -> bool:
    stack: list[str] = []
    for ch in (c for c in line if c in brackets):
        current = stack[-1] if len(stack) > 0 else None
        if ch == brackets[ch]:
            stack.append(ch)
        elif current == brackets[ch]:
            stack.pop()
        else:
            return False

    return len(stack) <= 0


def solve_32(file: str) -> int:
    return sum(is_balanced(line) for line in file.splitlines())
