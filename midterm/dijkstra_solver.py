import os
import heapq
from collections import defaultdict

# Function to read the graph from a file
def read_graph(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        start_vertex, end_vertex = map(int, f.readline().strip().split())
        edges = [tuple(map(int, line.split())) for line in f]
    return num_vertices, start_vertex, end_vertex, edges

# Function to implement Dijkstra's algorithm
def dijkstra(num_vertices, start_vertex, end_vertex, edges):
    graph = defaultdict(list) # Adjacency list representation of the graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    min_heap = [(0, start_vertex)]
    distances = {i: float('inf') for i in range(1, num_vertices + 1)}
    distances[start_vertex] = 0
    previous = {i: None for i in range(1, num_vertices + 1)}
    explored = []

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)
        explored.append(current_vertex)

        if current_vertex == end_vertex:
            break

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(min_heap, (distance, neighbor))

    path = []
    if distances[end_vertex] != float('inf'):
        while end_vertex is not None:
            path.insert(0, end_vertex)
            end_vertex = previous[end_vertex]
    else:
        path = None

    return explored, path

# Function to write the output to a file
def write_output(output_filename, explored, path):
    with open(output_filename, 'w') as f:
        f.write("Explored vertices:\n")
        f.write(" ".join(map(str, explored)) + "\n")
        if path:
            f.write("Minimum weight path:\n")
            f.write(" ".join(map(str, path)) + "\n")
        else:
            f.write("No path found, The start and ending vertices of desired path lie in different components.\n")

# Main function to process a single file
def process_file(input_filepath, output_filepath):
    num_vertices, start_vertex, end_vertex, edges = read_graph(input_filepath)
    explored, path = dijkstra(num_vertices, start_vertex, end_vertex, edges)
    write_output(output_filepath, explored, path)

# Function to process all files in the input directory
def process_all_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):  # Assuming input files have .txt extension
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename.replace(".txt", "_output.txt"))
            process_file(input_filepath, output_filepath)

# Driver code
if __name__ == "__main__":
    input_dir = "Inputs"
    output_dir = "Outputs"
    process_all_files(input_dir, output_dir)