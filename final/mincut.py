from collections import defaultdict
from typing import Dict, List, Tuple, Set

# Reference: https://blog.thomasjungblut.com/graph/mincut/mincut/
# This reference was used to help translate the knowledge we learned in class, to a more programmatic approach. This reference was written in Java, and
#     obvioulsy this is in python, but the general algo is the same of course. 

def compute_min_cut(graph: Dict[int, List[Tuple[int, int]]]) -> Tuple[Set[int], int, List[Tuple[int, int]]]:
    def merge_vertices(g: Dict[int, List[Tuple[int, int]]], s: int, t: int) -> Dict[int, List[Tuple[int, int]]]:
        new_graph = defaultdict(list)
        for v, edges in g.items():
            if v == t:
                continue

            for dest, weight in edges:
                if dest == t:
                    new_graph[v].append((s, weight))
                else:
                    new_graph[v].append((dest, weight))

        for dest, weight in g[t]:
            if dest != s:
                new_graph[s].append((dest, weight))

        return new_graph

    def maximum_adjacency_search(g: Dict[int, List[Tuple[int, int]]]) -> Tuple[int, int, int, List[int]]:
        visited = set()
        order = []
        weights = defaultdict(int)
        start = next(iter(g))
        current = start
        visited.add(current)
        order.append(current)

        for _ in range(len(g) - 1):
            for neighbor, weight in g[current]:
                if neighbor not in visited:
                    weights[neighbor] += weight

            max_vertex = max((v for v in weights if v not in visited), key=weights.get, default=None)
            if max_vertex is None:
                break

            visited.add(max_vertex)
            order.append(max_vertex)
            current = max_vertex

        s, t = order[-2], order[-1]
        cut_weight = weights[t]
        return s, t, cut_weight, order[:-1]

    original_graph = graph
    best_cut_weight = float('inf')
    best_partition = set()
    cut_edges = []

    while len(graph) > 1:
        s, t, cut_weight, partition = maximum_adjacency_search(graph)
        if cut_weight < best_cut_weight:
            best_cut_weight = cut_weight
            best_partition = set(partition)

            # Collect edges in the cut
            cut_edges = [(u, v, w) for u in original_graph for v, w in original_graph[u] if u in best_partition and v not in best_partition]

        graph = merge_vertices(graph, s, t)

    return best_partition, best_cut_weight, cut_edges

def read_graph_from_file(file_path: str) -> Dict[int, List[Tuple[int, int]]]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0].strip())
        graph = defaultdict(list)

        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))

    return graph

if __name__ == "__main__":
    input_file = "Inputs/class_example.txt"  # Replace with your file path
    graph = read_graph_from_file(input_file)
    partition, min_cut_weight, cut_edges = compute_min_cut(graph)

    # Prepare output
    other_side = set(graph.keys()) - partition
    print(f"The weight of the minimum edge-cut is {min_cut_weight}.")
    print("The vertices on one side of the cut are:")
    print(partition)
    print("The vertices on the other side of the cut are:")
    print(other_side)
    print("The edges of the cut with their weights are:")
    for u, v, w in cut_edges:
        print(f"Edge ({u}, {v}) with weight {w}")
