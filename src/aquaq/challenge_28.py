from __future__ import annotations

from typing import Literal, cast

MirrorPosition = Literal[" ", "/", "\\"]


class MirrorMaze:
    def __init__(self, map: str) -> None:
        self.mirrors: list[list[MirrorPosition]] = []
        self.letters: list[str] = list(map.splitlines()[0][1:-1])
        self.idx_by_letter = {l: i for i, l in enumerate(self.letters)}
        for line in map.splitlines()[1:-1]:
            self.mirrors.append([])
            for ch in line[1:-1]:
                self.mirrors[-1].append(cast(MirrorPosition, ch))
        assert len(self.mirrors) == len(self.mirrors[0])
        self.size = len(self.mirrors)

    def flip_if_mirror_at(self, row: int, col: int) -> None:
        match self.mirrors[row][col]:
            case " ":
                return
            case "/":
                self.mirrors[row][col] = "\\"
            case "\\":
                self.mirrors[row][col] = "/"

    def get_next_delta(
        self, row: int, col: int, drow: int, dcol: int
    ) -> tuple[int, int]:
        match self.mirrors[row][col]:
            case " ":
                return drow, dcol
            case "/":
                # r1c2; r2c2 -> r2c1 |  1; 0 ->  0;-1
                # r2c1; r2c2 -> r1c2 |  0; 1 -> -1; 0
                # r3c2; r2c2 -> r2c3 | -1; 0 ->  0; 1
                # r2c3; r2c2 -> r3c2 |  0;-1 ->  1; 0
                # swap and flip sign
                return -dcol, -drow
            case "\\":
                # r1c2; r2c2 -> r2c3 |  1; 0 ->  0; 1
                # r2c3; r2c2 -> r1c2 |  0;-1 -> -1; 0
                # r3c2; r2c2 -> r2c1 | -1; 0 ->  0;-1
                # r2c1; r2c2 -> r3c2 |  0; 1 ->  1; 0
                # swap
                return dcol, drow

    def get_row_from_letter(self, letter: str) -> int:
        return self.idx_by_letter[letter]

    def is_in_maze(self, row: int, col: int) -> bool:
        return 0 <= row <= self.size - 1 and 0 <= col <= self.size - 1

    def get_letter_from_outer_position(self, row: int, col: int) -> str:
        assert not self.is_in_maze(row, col)
        if not 0 <= row <= self.size - 1:
            return self.letters[col]
        return self.letters[row]

    def encrypt_letter(self, letter: str):
        drow, dcol = 0, 1
        row, col = self.get_row_from_letter(letter), 0
        while self.is_in_maze(row, col):
            drow, dcol = self.get_next_delta(row, col, drow, dcol)
            self.flip_if_mirror_at(row, col)
            row, col = row + drow, col + dcol
        return self.get_letter_from_outer_position(row, col)

    def encrypt(self, word: str) -> str:
        return "".join(self.encrypt_letter(letter) for letter in word)

    def __repr__(self) -> str:
        return "\n".join("".join(mirrors) for mirrors in self.mirrors)


def solve_28(file: str) -> str:
    return MirrorMaze(file).encrypt("FISSION_MAILED")
