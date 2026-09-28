from typing import Literal, cast, get_args

Face = Literal["F", "U", "L", "R", "D", "B"]
faces: list[Face] = list(get_args(Face))

rotation_order: dict[Face, list[tuple[Face, int, int, int]]] = {
    "F": [("L", 8, 5, 2), ("U", 6, 7, 8), ("R", 0, 3, 6), ("D", 2, 1, 0)],
    "R": [("F", 8, 5, 2), ("U", 8, 5, 2), ("B", 0, 3, 6), ("D", 8, 5, 2)],
    "U": [("F", 2, 1, 0), ("L", 2, 1, 0), ("B", 2, 1, 0), ("R", 2, 1, 0)],
    "B": [("R", 8, 5, 2), ("U", 2, 1, 0), ("L", 0, 3, 6), ("D", 6, 7, 8)],
    "L": [("F", 0, 3, 6), ("D", 0, 3, 6), ("B", 8, 5, 2), ("U", 0, 3, 6)],
    "D": [("F", 6, 7, 8), ("R", 6, 7, 8), ("B", 6, 7, 8), ("L", 6, 7, 8)],
}


class Cube:
    def __init__(self) -> None:
        self.faces: dict[Face, list[Face]] = {face: [face] * 9 for face in faces}

    def _rotate_face(self, face: Face, prime: bool):
        f = self.faces[face]
        if prime:
            f[0], f[2], f[8], f[6] = f[2], f[8], f[6], f[0]
            f[1], f[5], f[7], f[3] = f[5], f[7], f[3], f[1]
        else:
            f[0], f[6], f[8], f[2] = f[6], f[8], f[2], f[0]
            f[1], f[3], f[7], f[5] = f[3], f[7], f[5], f[1]

    def _rotate_sides(self, order: list[tuple[Face, int, int, int]], prime: bool):
        if not prime:
            order = order[::-1]
        tmp = self._get_group(order[0])
        for i in range(len(order) - 1):
            self._replace_group(order[i], self._get_group(order[i + 1]))
        self._replace_group(order[-1], tmp)

    def _get_group(
        self, indices: tuple[Face, int, int, int]
    ) -> tuple[Face, Face, Face]:
        face, i, j, k = indices
        return self.faces[face][i], self.faces[face][j], self.faces[face][k]

    def _replace_group(
        self, indices: tuple[Face, int, int, int], group: tuple[Face, Face, Face]
    ):
        face, i, j, k = indices
        fi, fj, fk = group
        self.faces[face][i], self.faces[face][j], self.faces[face][k] = fi, fj, fk

    def scramble(self, faces: str):
        faces += " "
        i = 0
        while faces[i] != " ":
            prime = faces[i + 1] == "'"
            face = cast(Face, faces[i])
            self._rotate_sides(rotation_order[face], prime)
            self._rotate_face(face, prime)
            i += 2 if prime else 1

    def get_result(self):
        solution = 1
        for face in self.faces["F"]:
            solution *= faces.index(face) + 1
        return solution

    def __repr__(self) -> str:
        result = ""
        for face in faces:
            result += f"\n{face}\n"
            ls = self.faces[face][::3]
            ms = self.faces[face][1::3]
            rs = self.faces[face][2::3]
            for l, m, r in zip(ls, ms, rs):
                result += f"{l}{m}{r}\n"
        return result


def solve_31(file: str) -> int:
    cube = Cube()
    cube.scramble(file)
    return cube.get_result()
