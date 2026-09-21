from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    children: tuple[Node, Node] | None
    value: set[str]
    weight: int

    @classmethod
    def from_value(cls, value: set[str], weight: int) -> Self:
        return cls(None, value, weight)

    @classmethod
    def from_childern(cls, left: Node, right: Node) -> Self:
        return cls(
            (left, right), left.value.union(right.value), left.weight + right.weight
        )

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


def solve_24(file: str) -> str:
    encoder, word = file.split("\n")
    nodes = [Node.from_value({v}, w) for v, w in Counter(encoder).most_common()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda v: v.weight, reverse=True)
        nodes.append(Node.from_childern(nodes.pop(), nodes.pop()))
    root = nodes[0]
    print(root)
    return root.decode(word)
