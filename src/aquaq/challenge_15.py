from collections import defaultdict
from functools import cache
from pathlib import Path

dictionary: dict[int, set[str]] = defaultdict(set[str])
file = Path("./additional/words.txt").read_text()
for line in file.splitlines():
    dictionary[len(line)].add(line)


def is_neighbour(word1: str, word2: str) -> bool:
    if word1 == word2:
        return False
    matches = True
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if not matches:
                return False
            matches = False
    return True


def get_distance(word1: str, word2: str) -> int:
    return sum(word1[i] != word2[i] for i in range(len(word1)))


@cache
def get_neighbours(word: str) -> set[str]:
    return {word2 for word2 in dictionary[len(word)] if is_neighbour(word, word2)}


def solve_15(file: str) -> int:
    solution = 1
    for line in file.splitlines():
        origin, target = line.split(",")
        assert len(origin) == len(target)

        visited: set[str] = set()
        journeys: dict[str, tuple[int, int]] = {
            origin: (1, get_distance(origin, target))
        }
        node = origin
        while node != target:
            node, (path_cost, _) = min(
                journeys.items(), key=lambda v: v[1][0] + v[1][1]
            )
            for next_node in get_neighbours(node):
                if next_node in visited or next_node in journeys:
                    continue
                next_cost = path_cost + 1
                journeys[next_node] = next_cost, get_distance(next_node, target)
            journeys.pop(node)
            visited.add(node)
        solution *= path_cost

    return solution
