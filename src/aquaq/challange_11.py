def solve_11(file: str) -> int:
    _, *areas = file.splitlines()
    w, h = 0, 0
    for _, area in enumerate(areas):
        lx, ly, ux, uy = map(int, area.split(","))
        w = max(lx, ux, w)
        h = max(ly, uy, h)

    floor = [[0 for _ in range(w)] for _ in range(h)]
    counted = 0

    for area_i, area in enumerate(areas):
        lx, ly, ux, uy = map(int, area.split(","))
        for i in range(ly, uy):
            for j in range(lx, ux):
                if floor[i][j] > 0:
                    counted |= floor[i][j] | 1 << area_i
                floor[i][j] |= 1 << area_i
    return sum(t & counted != 0 for l in floor for t in l)
