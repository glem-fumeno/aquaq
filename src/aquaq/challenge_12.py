def solve_12(file: str) -> int:
    building = {
        i: (floor[0], int(floor[1]))
        for i, line in enumerate(file.splitlines())
        if (floor := line.split(" "))
    }
    floor = 0
    floors = 1
    moving_up = True
    while floor in building:
        keep_direction, move_by = building[floor]
        if keep_direction == "0":
            moving_up = not moving_up
        if not moving_up:
            move_by *= -1
        floor += move_by
        floors += 1
    return floors
