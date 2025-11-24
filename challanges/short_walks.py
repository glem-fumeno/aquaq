def solve(input_file: str):
    room = [
        "  ##  ",
        " #### ",
        "######",
        "######",
        " #### ",
        "  ##  ",
    ]
    directions = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    pr, pc = 0, 2

    count = 0
    for dir in input_file:
        r, c = directions[dir][0] + pr, directions[dir][1] + pc
        if 0 <= r < len(room) and 0 <= c < len(room[r]) and room[r][c] == "#":
            pr, pc = r, c
        count += pr + pc

    print(count)
