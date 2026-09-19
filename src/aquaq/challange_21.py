from __future__ import annotations


class Node:
    __slots__ = "column", "cost", "row", "value"
    value: int
    cost: int

    def __init__(self, value: int) -> None:
        self.value = value
        self.cost = value

    def update_parent_cost(self, cost: int):
        self.cost = max(self.cost, cost + self.value)

    def __repr__(self) -> str:
        return f"N{self.cost}"

    def __eq__(self, v: object, /) -> bool:
        return type(v) is Node and (v.row, v.column) == (self.row, self.column)


class Graph:
    nodes: list[list[Node]]

    def __init__(self, costs: list[list[int]]) -> None:
        self.nodes = [[Node(v) for v in a] for a in costs]
        self.height = len(costs)
        self.width = len(costs[0])

    def neighbours_at(self, row: int, column: int) -> list[Node]:
        if row >= self.height - 1:
            return []
        nodes = [self.nodes[row + 1][column]]
        if column > 0:
            nodes.append(self.nodes[row + 1][column - 1])
        if column < self.width - 1:
            nodes.append(self.nodes[row + 1][column + 1])
        return nodes

    def max(self) -> int:
        return max(node.cost for nodes in self.nodes for node in nodes)

    def __repr__(self) -> str:
        return "\n".join(map(str, self.nodes))


def solve_21(file: str) -> int:
    costs = []
    sweep_costs = []
    span = 5
    for line in file.splitlines():
        costs.append([])
        sweep_costs.append([])
        for i, cost in enumerate(map(int, line.split(" "))):
            costs[-1].append(cost)
            if i < span - 1:
                continue
            sweep_costs[-1].append(sum(costs[-1][i - span + 1 :]))

    graph = Graph(sweep_costs)
    for row, nodes in enumerate(graph.nodes):
        for column, node in enumerate(nodes):
            for neighbour in graph.neighbours_at(row, column):
                neighbour.update_parent_cost(node.cost)
    return graph.max()
