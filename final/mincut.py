from collections import defaultdict
from typing import Dict, List, Tuple, Set
import os

def run_stoer_wagner(input_file: str, output_file: str):
    graph, original_edges = read_graph_from_file(input_file)
    partition, min_cut_weight, _ = compute_min_cut(graph)
    other_side = set(graph) - partition

    # Recompute cut edges from the original edges:
    cut_edges = set()
    for (u, v, w) in original_edges:
        # If one endpoint is in the partition and the other is not, it's a cut edge
        if (u in partition and v in other_side) or (v in partition and u in other_side):
            cut_edges.add((min(u, v), max(u, v), w))

    write_output_file(output_file, partition, other_side, cut_edges, min_cut_weight)

def merge_vertices(g, s, t, merged_vertices):
    # Ensure both s and t are initialized in merged_vertices
    if s not in merged_vertices:
        merged_vertices[s] = {s}
    if t not in merged_vertices:
        merged_vertices[t] = {t}
    
    # Merge vertex sets
    merged_vertices[s].update(merged_vertices[t])
    del merged_vertices[t]

    new_graph = defaultdict(list)
    for v, edges in g.items():
        for dest, weight in edges:
            # Redirect edges involving t to s
            if dest == t:
                dest = s
            if v == t:
                v = s
            if v != dest:  # Avoid self-loops
                new_graph[v].append((dest, weight))
    
    # Combine parallel edges
    for v, edges in new_graph.items():
        combined = defaultdict(int)
        for dest, weight in edges:
            combined[dest] += weight
        new_graph[v] = [(dest, weight) for dest, weight in combined.items()]

    # Remove self-loops
    for v in new_graph:
        new_graph[v] = [(dest, weight) for dest, weight in new_graph[v] if dest != v]

    return new_graph

def compute_min_cut(graph: Dict[int, List[Tuple[int, int]]]):
    merged_vertices = {v: {v} for v in graph}
    best_cut_weight = float('inf')
    best_partition = set()
    best_merged_snapshot = None
    cut_edges = []

    def maximum_adjacency_search(g: Dict[int, List[Tuple[int,int]]]):
        visited = set()
        order = []
        weights = defaultdict(int)
        start = next(iter(g))
        visited.add(start)
        order.append(start)
        current = start

        for _ in range(len(g)-1):
            for neighbor, w in g[current]:
                if neighbor not in visited:
                    weights[neighbor] += w

            candidates = [(v, weights[v]) for v in weights if v not in visited]
            if not candidates:
                break
            max_vertex = max(candidates, key=lambda x: (x[1], -x[0]))[0]

            visited.add(max_vertex)
            order.append(max_vertex)
            current = max_vertex

        s, t = order[-2], order[-1]
        cut_weight = weights[t]
        return s, t, cut_weight, order[:-1]

    # Copy the original graph to mutate
    local_graph = {k: list(v) for k,v in graph.items()}

    while len(local_graph) > 1:
        s, t, cut_weight, order = maximum_adjacency_search(local_graph)

        # Current partition from this phase
        partition = set(order)

        if cut_weight < best_cut_weight:
            best_cut_weight = cut_weight
            best_partition = partition.copy()
            best_merged_snapshot = {k: set(v) for k,v in merged_vertices.items()}

        local_graph = merge_vertices(local_graph, s, t, merged_vertices)

    # Reconstruct final partitions from the best snapshot
    expanded_partition = set()
    for v in best_partition:
        expanded_partition.update(best_merged_snapshot.get(v, {v}))

    # All vertices from the best snapshot
    all_vertices = set()
    for group in best_merged_snapshot.values():
        all_vertices.update(group)

    other_side = all_vertices - expanded_partition

    # Return the final partition, cut weight, and empty cut_edges (we'll recalc later)
    return expanded_partition, best_cut_weight, []


def read_graph_from_file(file_path: str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0].strip())
        graph = defaultdict(list)
        original_edges = []  # Keep track of all original edges

        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))
            original_edges.append((u, v, weight))

    return graph, original_edges

    return graph
def write_output_file(file_path, partition, other_side, cut_edges, min_cut_weight):
    with open(file_path, 'w') as f:
        f.write(f"The weight of the minimum edge-cut is {min_cut_weight}.\n")
        f.write("The vertices on one side of the cut are:\n")
        f.write(f"{partition}\n")
        f.write("The vertices on the other side of the cut are:\n")
        f.write(f"{other_side}\n")
        f.write("The edges of the cut with their weights are:\n")
        for u, v, w in cut_edges:
            f.write(f"Edge ({u}, {v}) with weight {w}\n")


def process_all_files(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name.replace(".txt", "_output.txt"))
            run_stoer_wagner(input_file, output_file)
            

if __name__ == "__main__":
    input_dir = "Inputs"  # Replace with your input directory
    output_dir = "Outputs"  # Replace with your output directory
    process_all_files(input_dir, output_dir)