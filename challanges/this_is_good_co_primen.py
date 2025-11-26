def is_co_prime(v, r):
    if r % 2 == v % 2 == 0:
        return False
    if r > v:
        v, r = r, v
    # Euclidean algorithm
    while r > 0:
        v, r = r, v % r
    return v == 1


def solve(input_file: str):
    value = int(input_file)
    return sum(i + 1 for i in range(value) if is_co_prime(value, i + 1))
