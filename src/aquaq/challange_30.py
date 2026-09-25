from __future__ import annotations

import sys
from functools import total_ordering

inv = {".": ".", "1": "0", "0": "1"}
card_cache: dict[str, Node] = {}


@total_ordering
class Node:
    cards: str
    __is_solvable: bool | None

    def __init__(self, cards: str) -> None:
        self.cards = cards
        self.__is_solvable = None

    @classmethod
    def cached(cls, cards: str) -> Node:
        if cards not in card_cache:
            node = cls(cards)
            if len(cards) < 600:
                card_cache[cards] = node
            return node
        return card_cache[cards]

    @classmethod
    def padded(cls, cards: str) -> Node:
        return cls.cached("." + cards + ".")

    def with_removed_card(self, pos: int) -> Node:
        cards = list(self.cards)
        cards[pos - 1 : pos + 2] = [inv[cards[pos - 1]], ".", inv[cards[pos + 1]]]
        return Node.cached("".join(cards))

    def split_at(self, pos: int) -> list[Node]:
        return [
            Node.padded(self.cards[: pos - 1] + inv[self.cards[pos - 1]]),
            Node.padded(inv[self.cards[pos + 1]] + self.cards[pos + 2 :]),
        ]

    def face_up_indices(self) -> list[int]:
        return [i for i, c in enumerate(self.cards) if c == "1"]

    def is_winning(self) -> bool:
        return all(c == "." for c in self.cards)

    def is_losing(self) -> bool:
        return all(c != "1" for c in self.cards)

    def sub_nodes(self) -> list[Node]:
        return sorted(
            Node.padded(card) for card in self.cards[1:-1].split(".") if card != ""
        )

    def sub_nodes_solvable(self) -> bool:
        return all(node.is_solvable() for node in self.sub_nodes())

    def face_up_removed_solvable(self) -> bool:
        return any(
            all(node.is_solvable() for node in self.split_at(i))
            for i in self.face_up_indices()
        )

    def is_solvable(self) -> bool:
        if self.__is_solvable is None:
            if self.is_winning():
                self.__is_solvable = True
            elif self.is_losing():
                self.__is_solvable = False
            elif self.cards.count(".") > 2:
                self.__is_solvable = self.sub_nodes_solvable()
            else:
                self.__is_solvable = self.face_up_removed_solvable()
        return self.__is_solvable

    def __repr__(self) -> str:
        return self.cards

    def __hash__(self) -> int:
        return hash(self.cards)

    def __lt__(self, other: Node) -> bool:
        if self.__is_solvable is not None:
            return True
        if other.__is_solvable is not None:
            return False
        return len(self.cards) < len(other.cards)


def solve_30(file: str) -> int:
    solution = 0
    sys.setrecursionlimit(10_000)
    for i, line in enumerate(file.splitlines()):
        print(i, line)
        node = Node.padded(line)
        nodes = [node.with_removed_card(i) for i in node.face_up_indices()]
        solution += sum(node.is_solvable() for node in nodes)
    return solution
