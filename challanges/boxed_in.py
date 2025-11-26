from csv import reader


def solve(input_file: str):
    tile_map = []
    max_x = 0
    max_y = 0
    for line in reader(input_file.splitlines()[1:]):
        tile_map.append(map(int, line))
        max_x = max(max_x, int(line[2]))
        max_y = max(max_y, int(line[3]))
    tiles = [[[] for _ in range(max_y)] for _ in range(max_x)]
    for i, (lx, ly, ux, uy) in enumerate(tile_map):
        for x in range(lx, ux):
            for y in range(ly, uy):
                tiles[x][y].append(i)
    idx = {i for c in tiles for t in c if len(t) > 1 for i in t}
    return len([1 for c in tiles for t in c if next(iter(t), -1) in idx])
