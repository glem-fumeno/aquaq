from collections import defaultdict


def solve_10(file: str) -> int:
    target = "DIDDY"
    origin = "TUPAC"
    _, *paths = file.splitlines()
    network: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for path in paths:
        source, destination, cost = path.split(",")
        network[source].append((destination, int(cost)))
        network[destination].append((source, int(cost)))
    visited: set[str] = set()
    journeys: dict[str, int] = {origin: 0}
    while len(network) > 0:
        node, path_cost = min(journeys.items(), key=lambda v: v[1])
        if node == target:
            break
        for next_node, node_cost in network.pop(node):
            next_cost = node_cost + path_cost
            if next_node in visited:
                continue
            if next_node in journeys and journeys[next_node] < next_cost:
                continue
            journeys[next_node] = next_cost
        journeys.pop(node)
        visited.add(node)
    return path_cost
