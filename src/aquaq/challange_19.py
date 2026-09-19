class Board:
    __slots__ = "lines", "size"
    lines: list[int]
    size: int

    def __init__(self, size: int):
        self.lines = [0] * size
        self.size = size

    def at(self, y: int, x: int) -> bool:
        return (
            (0 <= x <= self.size - 1)
            and (0 <= y <= self.size - 1)
            and bool(self.lines[y] & 1 << x)
        )

    def neighbours_at(self, y: int, x: int) -> int:
        return (
            (self.at(y - 1, x))
            + (self.at(y + 1, x))
            + (self.at(y, x - 1))
            + (self.at(y, x + 1))
        )

    def iterate(self):
        lines = [0] * self.size
        for y in range(self.size):
            for x in range(self.size):
                if self.neighbours_at(y, x) % 2 == 1:
                    lines[y] |= 1 << x
                else:
                    lines[y] &= (1 << self.size) - 1 - (1 << x)
        self.lines = lines

    def on_cells(self) -> int:
        return sum(bool(l & 1 << i) for l in self.lines for i in range(self.size))

    def __repr__(self) -> str:
        return "\n".join(f"{line:06b}" for line in self.lines)


def solve_19(file: str) -> int:
    solution = 0
    for line in file.splitlines():
        print(line)
        rounds, w, *sizes = line.split(" ")
        board = Board(int(w))
        for y, x in zip(sizes[::2], sizes[1::2]):
            board.lines[int(y)] |= 1 << int(x)
        for _ in range(int(rounds)):
            board.iterate()
        solution += board.on_cells()
    return solution
