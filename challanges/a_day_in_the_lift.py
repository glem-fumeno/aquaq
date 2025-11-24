from pathlib import Path


def solve():
    floors = {
        i: tuple(map(int, row.split(" ")))
        for i, row in enumerate(
            Path("./inputs/a_day_in_the_lift.txt")
            .read_text()
            .strip()
            .splitlines()
        )
    }
    count = 1
    floor = 0
    direction = 1
    while floor in floors:
        stay, magnitude = floors[floor]
        if not stay:
            direction *= -1
        floor += magnitude * direction
        count += 1
    print(count)
