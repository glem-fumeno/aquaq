from __future__ import annotations

from typing import Literal, cast

CardState = Literal[".", "0", "1"]


class Node:
    cards: str

    def __init__(self, cards: str) -> None:
        self.cards = cards

    def replace_at(self, pos: int, state: CardState):
        self.cards = self.cards[:pos] + state + self.cards[pos + 1 :]

    def get_at(self, pos: int) -> CardState:
        return cast(CardState, self.cards[pos])

    def get_opposite(self, state: CardState) -> CardState:
        match state:
            case ".":
                return "."
            case "0":
                return "1"
            case "1":
                return "0"

    def get_node_with_removed_card(self, pos: int) -> Node:
        next_node = Node(self.cards)
        next_node.replace_at(pos, ".")
        next_node.replace_at(pos - 1, self.get_opposite(self.get_at(pos - 1)))
        next_node.replace_at(pos + 1, self.get_opposite(self.get_at(pos + 1)))
        return next_node

    def get_face_up_indices(self) -> list[int]:
        return [i for i, c in enumerate(self.cards) if c == "1"]

    def __repr__(self) -> str:
        return self.cards

    def is_winning(self) -> bool:
        return all(c == "." for c in self.cards)

    def is_losing(self) -> bool:
        return all(c != "1" for c in self.cards)


def solve_30(file: str) -> int:
    for line in file.splitlines():
        node = Node("." + line + ".")
        nodes = [node.get_node_with_removed_card(i) for i in node.get_face_up_indices()]
        for index in node.get_face_up_indices():
            next_node = node.get_node_with_removed_card(index)
        print()
    return 0
