from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    children: tuple[Node, Node] | None
    value: str
    weight: int

    @classmethod
    def from_value(cls, value: str, weight: int) -> Self:
        return cls(None, value, weight)

    @classmethod
    def from_childern(cls, left: Node, right: Node) -> Self:
        return cls((left, right), left.value + right.value, left.weight + right.weight)

    def __repr__(self) -> str:
        value = "".join(self.value)
        if self.children is None:
            return f"{value}x{self.weight}"
        left, right = self.children
        return f"{value}x{self.weight}({left},{right})"

    def encode_char(self, char: str) -> str:
        if self.children is None:
            return ""
        left, right = self.children
        if char in left.value:
            return "0" + left.encode_char(char)
        else:
            return "1" + right.encode_char(char)

    def encode(self, string: str) -> str:
        return "".join(self.encode_char(char) for char in string)

    def decode(self, string: str) -> str:
        current_node = self
        solution = ""
        for ch in string:
            assert current_node.children is not None
            left, right = current_node.children
            if ch == "0":
                current_node = left
            else:
                current_node = right
            if current_node.children is None:
                assert len(current_node.value) == 1
                solution += next(iter(current_node.value))
                current_node = self
        return solution

    def codes(self) -> dict[str, str]:
        if self.children is None:
            return {"": self.value}
        left, right = self.children
        return {
            **{"0" + k: v for k, v in left.codes().items()},
            **{"1" + k: v for k, v in right.codes().items()},
        }

    @property
    def sort_by(self) -> tuple[int, int, str]:
        return self.weight, len(self.value), self.value


def solve_24(file: str) -> str:
    encoder, word = file.split("\n")
    nodes = [Node.from_value(v, w) for v, w in Counter(encoder).items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda v: v.sort_by, reverse=True)
        nodes.append(Node.from_childern(nodes.pop(), nodes.pop()))
    return nodes[0].decode(word)
