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
    
    # Merge all edges from t to others into s, except the edge to s
    for dest, weight in g[t]:
        if dest != s:
            new_graph[s].append((dest, weight))
    
    # Remove self-loop from s if it exists
    new_graph[s] = [(v, w) for v, w in new_graph[s] if v != s]

    # Combine parallel edges
    for v, edges in new_graph.items():
        new_edges = defaultdict(int)
        for dest, weight in edges:
            new_edges[dest] += weight
        new_graph[v] = [(dest, weight) for dest, weight in new_edges.items()]

    # list vertice and edges nicely for debugging
    for v, edges in new_graph.items():
        print(f"Vertex {v}: {edges}")

    return new_graph

def compute_min_cut(graph: Dict[int, List[Tuple[int, int]]]):
    # "Legal Order" algorithm for Stoer-Wagner min-cut
    def maximum_adjacency_search(g: Dict[int, List[Tuple[int, int]]] ):
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
            # Process all neighbors of the current vertex
            for neighbor, weight in g[current]:
                if neighbor not in visited:
                    weights[neighbor] += weight
            
            # Select the next vertex with the maximum weight
            max_vertex = max(
                (v for v in weights if v not in visited), 
                key=lambda v: (weights[v], -v),
                default=None
            )
            
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
        
        # Collect edges in the cut *before* merging
        current_cut_edges = [(u, v, w) for u in original_graph for v, w in original_graph[u] 
                             if u in best_partition and v not in best_partition]
        
        print(f"Adjacency search order: {partition}")
        print(f"Cut weight: {cut_weight}")

        if cut_weight <= best_cut_weight:
            best_cut_weight = cut_weight
            best_partition = set(partition)
            print(f"New best cut weight: {best_cut_weight}")
            print(f"New best partition: {best_partition}")

            # Update cut edges for the best partition
            cut_edges = current_cut_edges
            print(f"Edges in the current best cut: {cut_edges}")

        print(f"Merging {s} and {t} with cut weight {cut_weight}")
        print(f"Merging vertices {s} and {t} into {s}")

        # Create a debug print of the merged vertices, and updated it with either another new merged vertex, or appended to a previous
        merged_vertices = f"{s} + {t}"

        print(f"Merged vertices: {merged_vertices}")

        
        # Merge the vertices after the cut has been recorded
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