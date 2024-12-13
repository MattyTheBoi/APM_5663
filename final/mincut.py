from collections import defaultdict
from typing import Dict, List, Tuple, Set
import os

def run_stoer_wagner(input_file: str, output_file: str):
    graph = read_graph_from_file(input_file)
    partition, min_cut_weight, cut_edges = compute_min_cut(graph)
    other_side = set(graph) - partition
    write_output_file(output_file, partition, other_side, cut_edges, min_cut_weight)

def merge_vertices(g: Dict[int, List[Tuple[int, int]]], s: int, t: int):
    # Create a new graph without vertex t, merging it into s
    new_graph = defaultdict(list)
    
    for v, edges in g.items():
        if v == t:
            continue  # Skip vertex t

        for dest, weight in edges:
            if dest == t:
                new_graph[v].append((s, weight))  # Merge t into s
            else:
                new_graph[v].append((dest, weight))  # Keep other edges unchanged
    
    # Merge all edges from t to others into s
    for dest, weight in g[t]:
        if dest != s:
            new_graph[s].append((dest, weight))

    return new_graph

def compute_min_cut(graph: Dict[int, List[Tuple[int, int]]] ):
    # "Legal Order" algorithm for Stoer-Wagner min-cut
    def maximum_adjacency_search(g: Dict[int, List[Tuple[int, int]]]):
        visited = set()
        order = []
        weights = defaultdict(int)
        
        # Start with an arbitrary vertex (first one in the graph)
        start = next(iter(g))
        current = start
        visited.add(current)
        order.append(current)
        
        print(f"Starting search with vertex {start}")
        
        for _ in range(len(g) - 1):
            print(f"\nCurrent vertex: {current}")
            # Process all neighbors of the current vertex
            for neighbor, weight in g[current]:
                if neighbor not in visited:
                    weights[neighbor] += weight
                    print(f"    Adding weight for {neighbor}: {weights[neighbor]}")
            
            # Select the next vertex with the maximum weight (If there are multiple, pick the lowest-numbered vertex)
            max_vertex = max(
                (v for v in weights if v not in visited), 
                key=lambda v: (weights[v], -v),  # First prioritize weight, then will prefer lower vertex number (-v)
                default=None
            )

            print(f"    Next candidate max_vertex: {max_vertex} with weight {weights.get(max_vertex, 'N/A')}")
            
            if max_vertex is None:
                break
            
            visited.add(max_vertex)
            order.append(max_vertex)
            current = max_vertex
            print(f"    Visited: {visited}")
            print(f"    Order so far: {order}")

        # The last two vertices form the cut (s, t)
        s, t = order[-2], order[-1]
        cut_weight = weights[t]
        
        print(f"\nFinal vertices for the cut: s = {s}, t = {t}")
        print(f"Cut weight: {cut_weight}")
        print(f"Final order of vertices: {order}")
        
        return s, t, cut_weight, order[:-1]


    original_graph = graph
    best_cut_weight = float('inf')
    best_partition = set()
    cut_edges = []

    while len(graph) > 1:
        s, t, cut_weight, partition = maximum_adjacency_search(graph)
        # Print out the adjacency search result and the cut weight
        print(f"Adjacency search order: {partition}")
        print(f"Cut weight: {cut_weight}")
        # We check if equal as well, since over time, the cut will get smaller, so its easier to check
        if cut_weight <= best_cut_weight:
            # Update the best cut weight and partition
            best_cut_weight = cut_weight
            best_partition = set(partition)
            print(f"New best cut weight: {best_cut_weight}")
            print(f"New best partition: {best_partition}")

            # Collect edges in the cut
            cut_edges = [(u, v, w) for u in original_graph for v, w in original_graph[u] 
                        if u in best_partition and v not in best_partition]
            print(f"Edges in the current best cut: {cut_edges}")
        # Print what we are merging
        print(f"Merging {s} and {t} with cut weight {cut_weight}")
        graph = merge_vertices(graph, s, t)

    return best_partition, best_cut_weight, cut_edges


def read_graph_from_file(file_path: str):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0].strip())
        graph = defaultdict(list)

        for line in lines[1:]:
            u, v, weight = map(int, line.split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))

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
