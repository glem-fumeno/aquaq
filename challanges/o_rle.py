def solve(input_file: str):
    counts = 0
    for line in input_file.splitlines():
        snippet_count = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line) - 1):
                if (len(line) - i - 1) // (j - i) < snippet_count:
                    continue
                repeats = line[i:]
                count = 0
                while repeats.startswith(line[i:j]):
                    count += 1
                    repeats = repeats.removeprefix(line[i:j])
                if count > snippet_count:
                    snippet_count = count
        counts += snippet_count
    return counts
