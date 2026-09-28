from __future__ import annotations


class Segment:
    position: tuple[int, int]
    character: str
    neighbours: list[Segment]

    def __init__(self, position: tuple[int, int], character: str) -> None:
        self.position = position
        self.character = character
        self.neighbours = []

    def __eq__(self, value: object, /) -> bool:
        return isinstance(value, Segment) and value.position == self.position

    def get_value(self):
        return ord(self.character) - ord("a") + 1

    def get_next(self, parent: Segment | None) -> Segment | None:
        for neighbour in self.neighbours:
            if neighbour != parent:
                return neighbour

    @property
    def is_headtail(self) -> bool:
        return len(self.neighbours) <= 1

    @property
    def is_two_word(self) -> bool:
        if self.is_headtail:
            return False
        left, right = self.neighbours
        return not (
            False
            or left.position[0] == self.position[0] == right.position[0]
            or left.position[1] == self.position[1] == right.position[1]
        )

    def __hash__(self) -> int:
        return hash(self.position)

    def __repr__(self) -> str:
        return self.character


def solve_27(file: str) -> int:
    segment_by_position: dict[tuple[int, int], Segment] = {}
    for i, line in enumerate(file.splitlines()):
        for j, ch in enumerate(line):
            if ch == " ":
                continue
            segment_by_position[i, j] = Segment((i, j), ch)
    headtails = set[Segment]()
    for (i, j), segment in segment_by_position.items():
        segment.neighbours = [
            segment_by_position[p]
            for p in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            if p in segment_by_position
        ]
        if segment.is_headtail:
            headtails.add(segment)
    total = 0
    while len(headtails) > 0:
        parent = headtails.pop()
        node = parent.get_next(None)
        word = parent.character
        current_total = parent.get_value()
        while node is not None:
            word += node.character
            current_total += node.get_value()
            if node.is_two_word:
                total += current_total * len(word)
                current_total = node.get_value()
                word = node.character
            parent, node = node, node.get_next(parent)
        total += current_total * len(word)
        headtails.remove(parent)
    return total
