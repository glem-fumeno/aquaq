def solve_29(file: str) -> int:
    total = 0
    number = 0
    while number <= int(file):
        # if number % 1_000_000 == 0:
        #     print(number)
        sn = str(number)
        to_skip = 1
        for i in range(len(sn) - 2):
            if int(sn[i]) > int(sn[i + 1]):
                to_skip = 10 ** (len(sn) - i - 2)
                break
        else:
            if sorted(sn) == list(sn):
                total += 1
        number += to_skip

    return total
