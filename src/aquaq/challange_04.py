def solve_04(file: str) -> int:
    goal = int(file)
    factors = set()
    current_factor = 2

    number = goal
    while number != 1:
        if number % current_factor == 0:
            factors.add(current_factor)
            number //= current_factor
        else:
            current_factor += 1

    coprimes = []
    for i in range(1, goal):
        for factor in factors:
            if i % factor == 0:
                break
        else:
            coprimes.append(i)

    return sum(coprimes)
