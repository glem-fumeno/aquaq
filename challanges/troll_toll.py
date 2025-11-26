from csv import DictReader


def solve(input_file: str):
    nodes: dict[str, dict[str, int]] = {}
    for line in DictReader(input_file.splitlines()):
        nodes[line["s"]] = nodes.get(line["s"], {})
        nodes[line["s"]][line["d"]] = int(line["c"])
        nodes[line["d"]] = nodes.get(line["d"], {})
        nodes[line["d"]][line["s"]] = int(line["c"])
    paths: dict[tuple[str, ...], int] = {
        (k,): v for k, v in nodes["TUPAC"].items()
    }
    while True:
        min_path = min(paths.values())
        path_name = [k for k, v in paths.items() if v == min_path][0]
        last_node = path_name[-1]
        if last_node == "DIDDY":
            return min_path
        for node, weight in nodes[last_node].items():
            if node in path_name:
                continue
            paths[(*path_name, node)] = min_path + weight
        del paths[path_name]
