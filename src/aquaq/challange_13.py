def solve_13(file: str) -> int:
    total = 0
    for line in file.splitlines():
        max_count = 0
        l = len(line)
        for i in range(l):
            if i > l - max_count:
                break
            for j in range(i, l):
                span = j + 1 - i
                if span * max_count > l - i:
                    break
                series = line[i:j + 1]
                count = 1
                while line.startswith(series, i + count * span):
                    count += 1
                if count > max_count:
                    max_count = count
        total += max_count

    return total
