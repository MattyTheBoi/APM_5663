import os
from collections import defaultdict, deque

# Function to read the graph from a file
def read_graph(file_path):
    with open(file_path, 'r') as file:
        num_vertices = int(file.readline().strip())  # First line: number of vertices
        source, sink = map(int, file.readline().strip().split())  # Second line: source and sink vertices
        edges = [tuple(map(int, line.strip().split())) for line in file]  # Remaining lines: edges
    return num_vertices, source, sink, edges

# Function to perform BFS and find an augmenting path
def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:  # If not visited and capacity > 0
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

# Function to implement the Ford-Fulkerson algorithm
def ford_fulkerson(num_vertices, source, sink, edges):
    capacity = defaultdict(lambda: defaultdict(int))
    flow = defaultdict(lambda: defaultdict(int))
    original_capacity = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        capacity[u][v] = w
        original_capacity[u][v] = w
    
    parent = {}
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    # Find the minimum cut
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
    
    min_cut = [(u, v, original_capacity[u][v]) for u in visited for v in original_capacity[u] if v not in visited and original_capacity[u][v] > 0]
    
    return max_flow, flow, min_cut, visited

# Function to write the output to a file
def write_output(file_path, max_flow, flow, min_cut, visited, source):
    with open(file_path, 'w') as file:
        file.write(f"Maximum Flow: {max_flow}\n")
        file.write("Flow values on all edges:\n")
        for u in flow:
            for v in flow[u]:
                if flow[u][v] > 0:
                    file.write(f"Edge {u}-{v}, Flow: {flow[u][v]}\n")
        file.write("Vertices on the left side of the minimum cut:\n")
        visited_list = list(visited)
        visited_list_str = [f"{v} (source)" if v == source else str(v) for v in visited_list]
        file.write(", ".join(visited_list_str) + "\n")
        file.write("Edges in the minimum cut with capacities:\n")
        for u, v, w in min_cut:
            file.write(f"Edge {u}-{v}, Cap: {w}\n")

# Main function to process a single file
def process_file(input_filepath, output_filepath):
    num_vertices, source, sink, edges = read_graph(input_filepath)
    max_flow, flow, min_cut, visited = ford_fulkerson(num_vertices, source, sink, edges)
    write_output(output_filepath, max_flow, flow, min_cut, visited, source)

# Function to process all files in the input directory
def process_all_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):  # Assuming input files have .txt extension
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename.replace(".txt", "_output.txt"))
            process_file(input_filepath, output_filepath)

# Entry point for the program
if __name__ == "__main__":
    input_dir = "Inputs"  # Directory containing input files
    output_dir = "Outputs"  # Directory for output files
    process_all_files(input_dir, output_dir)  # Process all input files