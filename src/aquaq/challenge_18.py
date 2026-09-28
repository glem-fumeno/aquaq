import calendar
import time


def solve_18(file: str) -> int:
    solution = 0
    for line in file.splitlines():
        t = calendar.timegm(time.strptime(line, "%H:%M:%S"))
        for i in range(24 * 60 * 60):
            offset = time.strftime("%H:%M:%S", time.gmtime(t + i))
            if offset == offset[::-1]:
                solution += i
                break
            offset = time.strftime("%H:%M:%S", time.gmtime(t - i))
            if offset == offset[::-1]:
                solution += i
                break

    return solution
