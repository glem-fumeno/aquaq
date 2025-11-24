def solve(input_file: str):
    floors = {
        i: tuple(map(int, row.split(" ")))
        for i, row in enumerate(input_file.splitlines())
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
